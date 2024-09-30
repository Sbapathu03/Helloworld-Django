from django.http import JsonResponse
from django.shortcuts import render

# JSON response
def hello_world_json(request):
    return JsonResponse({"Message": "Hello World!"})

# HTML response
def hello_world_html(request):
    return render(request, 'api/hello.html') 
