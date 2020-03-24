from django.shortcuts import render

# Create your views here.
def rejesterform (request):
    return render(request,'indexform.html')
