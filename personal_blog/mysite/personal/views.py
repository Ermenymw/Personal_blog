from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html', { 'content': ['If you would like to contact me, please email me','ermenyu@gmail.com']})

def gallery(request):
    photos = get_object_or_404(Gallery)
    return render(request, 'personal/gallery.html', { 'photos': photos })
