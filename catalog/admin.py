from django.contrib import admin
from .models import Author,Genre,Language,Book,BookInstance
# Register your models here.

admin.site.register([Book,Author,Language,BookInstance,Genre])
