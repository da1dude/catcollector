from django.shortcuts import render

cats = [
    {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
    {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
    {'name': 'AngryCat', 'breed': 'calico', 'description': 'gentle and loving', 'age': 4},
]

# Create your views here.
def home(request):
# Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
# Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

def cats_index(request):
    # We pass data to a template very much like we did in Express!
    return render(request, 'cats/index.html', {
        'cats': cats
    })