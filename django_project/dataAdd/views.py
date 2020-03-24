from django.shortcuts import render,HttpResponse
from .forms import data_add
from login.models import User
# Create your views here.
def add_data(request):
    if request.method== 'POST':
        form=data_add(request.POST)
        if form.is_valid():
            print(form,"hhhh",request.POST)
            new_form=form.save(commit=False)
            user_obj=User.objects.get(id=request.session['id'])
            new_form.user_id= user_obj
            new_form.save()
            return HttpResponse('done')

    else:
        form= data_add()
    
    context={
        'form':form,
    }
    return render (request,'addextradata.html',context)