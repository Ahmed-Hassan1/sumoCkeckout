from django.shortcuts import render
from .paying import create_order
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
# Create your views here.


def homePage(request):
    response=create_order()
    print(response)
    url=response['data']['checkoutUrl']
    context={
        "url":url
    }
    return render(request,"checkout/index.html",context=context)


def test(request):
    response=create_order()
    print(response)
    return render(request,"checkout/test.html")

@csrf_exempt
def callback(request):
    file=Sumo.objects.all().last()
    print(file)
    context={
        "operation":True,
        "file":file
    }
    return render(request,"checkout/callback.html",context=context)
    # try:
    #     if request.method=='GET':
    #         print("============================")
    #         print(request.GET)
    #         isSuccess=True if request.GET['status']=="SUCCESS" else False
    #         context={
    #             "operation":isSuccess,
    #             "file":file
    #         }
    #         return render(request,"checkout/callback.html",context=context)
    #     if request.method=='POST':
    #         body_unicode = request.body.decode('utf-8')
    #         body = json.loads(body_unicode)
    #         content = body['content']
    #         print("============================")
    #         print(request.body)
    #         print("............................")
    #         print(content)
    #         isSuccess=True if content['status']=="SUCCESS" else False
    #         context={
    #             "operation":isSuccess,
    #             "file":file
    #         }
    #         return render(request,"checkout/callback.html",context=context)
    # except Exception  as e:
    #     print(file)
    #     print(e)
    #     context={
    #         "operation":True,
    #         "file":file
    #     }
    #     return render(request,"checkout/callback.html",context=context)

def fail(request):

    return render(request,"checkout/fail.html")