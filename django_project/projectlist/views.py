from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from user_projects.models import *



#return projects of specific user by user_id
def all_project(request):
    user_obj=User.objects.get(id=request.session['id'])
    all_project =Projects.objects.all().filter(user_id = user_obj )
    
    context = {
      'all_project' : all_project,
    }
    # return HttpResponse(all_project.project_title)
    if 'id' in request.session:
        return render(request,'all_project.html',context)
    else:
        return  redirect('/login')
    



def all_donation(request):
    user_obj=User.objects.get(id=request.session['id'])
    all_donation =Donation.objects.all().filter(user_id = user_obj)
    
    context = {
      'all_donation' : all_donation,
    }
    if 'id' in request.session:
        return render(request, 'all_donation.html', context)
    else:
        return redirect('/login')





def project(request,id):
    pass

