"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rejester.views import rejesterform
from login.views import my_login,activate,login,update,delete_user,logout,forget_my_password,my_profile
from dataAdd.views import add_data
from user_projects import views as user_projects
from projectlist import views as projectlist_view
from django.urls import path, include
from home import  views



urlpatterns = [
    path('admin/', admin.site.urls),
    #login and rejesteration
    path('rejester/',rejesterform),
    path('login/',my_login),
    path('logout/',logout ),
    path('activate/<activeno>/',activate),
    path('login/profile',login),
    path('update/',update),
    path('add/data',add_data),
    path('delete/profile',delete_user),
    path('forget/my_pass',forget_my_password),
    path("my_profile/",my_profile),
    # user_project
    path('projects/add', user_projects.add_project),
    path('projects/save', user_projects.save_project),
    path('projects/rate', user_projects.rate_project),
    path('projects/cancel', user_projects.cancel_project),
    path('projects/<int:_id>', user_projects.project_details),
    path('categories/add', user_projects.add_category),
    path('comments/add', user_projects.add_comment),
    path('comments/reply', user_projects.reply_comment),
    path('donation/add', user_projects.add_donation),
    path('projectlist/', projectlist_view.all_project),
    path('donationlist/', projectlist_view.all_donation),
    path('project/report', user_projects.report_project),
    path('comment/report', user_projects.report_comment),
#     maryam
    path('home/', include('home.urls')),
 path("home/search",views.search),
path("home/category/",views.category),

]

from django_project import  settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
