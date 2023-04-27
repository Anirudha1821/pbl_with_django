from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from resumeb.models import Forms
# above is imp 
from django.contrib import messages
from .pdf import genrate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout






# Create your views here.
def indexreq(request):
    # return HttpResponse("This is home page")

    return render(request,'index.html')
def mytemp(request):

        
    # return HttpResponse("This is home page")

    return render(request,'mytemp.html')
def about(request):
    data={}
    formsData=Forms.objects.all()
    for a in formsData:
        print(a.myname)

    try:
        if request.method =="POST":   
            dbmyname=(request.POST.get('myname'))
            dblname=(request.POST.get('lname'))
            dbno=int(request.POST.get('no'))
            dbemail=(request.POST.get('email'))
            dbcompany=(request.POST.get('company'))
            dbindtext=(request.POST.get('indtext'))
            dbprotext=(request.POST.get('protext'))
            dbcomments=(request.POST.get('comments'))
            data={
                'dbmyname':dbmyname,
                'dblname':dblname,
                'dbno':dbno,
                'dbemail':dbemail,
                'dbcompany':dbcompany,
                'dbindtext':dbindtext,
                'dbprotext':dbprotext,
                'dbcomments':dbcomments, 
                }


    # if  request.POST.get("genratepdf"):
    #     pdf=genrate(about.html)
    #     return HttpResponse(pdf,content_type="application/pdf")
    # else:
    #     return render(request,'about.html',data)
    except:
        pass
    # formsData=Forms.objects.all()
    # for a in formsData:
    #     print(a.myname)
    # print(Forms)

    # try:
    #     if  request.GET.get('genratepdf') == 'myvalue':
    #         # print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    #         pdf=genrate("about.html")
    #         return HttpResponse(pdf,content_type="application/pdf")
    #         # return HttpResponse("hiiskndlk")
    #     else:
    #         return render(request,'about.html',data)
    # except:
    
    
    # to send perticular to perticular site 
    # url="/mytemp/?dbmyname={}".format(myname)
    # return redirect(url)
    
    return render(request,'about.html',data)



    
def temps(request):
    return render(request,'tempmenu.html')
def contact (request):
    return render(request,'contact.html')
def base(request):
    return render(request,'base.html')
def resume(request):
    return render(request,'resume.html')
def tempmenu(request):
    return render(request,'tempmenu.html')
def home(request):
    return render(request,'index.html')
def form_1(request):
    return render(request,'form_1.html')
def login(request):
#     >>> user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    # # At this point, user is a User object that has already been saved
    # # to the database. You can continue to change its attributes
    # # if you want to change other fields.
    # >>> user.last_name = "Lennon"
    # >>> user.save()

    # Ani
    # Ani@21072003
    try:
        if request.method =="POST":
            print("hihihihhihi")
            loginname = request.POST.get('loginname')
            loginpassword  = request.POST.get('loginpassword')
            # print(loginname)
            # print(loginpassword)
            user = authenticate(username='loginname',password="loginpassword")
            if user is not None:
                return redirect('form.html')
            else:
                return render(request,'form.html')
    except:
        pass
    return render(request,'form.html')

        
           
def logoutUser(request):
    logout(request)
    return redirect("/login")
def form(request):
    if request.user.is_anonymous:
        return redirect("/login")
    formsData=Forms.objects.all()
    # for a in formsData:
    #     print(a.myname)
    dt={
        'formsData':formsData
    }
    data={}
    # Above declaration is very imp 
    try:
        if request.method =="POST":
            myname = request.POST.get('myname')
            lname=request.POST.get('lname')
            no=request.POST.get('no')
            email=request.POST.get('email')
            company=request.POST.get('company')
            indtext=request.POST.get('indtext')
            protext=request.POST.get('protext')
            comments=request.POST.get('comments')
            myform= Forms(myname=myname,lname=lname,no=no,email=email,company=company,indtext=indtext,protext=protext,comments=comments)
            myform.save()
            messages.success(request, "Your form submitted succesfully.")
            dbmyname=(request.POST.get('myname'))
            dblname=(request.POST.get('lname'))
            dbno=int(request.POST.get('no'))
            dbemail=(request.POST.get('email'))
            dbcompany=(request.POST.get('company'))
            dbindtext=(request.POST.get('indtext'))
            dbprotext=(request.POST.get('protext'))
            dbcomments=(request.POST.get('comments'))
            data={
                'dbmyname':dbmyname,
                'dblname':dblname,
                'dbno':dbno,
                'dbemail':dbemail,
                'dbcompany':dbcompany,
                'dbindtext':dbindtext,
                'dbprotext':dbprotext,
                'dbcomments':dbcomments, 
                }
    except:
        pass
    return render(request,'form.html',data)

# def form_1(request,form_1):
#     return render(request,'form_1.html')
    
    # return HttpResponse(anyname)     -->>it prints any slug which user enter in url on site 




    