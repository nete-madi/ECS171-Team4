
 0. Get Pycharm Pro(Free Education license: https://www.jetbrains.com/community/education/#students)
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
    Data = {}  
    return render(request,"CoreBackend/index.html",Data)  
  
def UploadPage(request):  
    Data = {}  
    return render(request,"CoreBackend/upload.html",Data)  
  
def EDAAndResults(request):  
    Data = {}  
    return render(request, "CoreBackend/results.html", Data)
```
8. Add a new directory to your `templates` directory called `CoreBackend`
9.  Add the following files to `templates/CoreBackend`: `results.html`,`index.html`,`upload.html`
10. Paste this into your `index.html`:
```
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
<p style="color:green"> This the about page!</p>  
</body>  
</html>
```
11. Paste this into your `results.html`:
```
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
<p style="color:red"> This the result page!</p>  
</body>  
</html>
```
12. Paste this into your `upload.html`:
```
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
<p style="color:blue"> This the upload page!</p>  
</body>  
</html>
```
13. Now if you go these pages: the html should be sent back to you instead of just text like before!
