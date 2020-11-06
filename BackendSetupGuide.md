 1. Open Pycharm : Create basic Django project (make sure to use Virtualenv)
 2. Add `import os` to the settings.py
 3. Run `python manage.py startapp CoreBackend`. This will initialize the sub-app directory/files.
 4. Create a `urls.py` in the CoreBackend directory.
 5. Paste the following code in the `CoreBackend/urls.py`:
```
from django.urls import path  
  
from . import views  
  
urlpatterns = [  
    path('', views.AboutUsAndDownload, name='index'),  
    path('upload/', views.UploadPage, name='upload'),  
    path('results/', views.EDAAndResults, name='edaresults')  
]
```
6. Paste the following code in the `ECS171Backend\urls.py`
```
from django.contrib import admin  
from django.urls import include,path  
  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',include('CoreBackend.urls')),  
]

``` 
7. Paste this code in the `CoreBackend\views.py`:
```
from django.shortcuts import render  
from django.http import HttpResponse  
  
  
def AboutUsAndDownload(request):  
    return HttpResponse("Hello, world. You're at the About us page!")  
  
def UploadPage(request):  
    return HttpResponse("Hello, world. You're at the Upload page!")  
  
def EDAAndResults(request):  
    return HttpResponse("Hello, world. You're at the EDA and Results page!")
```
8. Run `python manage.py runserver`
