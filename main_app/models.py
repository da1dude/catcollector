from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    # this is the get_absolute_url method, it redirects to the detail page where approprite
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

#The model for feedins - this is 1:M relationship with cats
    # one cat can have many feedings
class Feeding(models.Model):
    #first position in the feild (feeding date overides the date name)
    date = models.DateField('feeding date')
        # meals are a charfield with a max_length of one, because we're only going to save the
        # first initial of each meal
        # B-reakfast
        # L-unch
        # D-inner
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        # this is what will create the drop down menu
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )

    # Create a cat_id FK / creates the one to many relationship where cat has many feedings
    # models.ForeignKey needs two args, the model, and what to do if the parent model is deleted
    # casscade says that if the cat is deleted then delete all the feedings as well.
    # in the db, the column in the feedings table for the FK will be called cat_id
    # because django by default appends _id to the name of the model
    # DO not confuse this with mongoDB and their ._id not the same.
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        # get_xxx_display alows ya to select any value to display by replacing xxx
        return f"{self.get_meal_display()} on {self.date} for {self.cat}"