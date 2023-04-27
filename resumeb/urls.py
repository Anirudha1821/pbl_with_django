from django.contrib import admin
from django.urls import path
from resumeb import views

urlpatterns = [
    path("",views.indexreq,name="home_page"),
    path("home",views.home,name='home'),
    path("about",views.about,name='about'),
    path("temps",views.temps,name='temps'),
    path("contact",views.contact,name='contact'),
    path("resume",views.resume,name='base'),
    path("base",views.base,name='base'),
    path("tempmenu",views.tempmenu,name='base'),
    path("form",views.form,name='form'),
    path("form_1",views.form_1,name='form_1'),
    path("mytemp",views.mytemp,name='my-temp-form'),
    path("login",views.login,name='login'),
    path("logoutUser",views.login,name='logout'),
    
    # SLUG 
    
    # path("form/<str:form_1>",views.form_1,name='form_1'),
    
    # In views.py ...we add the following functions-->> 
    
    # def temps(request,anyname):
    #     return render(request,'tempmenu.html')
    
        # return HttpResponse(anyname)     -->>it prints any slug which user enter in url on site 



]
