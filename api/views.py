from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework import request, response
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status


from .models import Task
from .serializers import TaskSerializers


# Create your views here.
class HomePage(View):
    def get(self, request: HttpRequest):
        task = Task.objects.all()
        ruyxat = []
        for item in task:
            serialazers = TaskSerializers(item)
            data = serialazers.data
            ruyxat.append(data)
        return JsonResponse(ruyxat, safe=False)

@api_view(['GET'])
def GetRequestView(request: request):
    print("So'rov: ", request)
    print("Data: ", request.data)
    print("Query params: ", request.query_params)
    print("Parsers: ", request.parsers)
    print("Accepted_renderer", request.accepted_renderer)
    print("Accepted media type: ", request.accepted_media_type)
    print("User: ", request.user)
    print("Auth: ", request.auth)
    print("Method: ", request.method)
    print("Content type: ", request.content_type)
    print("Stream: ", request.stream)
    data = {"statust":"Get orqali request so'rovi"}

    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def PostRequestView(request: request):
    print(request)
    print("Data: ", request.data)
    print("Query params: ", request.query_params)
    print("Parsers: ", request.parsers)
    print("Accepted_renderer", request.accepted_renderer)
    print("User: ", request.user)
    print("Auth: ", request.auth)
    print("Method: ", request.method)
    print("Content type: ", request.content_type)
    print("Stream: ", request.stream)
    data = {"statust":"Post orqali request so'rovi"}
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetResponseView(response: response):
    print(response)
    print("Data: ", response.data)
    print("status: ", response.status)
    # print("template name: ", response.template_name)
    # print("headers: ", response.headers)
    # print('content type', response.content_type)
    # print('conten: ', response.content)
    data = {"status": "Get orqali response so'rovi"}
    return Request(request=data)

