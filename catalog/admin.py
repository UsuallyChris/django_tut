from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth')

admin.site.register(Author, AuthorAdmin)