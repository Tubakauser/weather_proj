from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def weather_app(request):
    if request.method == "POST":
        lati = request.POST["lat"]
        logn = request.POST["long"]
        print(lati,logn)
        return render(request,"weather.html",{"lati":lati,"logn":logn})

    return render(request,"weather.html")
