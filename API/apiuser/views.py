import json
from django.forms import ValidationError
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views import View
from .serializer.userdto import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.


class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd=json.loads(request.body)
        try:
            serializer = UserSerializer(data=jd)
            serializer.is_valid()
            user = User.objects.create_user(
                username=jd['username'],
                email=jd['email'],
                password=jd['password']
            )
            response = ({'message': 'User created successfully.'})
            return JsonResponse(response)
        except ValidationError as e:
            return HttpResponseBadRequest(e.detail)
