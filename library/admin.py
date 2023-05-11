from django.contrib import admin
from .models import UserProfile,Book,Book_Issue,BookInstance

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Book_Issue)
admin.site.register(BookInstance)
