from django.shortcuts import render
from .models import photos

# Home view
def home(request):
    return render(request, 'myApp/index.html')  # Update with your actual home template name

# Collections view
def collection(request):
    pic = photos.objects.all()
    return render(request, 'myApp/collection.html',{"picture":pic})  # This is your collections page

# Contact view
def contact(request):
    return render(request, 'myApp/contact.html')  # Update with your actual contact template name

