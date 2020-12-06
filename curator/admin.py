from django.contrib import admin
#from .models import UserRegistrationForm
# Register your models here.
#admin.site.register(UserRegistrationForm)
from .models import *

admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Album)

