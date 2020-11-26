from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .forms import *
from django.http import HttpResponseRedirect
import os

"""
Resources Used:

- https://stackoverflow.com/questions/39341895/django-errorcant-specify-the-download-filename
- https://docs.djangoproject.com/en/3.1/topics/forms/
- https://docs.djangoproject.com/en/3.1/topics/http/file-uploads/
- https://docs.djangoproject.com/en/3.0/
- https://docs.djangoproject.com/en/3.1/howto/static-files/


"""




def AboutUsAndDownload(request):
    if request.method == 'POST':
        return FileResponse(open("Patient Form.png", 'rb'), as_attachment=True, filename='MedicalForm.png')
    Data = {}

    return render(request,"CoreBackend/index.html",Data)

def UploadPage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open('CurrentImage', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
            return HttpResponseRedirect('/results/')
    else:
        form = UploadFileForm()

    Data = {'form': form}
    return render(request,"CoreBackend/upload.html",Data)

def EDAAndResults(request):
    Data = {}
    return render(request, "CoreBackend/results.html", Data)

def Contributors(request):
    Data = {}
    return render(request, "CoreBackend/contributors.html", Data)

def Project(request):
    Data = {}
    return render(request, "CoreBackend/description.html", Data)