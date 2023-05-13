from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from resumeb.models import Forms
from resumeb.models import F
# above is imp
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login


# Create your views here.
def indexreq(request):
    # return HttpResponse("This is home page")

    return render(request, 'index.html')


def mytemp(request):

    # return HttpResponse("This is home page")

    return render(request, 'mytemp.html')


def about(request):
    return render(request, 'about.html')


def temps(request):
    return render(request, 'tempmenu.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'contact.html')


def base(request):
    return render(request, 'base.html')


def tempmenu(request):

    mdata = {}
    # formsData=F.objects.all()
    # for a in formsData:
    #     print(a.myname)

    # if request.method == "POST":
    #     print("dsuhufdsfsffd")
    #     mdname = (request.POST.get('dname'))
    #     mdsurname = (request.POST.get('dsurname'))
    #     mdphoneno = (request.POST.get('dphoneno'))
    #     mdemail = (request.POST.get('demail'))
    #     mdcompany = (request.POST.get('dcompany'))
    #     mdcountry = (request.POST.get('dcountry'))
    #     mdcity = (request.POST.get('dcity'))
    #     mdschool = (request.POST.get('dschool'))
    #     mdcollege = (request.POST.get('dcollege'))
    #     mddegree = (request.POST.get('ddegree'))
    #     mdmonth = (request.POST.get('dmonth'))
    #     mdposition = (request.POST.get('dposition'))
    #     mdc1 = (request.POST.get('dc1'))
    #     mdcc1 = (request.POST.get('dcc1'))
    #     mdm1 = (request.POST.get('dm1'))
    #     mdm2 = (request.POST.get('dm2'))
    #     mdpincode = (request.POST.get('dpincode'))
    #     mdata = {
    #         'mdname': mdname,
    #         'mdsurname': mdsurname,
    #         'mdphoneno': mdphoneno,
    #         'mdemail': mdemail,
    #         'mdcompany': mdcompany,
    #         'mdcountry': mdcountry,
    #         'mdcity': mdcity,
    #         'mdschool': mdschool,
    #         'mdcollege': mdcollege,
    #         'mddegree': mddegree,
    #         'mdmonth': mdmonth,
    #         'mdposition': mdposition,
    #         'mdc1': mdc1,
    #         'mdcc1': mdcc1,
    #         'mdcc1': mdcc1,
    #         'mdm1': mdm1,
    #         'mdm2': mdm2,
    #         'mdpincode': mdpincode,
    #     }

    # if  request.POST.get("genratepdf"):
    #     pdf=genrate(about.html)
    #     return HttpResponse(pdf,content_type="application/pdf")
    # else:
    #     return render(request,'about.html',data)

    # return render(request, 'tempmenu.html', mdata)

    mdata = {}
    # formsData=F.objects.all()
    # for a in formsData:
    #     print(a.myname)

    if request.method == "POST":
        print("dsuhufdsfsffd")
        mdname = (request.POST.get('dname'))
        mdsurname = (request.POST.get('dsurname'))
        mdphoneno = (request.POST.get('dphoneno'))
        mdemail = (request.POST.get('demail'))
        mdcompany = (request.POST.get('dcompany'))
        mdcountry = (request.POST.get('dcountry'))
        mdcity = (request.POST.get('dcity'))
        mdschool = (request.POST.get('dschool'))
        mdcollege = (request.POST.get('dcollege'))
        mddegree = (request.POST.get('ddegree'))
        mdmonth = (request.POST.get('dmonth'))
        mdposition = (request.POST.get('dposition'))
        mdc1 = (request.POST.get('dc1'))
        mdcc1 = (request.POST.get('dcc1'))
        mdm1 = (request.POST.get('dm1'))
        mdm2 = (request.POST.get('dm2'))
        mdpincode = (request.POST.get('dpincode'))
        mdata = {
            'mdname': mdname,
            'mdsurname': mdsurname,
            'mdphoneno': mdphoneno,
            'mdemail': mdemail,
            'mdcompany': mdcompany,
            'mdcountry': mdcountry,
            'mdcity': mdcity,
            'mdschool': mdschool,
            'mdcollege': mdcollege,
            'mddegree': mddegree,
            'mdmonth': mdmonth,
            'mdposition': mdposition,
            'mdc1': mdc1,
            'mdcc1': mdcc1,
            'mdcc1': mdcc1,
            'mdm1': mdm1,
            'mdm2': mdm2,
            'mdpincode': mdpincode,
        }
        print(mdata)
    return render(request, 'newform.html', mdata)


def submitf(request):
    mdata = {}
    # formsData=F.objects.all()
    # for a in formsData:
    #     print(a.myname)

    if request.method == "POST":
        print("dsuhufdsfsffd")
        mdname = (request.POST.get('dname'))
        mdsurname = (request.POST.get('dsurname'))
        mdphoneno = (request.POST.get('dphoneno'))
        mdemail = (request.POST.get('demail'))
        mdcompany = (request.POST.get('dcompany'))
        mdcountry = (request.POST.get('dcountry'))
        mdcity = (request.POST.get('dcity'))
        mdschool = (request.POST.get('dschool'))
        mdcollege = (request.POST.get('dcollege'))
        mddegree = (request.POST.get('ddegree'))
        mdmonth = (request.POST.get('dmonth'))
        mdposition = (request.POST.get('dposition'))
        mdc1 = (request.POST.get('dc1'))
        mdcc1 = (request.POST.get('dcc1'))
        mdm1 = (request.POST.get('dm1'))
        mdm2 = (request.POST.get('dm2'))
        mdpincode = (request.POST.get('dpincode'))
        desc = request.POST.get('desc')

        mdata = {
            'mdname': mdname,
            'mdsurname': mdsurname,
            'mdphoneno': mdphoneno,
            'mdemail': mdemail,
            'mdcompany': mdcompany,
            'mdcountry': mdcountry,
            'mdcity': mdcity,
            'mdschool': mdschool,
            'mdcollege': mdcollege,
            'mddegree': mddegree,
            'mdmonth': mdmonth,
            'mdposition': mdposition,
            'mdc1': mdc1,
            'mdcc1': mdcc1,
            'mdm1': mdm1,
            'mdm2': mdm2,
            'mdpincode': mdpincode,
            'desc': desc,

        }
        print(mdata)
    return render(request, 'newform.html', mdata)
#


def newform(request):

    print("-----------------------------GET----------------------------")
    # formsData = F.objects.all()
    # print(formsData)

    mdata = {}
    # Above declaration is very imp
    if request.method == "POST":
        print("----------------------------------POST---------------------------------")
        # print(formsData)

        dname = request.POST.get('dname')
        dsurname = request.POST.get('dsurname')
        dphoneno = request.POST.get('dphoneno')
        demail = request.POST.get('demail')
        dcountry = request.POST.get('dcountry')
        dcity = request.POST.get('dcity')
        desc = request.POST.get('desc')
        dpincode = request.POST.get('dpincode')
        dcompany = (request.POST.get('dcompany'))
        dschool = (request.POST.get('dschool'))
        dcollege = (request.POST.get('dcollege'))
        ddegree = (request.POST.get('ddegree'))
        dmonth = (request.POST.get('dmonth'))
        dposition = (request.POST.get('dposition'))
        dc1 = (request.POST.get('dc1'))
        dcc1 = (request.POST.get('dcc1'))
        dm1 = (request.POST.get('dm1'))
        dm2 = (request.POST.get('dm2'))
        myF = F(dname=dname, dsurname=dsurname, dphoneno=dphoneno, demail=demail,
                dcountry=dcountry, dcity=dcity, desc=desc, dpincode=dpincode,dschool=dschool, dcollege=dcollege,
                ddegree=ddegree, dmonth=dmonth,dposition=dposition, dc1=dc1, dcc1=dcc1, dm1=dm1, dm2=dm2,dcompany=dcompany)
        myF.save()
        messages.success(request, "Your form submitted succesfully.")
        mdname = (request.POST.get('dname'))
        mdsurname = (request.POST.get('dsurname'))
        mdphoneno = (request.POST.get('dphoneno'))
        mdemail = (request.POST.get('demail'))
        mdesc = (request.POST.get('desc'))
        mdcountry = (request.POST.get('dcountry'))
        mdcity = (request.POST.get('dcity'))
        mdpincode = (request.POST.get('dpincode'))
        mdschool = (request.POST.get('dschool'))
        mdcollege = (request.POST.get('dcollege'))
        mddegree = (request.POST.get('ddegree'))
        mdmonth = (request.POST.get('dmonth'))
        mdposition = (request.POST.get('dposition'))
        mdcompany = (request.POST.get('dcompany'))
        mdc1 = (request.POST.get('dc1'))
        mdcc1 = (request.POST.get('dcc1'))
        mdm1 = (request.POST.get('dm1'))
        mdm2 = (request.POST.get('dm2'))
        mdata = {
            'mdname': mdname,
            'mdsurname': mdsurname,
            'mdphoneno': mdphoneno,
            'mdemail': mdemail,
            'mdcountry': mdcountry,
            'mdcity': mdcity,
            'mdesc': mdesc,
            'mdpincode': mdpincode,
            'mdcompany': mdcompany,
            'mdschool': mdschool,
            'mdcollege': mdcollege,
            'mddegree': mddegree,
            'mdmonth': mdmonth,
            'mdposition': mdposition,
            'mdc1': mdc1,
            'mdcc1': mdcc1,
            'mdm1': mdm1,
            'mdm2': mdm2,
        }

    return render(request, 'newform.html', mdata)


def newform1(request):
    mdata = {}
    # Above declaration is very imp
    try:
        if request.method == "POST":
            dschool = request.POST.get('dschool')
            dcollege = request.POST.get('dcollege')
            ddegree = request.POST.get('ddegree')
            dmonth = request.POST.get('dmonth')
            myF = F(dschool=dschool, dcollege=dcollege,
                    ddegree=ddegree, dmonth=dmonth)
            myF.save()
            messages.success(request, "Your form submitted succesfully.")
            mdschool = (request.POST.get('dschool'))
            mdcollege = (request.POST.get('dcollege'))
            mddegree = (request.POST.get('ddegree'))
            mdmonth = (request.POST.get('dmonth'))
            mdata = {
                'mdschool': mdschool,
                'mdcollege': mdcollege,
                'mddegree': mddegree,
                'mdmonth': mdmonth,
            }
    except:
        pass
    return render(request, 'newform1.html', mdata)


def newform2(request):
    mdata = {}
    # Above declaration is very imp
    try:
        if request.method == "POST":
            dposition = request.POST.get('dposition')
            dc1 = request.POST.get('dc1')
            dcc1 = request.POST.get('dcc1')
            dm1 = request.POST.get('dm1')
            dm2 = request.POST.get('dm2')
            myF = F(dposition=dposition, dc1=dc1, dcc1=dcc1, dm1=dm1, dm2=dm2)
            myF.save()
            messages.success(request, "Your form submitted succesfully.")
            mdposition = (request.POST.get('dposition'))
            mdc1 = (request.POST.get('dc1'))
            mdcc1 = (request.POST.get('dcc1'))
            mdm1 = (request.POST.get('dm1'))
            mdm2 = (request.POST.get('dm2'))
            mdata = {
                'mdposition': mdposition,
                'mdc1': mdc1,
                'mdcc1': mdcc1,
                'mdcc1': mdcc1,
                'mdm1': mdm1,
                'mdm2': mdm2,
            }
    except:
        pass
    return render(request, 'newform2.html')


def newform3(request):

    return render(request, 'form.html')


def form(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    formsData = Forms.objects.all()
    # for a in formsData:
    #     print(a.myname)
    dt = {
        'formsData': formsData
    }
    data = {}
    # Above declaration is very imp
    try:
        if request.method == "POST":
            myname = request.POST.get('myname')
            lname = request.POST.get('lname')
            no = request.POST.get('no')
            email = request.POST.get('email')
            company = request.POST.get('company')
            indtext = request.POST.get('indtext')
            protext = request.POST.get('protext')
            comments = request.POST.get('comments')
            myform = Forms(myname=myname, lname=lname, no=no, email=email,
                           company=company, indtext=indtext, protext=protext, comments=comments)
            myform.save()
            messages.success(request, "Your form submitted succesfully.")
            dbmyname = (request.POST.get('myname'))
            dblname = (request.POST.get('lname'))
            dbno = int(request.POST.get('no'))
            dbemail = (request.POST.get('email'))
            dbcompany = (request.POST.get('company'))
            dbindtext = (request.POST.get('indtext'))
            dbprotext = (request.POST.get('protext'))
            dbcomments = (request.POST.get('comments'))
            data = {
                'dbmyname': dbmyname,
                'dblname': dblname,
                'dbno': dbno,
                'dbemail': dbemail,
                'dbcompany': dbcompany,
                'dbindtext': dbindtext,
                'dbprotext': dbprotext,
                'dbcomments': dbcomments,
            }
    except:
        pass
    return render(request, 'form.html', data)


def form_1(request):
    return render(request, 'form_1.html')
def rat(request):
    return render(request, 'rat.html')


def loginUser(request):
    #     >>> user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    # # At this point, user is a User object that has already been saved
    # # to the database. You can continue to change its attributes
    # # if you want to change other fields.
    # >>> user.last_name = "Lennon"
    # >>> user.save()

    # Ani
    # Ani@21072003
    try:
        if request.method == "POST":
            print("hihihihhihi")
            loginname = request.POST.get('loginname')
            loginpassword = request.POST.get('loginpassword')
            # print(loginname)
            # print(loginpassword)
            user = authenticate(username=loginname, password=loginpassword)
            if user is not None:
                login(request, user)
                return redirect('/contact')
            else:
                return render(request, 'login.html')
    except:
        pass
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
# def form_1(request,form_1):
#     return render(request,'form_1.html')

    # return HttpResponse(anyname)     -->>it prints any slug which user enter in url on site
