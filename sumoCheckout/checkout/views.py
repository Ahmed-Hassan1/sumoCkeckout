from django.shortcuts import render
from .paying import create_order
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

def callback(request):
    try:
        isSuccess=True if request.GET['status']=="SUCCESS" else False
        context={
            "operation":isSuccess
        }
        return render(request,"checkout/callback.html",context=context)
    except:
        context={
            "operation":False
        }
        return render(request,"checkout/callback.html",context=context)