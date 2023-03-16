from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from photo_app.models import Photo
from photo_app import forms

# Create your views here.


def index(request):
    all_photos = Photo.objects.order_by('-upload_date').filter(is_archived=False)
    # Return list of lists of 3 for rows
    photo_list = [all_photos[i:i+3] for i in range(0, len(all_photos), 3)]
    photo_dict = {'photos': photo_list}
    return render(request, 'photo_app/index.html', context=photo_dict)

def upload_form(request):
    form = forms.UploadForm()

    if request.method == 'POST':
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("VALIDATION SUCCESS")
            print(form.cleaned_data['title'])
            print(form.cleaned_data['image'])
            form.save(commit=True)
            return redirect("/")
        else:
            print("Error - form invalid.")

    return render(request, 'photo_app/upload_image.html', {'form': form})

def show_image(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'photo_app/show_image.html', {'photo': photo})

def edit_image(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    form = forms.EditForm(request.POST or None, instance = photo)

    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(f"/{photo_id}")
    
    return render(request, 'photo_app/edit_image.html', {'form': form, 'photo': photo})

def delete_image(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    if request.method == 'POST':
        photo.delete()
        return HttpResponseRedirect('/')
    
    return render(request, 'photo_app/delete_image.html', {'photo': photo})