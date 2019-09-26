from django.contrib import admin

from catalog.models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

#admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

#admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Language)

# Register your models here.
