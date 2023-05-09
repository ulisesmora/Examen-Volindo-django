from typing import Any
from django import http
from django.forms import ValidationError
from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .seralizer.taskdto import taskSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
import jwt
# Create your views here.
class TaskView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get(self,request, id=0):
        if(id>0):
            tasks=list(Task.objects.filter(id=id).values())
            if len(tasks) > 0 : 
                task = tasks[0]
                datos={'message':"Success",'tak':task}
            else:
                datos={'message':"Task not found..."}
            return JsonResponse(datos)        
        else:
            decoded_data=(jwt.decode(str(request.auth), 'PASSWORD', 'utf-8'))    
            tasks = list(Task.objects.filter(user_id=decoded_data['user_id']).values())
            if len(tasks) > 0 : 
                datos={'message':"Success",'taks':tasks}
            else:
                datos={'message':"Tasks not found..."}    
        return JsonResponse(datos)

    def post(self,request):
        try:
            jd=json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid Json")
        serializer = taskSerializer(data=jd)
        try:
            serializer.is_valid(raise_exception=True)
            decoded_data=(jwt.decode(str(request.auth), 'PASSWORD', 'utf-8'))
            Task.objects.create(title=jd['title'], description=jd['description'],user_id=decoded_data['user_id'])
            datos={'message':"Success"}
            return JsonResponse(datos)
        except ValidationError as e:
            return HttpResponseBadRequest(e.detail)

    def put(self,request,id):
        try:
            jd=json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid Json")
        serializer = taskSerializer(data=jd)
        tasks=list(Task.objects.filter(id=id).values())
        try:
            serializer.is_valid(raise_exception=True) 
            if len(tasks) > 0 :
                task = Task.objects.get(id=id)
                task.title = jd['title']
                task.description = jd['description']
                task.save()
                datos = {'message': "Success"}
            else:
                datos={'message':"Task not found..."}
            return JsonResponse(datos)
        except ValidationError as e:
            return HttpResponseBadRequest(e.detail)

        
    def delete(self,request,id):
        tasks=list(Task.objects.filter(id=id).values())
        if len(tasks) > 0 : 
            Task.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos={'message':"Task not found..."}
        return JsonResponse(datos)

