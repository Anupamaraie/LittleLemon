from django.contrib import admin
from .models import Book, AuthorDet

# Register your models here.
admin.site.register(Book)
admin.site.register(AuthorDet)