from django.contrib import admin
from django.urls import path
from resumeb import views

urlpatterns = [
    path("",views.indexreq,name="home_page"),
    path("home",views.home,name="home"),
    path("about",views.about,name='about'),
    path("form",views.form,name='form'),
    path("carrer_center",views.carrer_center,name='carrer_center'),
    path("contact",views.contact,name='contact'),
    path("base",views.base,name='base'),
    path("tempmenu",views.tempmenu,name='base'),
    path("submitf",views.submitf,name=''),
    path("resume1",views.resume1,name=''),
    path("resume2",views.resume2,name=''),
    path("rat",views.rat,name=''),
    # path("form",views.form,name='form'),
    path("newform",views.newform,name='newform'),
    path("newform1",views.newform1,name='newform1'),
    path("newform2",views.newform2,name='newform2'),
    path("newform3",views.newform3,name='newform3'),
    path("aboutus",views.aboutus,name='aboutus'),
    # path("form_1",views.form_1,name='form_1'),
    path("mytemp",views.mytemp,name='my-temp-form'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout'),
    path("options",views.options,name='options'),
    
    # SLUG 
    
    # path("form/<str:form_1>",views.form_1,name='form_1'),
    
    # In views.py ...we add the following functions-->> 
    
    # def carrer_center(request,anyname):
    #     return render(request,'tempmenu.html')
    
        # return HttpResponse(anyname)     -->>it prints any slug which user enter in url on site 



]
