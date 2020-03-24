from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, Count, F
from user_projects.models import *


def add_project(request):
    if 'id' in request.session:

        return render(request,"user_projects/add_project.html", {"categories" : Category.objects.all()})
    else:
        return  redirect('/login')


def add_category(request):
    if request.method == "POST":
        Category(None,request.POST["name"]).save()
        return redirect("/projects/add")


def save_project(request):
    if request.method == "POST":
        user = User.objects.get(id = request.session['id'])
        category = Category.objects.get(category_id = request.POST["project_category"])
        my_project = Projects(project_title = request.POST["project_title"], project_details = request.POST["project_description"], total_target = request.POST["project_total_target"], start_time = request.POST["project_start_date"], end_time = request.POST["project_end_date"], category_id = category, user_id = user)
        my_project.save()

        for tag in request.POST["project_tags"].split(","):
            Tags(project_id = my_project, tag_name = tag).save()

        for _img in request.FILES.getlist('project_images[]'):
            FileSystemStorage(location='/images')
            Images(project_id = my_project, img = _img).save()

        # return ('/projects/' + my_project.project_id +'/')
        return  redirect(f"/projects/{my_project.project_id }")
        # return render(request,"user_projects/project_details.html", {"projects" : Projects.objects.all()})
    else:
        if 'id' in request.session:
            return render(request,"user_projects/add_project.html")
        else:
            return redirect('/login')


def project_details(request, _id):
    if 'id' in request.session:
        print('mwgooooookokokokokokokd')
        project_data = Projects.objects.get(project_id=_id)
        project_category = Category.objects.get(category_id=project_data.category_id_id)
        project = {"data": project_data, "category": project_category,
                   "total_donate": project_data.donation_set.all().aggregate(Sum('donation_amount')),
                   "rate_sum": project_data.rate_set.all().aggregate(Sum('rate')),
                   "rate_count": project_data.rate_set.all().aggregate(Count('rate'))}
        # return render(request,"user_projects/project_details.html", project)
        return render(request, "user_projects/sliderpase.html", project)

    else:
        print('sssssssssss')
        return redirect('/login')





def add_comment(request):
    if request.method == "POST":
        project = Projects.objects.get(project_id = request.POST["project_id"])
        user = User.objects.get(id = request.session['id'])
        Comment(user_id = user, project_id = project, comment_content = request.POST["content"]).save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def reply_comment(request):
    if request.method == "POST":
        comment = Comment.objects.get(comment_id = request.POST["comment_id"])
        user = User.objects.get(id = request.session['id'])
        SubComment(comment_id = comment, user_id = user, comment_content = request.POST["content"]).save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_donation(request):
    if request.method == "POST":
        project = Projects.objects.get(project_id = request.POST["project_id"])
        user = User.objects.get(id = request.session['id'])
        is_donated = Donation.objects.filter(user_id = user, project_id = project)
        if not is_donated:
            Donation(user_id = user, project_id = project, donation_amount = request.POST["amount"]).save()
        else:
            Donation.objects.filter(user_id = user, project_id = project).update(donation_amount = F("donation_amount") + request.POST["amount"])
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def rate_project(request):
    if request.method == "POST":
        project = Projects.objects.get(project_id = request.POST["project_id"])
        user = User.objects.get(id = request.session['id'])
        is_rated = Rate.objects.filter(user_id = user, project_id = project)
        if not is_rated:
            Rate(user_id = user, project_id = project, rate = request.POST["rate"]).save()
        else:
            Rate.objects.filter(user_id = user, project_id = project).update(rate = request.POST["rate"])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def cancel_project(request):
    if request.method == "POST":
        Projects.objects.filter(project_id = request.POST["project_id"]).delete()
        return HttpResponseRedirect("/projects/add")


def report_comment(request):
    if request.method == "POST":
        print(request.POST,'fffff')
        comment = Comment.objects.get(project_id = request.POST["comment_id"])
        user = User.objects.get(id = request.session["id"])
        CommentReports(comment_id = comment, user_id = user).save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def report_project(request):
    if request.method == "POST":
        print(request.POST,"sssss")
        project = Projects.objects.get(project_id = request.POST["project_id"])
        user = User.objects.get(id = request.session["id"])
        ProjectReports(project_id = project, user_id = user).save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

