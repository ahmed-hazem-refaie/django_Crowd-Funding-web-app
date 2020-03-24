from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.db import connection
from django.contrib import  messages
from django.db.models import Q
from operator import itemgetter
from django.contrib import  messages
from user_projects.models import *



# Create your views here.
cursor = connection.cursor()
def homepage(request):
     projectsCategory=cursor.execute('select user_projects_projects.project_title from user_projects_projects join user_projects_category where user_projects_projects.category_id_id==user_projects_category.category_id ;')
     records = projectsCategory.fetchall()

     categoryobj = Category.objects.all()

     latestproject=cursor.execute('SELECT user_projects_projects.project_title FROM user_projects_projects ORDER BY user_projects_projects.start_time  DESC LIMIT 5;')
     recentProject = [', '.join(map(str, x)) for x in latestproject]

     adminProjectsChoice=cursor.execute('select user_projects_projects.project_title FROM user_projects_projects where user_projects_projects.project_show == 1;')
     adminChoice = [', '.join(map(str, x)) for x in adminProjectsChoice]

     highestRating=cursor.execute('select user_projects_projects.project_title, sum(rate)as sumRating from user_projects_projects join user_projects_rate where user_projects_projects.project_id == user_projects_rate.project_id_id GROUP by user_projects_rate.project_id_id order by sumRating DESC limit 5;')
     highestProjects = [', '.join(map(str, x)) for x in highestRating]
     # ////////
     highestRating1 = cursor.execute(
         'select user_projects_projects.project_id, user_projects_projects.project_title, sum(rate)as sumRating,user_projects_projects.total_target from user_projects_projects join user_projects_rate where user_projects_projects.project_id == user_projects_rate.project_id_id GROUP by user_projects_rate.project_id_id order by sumRating DESC limit 5;')
     x=highestRating1.fetchall()
     print(highestRating1.fetchall(),'klm',x[0][1])
     highestProjects1 = [', '.join(map(str, x)) for x in highestRating1]

     if 'id' in request.session:
         return render(request, "home.html", {'categoryobj': categoryobj,
                                          # 'projectsCategory':projectsCategory,
                                          'highestProjects': highestProjects,
                                          'recentProject': recentProject,
                                          'adminChoice': adminChoice,
                                              'highestProjects1': x,
                                          })
     else:

         return redirect('/login')


def category (request):
    if request.method=='GET':
        catId=request.GET.get('cat_id', False)

        if catId:
            match=Category.objects.filter(Q(category_id__iexact=catId))
            if match:
                projectcat=Projects.objects.filter(category_id_id=catId)
                if 'id' in request.session:
                    return render(request, "categories.html", {'cat_id': match, 'projectcat': projectcat})

                else:
                    return redirect('/login')
            else :
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('')

    if 'id' in request.session:
        return render(request, "categories.html")

    else:
        return redirect('/login')


def search(request):
    if request.method=='POST':
        title=request.POST.get('title_search', False)

        if title:
            match=Projects.objects.filter(Q(project_title__iexact=title))
            if match:
                return render(request,"searchResult.html",{'stitle':match})
            else :
                messages.error(request,'no result found')

        tag =  request.POST.get('tag_search', False)
        if tag:
            tmatch = Tags.objects.filter(Q(tag_name__iexact=tag))
            if tmatch:
                return render(request, "searchResult.html", {'stag': tmatch})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('search')
    if 'id' in request.session:
        return render(request, "searchResult.html")
    else:
        return redirect('/login')



