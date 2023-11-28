from django.shortcuts import render

# Create your views here.
def function(request):
    return render(request,'generic_static.html')
    