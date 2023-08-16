from django.contrib import admin
from .models import reader, book

admin.site.register(reader)
admin.site.register(book)