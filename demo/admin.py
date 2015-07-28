from django.contrib import admin
from .models import Book, BookSnippet


admin.site.register(Book)
admin.site.register(BookSnippet)
