from django.shortcuts import render

# Create your views here.


def homePage(request):

    print(request.body)
    return render(request,"sumoCheckout/index.html")