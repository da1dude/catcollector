from django.shortcuts import render

from .models import Cat

#used to build initial view
# cats = [
#     {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#     {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
#     {'name': 'AngryCat', 'breed': 'calico', 'description': 'gentle and loving', 'age': 4},
# ]

# Create your views here.
def home(request):
# Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
# Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

def cats_index(request):
    #collect our objects from the db
    cats = Cat.objects.all()

    # for cat in cats:
    #     print(cat)
    # We pass data to a template very much like we did in Express!
    return render(request, 'cats/index.html', {
        'cats': cats
    })

#detail view - shows 1 cat at '/cats/:id'
def cats_detail(request, cat_id):
    #find one cat wiht its id
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', { 'cat': cat })