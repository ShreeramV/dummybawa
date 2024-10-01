from django.shortcuts import render

# Home view
def home(request):
    return render(request, 'myApp/index.html')  # Update with your actual home template name

# Collections view
def collection(request):
    return render(request, 'myApp/collection.html')  # This is your collections page

# Contact view
def contact(request):
    return render(request, 'myApp/contact.html')  # Update with your actual contact template name

