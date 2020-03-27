from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms_log import  rejesterform
from django.views.generic import TemplateView
from .models import User
from django.contrib import messages
from django.core.mail import send_mail
import  uuid
from .models import User
from django.contrib import messages
from  datetime import  datetime,timedelta


# Create your views here.

class Home (TemplateView):
    template_name = 'myindexform.html'

def my_login(request):
    form=rejesterform()
    if request.method=='POST':
        code=uuid.uuid4()
        values=request.POST
        # values['code']=code
        # values['state']='D'
        print(request.FILES)

        form=rejesterform(values,request.FILES)
        if form.is_valid():
            print('validddddd')
            a=form.save()
            print(a)
            a.code=code
            a.save()
            send_mail(
                'hello activate here',
                f"Welcome to our website activate here  http://localhost:8000/activate/{code}",
                'django4iti@gmail.com',
                [a.email],
                fail_silently=False,
            )
            messages.success(request, 'Profile details updated.')
            return render(request,'myindexform.html',{'form':form})
        else:
            print(form.errors,"hh")
            # messages.success(request,'not valid yabaa')
            return render(request,'myindexform.html',{'form':form})
    return render(request, 'myindexform.html', {'form': form})















# for activation
def activate (request,activeno):
     print(User.objects.filter(code=activeno))
     user_obj=User.objects.filter(code=activeno)
     if user_obj:
        user_obj=user_obj[0]
        user_obj.state='A'
        if user_obj.datetime.date() == datetime.today().date():
            user_obj.save()
        else:
            user_obj.delete()
            return HttpResponse("<h1>your account has been deleted because u activate it late plz create new one <br>"
                                "<hr>"
                                "<h2>via this link ---->></h2><hr><hr>"
                                '<a href="http://localhost:8000/login">#login Here </a>')

        return HttpResponse("<h1>Activation Done <a href="
                            "http://localhost:8000/login"
                            ">#Click _to login now with your data</a></h1>")
     else:
         return HttpResponse("<h1>your account has been deleted because u activate it late plz create new one <br>.."
                            "<hr>"
                            "<h2>via this link ---->></h2><hr><hr>"
                            '<a href="http://localhost:8000/login">#login Here </a>')


    # mm.date() == datetime.today().date())


def update (request):
    if 'id' in request.session :

        user_obj = User.objects.filter(id=request.session['id'])
        if user_obj:
            user_obj = user_obj[0]
            form = rejesterform(request.POST  or None  ,request.FILES or None,instance=user_obj)
            if request.POST and form.is_valid():
                form.save()
                return HttpResponse('done')

    return render(request, 'myindexform.html', {'form': form ,'edit':True,'password':user_obj.password})

def login (request):
    if request.method=='POST':
        print(request.POST['email'])
        if request.POST['email'] and request.POST['password']:
            user_obj = User.objects.filter(email=request.POST['email'],password=request.POST['password'],state='A')
            if user_obj:
                user_obj = user_obj[0]
                request.session['id'] = user_obj.id
                request.session['name'] = user_obj.f_name
                request.user.f_name='done'
                print(request.user.f_name)
                # return render(request, 'profile.html', {'info':user_obj})
                return redirect('/my_profile')
            else:
                messages.success(request,'not found rejester here or need to activate via email in the span message -->')
                return redirect('/login/')


        else:
            messages.success(request, 'not allowed input data')
            return redirect('/login/')

    else:
        return redirect('/login/')

def my_profile (request):
    if 'id' in request.session:
        user_obj=User.objects.get(id=request.session['id'])
        return render(request, 'profile.html', {'info':user_obj})
    else:
        return redirect('/login')
def logout (request):
    request.session.flush()
    return  redirect('/login')


# deleting
def delete_user (request):

    post = get_object_or_404(User, id=request.session['id'])
    post.delete()
    messages.success(request,'deleted')
    return  redirect('/login')


def forget_my_password (request):
    print('hi')
    if request.method == 'POST':
        print (request.POST['email'])
        find_user=User.objects.filter(email=request.POST['email'])
        if find_user:
            send_mail(
                'email get password to login ',
                f"we happy to reget ur pass again  pass is ===>      {find_user[0].password}",
                'django4iti@gmail.com',
                [find_user[0].email],
                fail_silently=False,
                    )
            messages.success(request, 'password sent to ur mail')
        else:
            messages.success(request, 'not rejestered or not activated ')

        return redirect('/login')
    else:
        return redirect('/login')

