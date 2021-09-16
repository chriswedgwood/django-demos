from django.shortcuts import render
from PIL import Image  
from base64 import b64encode
from mimetypes import guess_type

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def upload_photo(request):
    pass





from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadPhotoForm

# Imaginary function to handle an uploaded file.
def handle_uploaded_file(photo):
    print(photo)

def upload_photo(request):
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadPhotoForm()
    return render(request, 'cropper/upload_photo.html', {'form': form})


def image_change(request):
    folder = 'images/'
    myfile = request.FILES['q']
    fs = FileSystemStorage() #defaults to   MEDIA_ROOT  
    filename = fs.save(myfile.name, myfile)
    file_url = fs.url(filename)
    return render(request, "cropper/upload_image.html", {'file_url':file_url})

