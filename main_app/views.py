from django.shortcuts import render
# importing our class based views also known as CBV's
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Cat
# Import the FeedingForm
from .forms import FeedingForm

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
    cat = Cat.objects.get(id=cat_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        # include the cat and feeding_form in the context
        'cat': cat, 'feeding_form': feeding_form
    })

# inherit from the CBV - CreateView, to make our cats create view
class CatCreate(CreateView):
    # tell the createview to use the Cat model for all its functionality
    model = Cat
    # this view creates a form, so we need to identify which fields to use
    fields = '__all__'
    # we can add other options inside this view
    # success_url = '/cats/{cat_id}'

# Update View - extends the UpdateView class
class CatUpdate(UpdateView):
    model = Cat
    # let's make it so you can't rename a cat
    # we could simply say fields = '__all__', or we can customize like this:
    fields = ['breed', 'description', 'age']

# Delete View - extends DeleteView
class CatDelete(DeleteView):
    model = Cat

    success_url = '/cats'

#Feeding and relationship view functions
#this is to add a feeding to a cat
def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    #django give us a built in function for that
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)