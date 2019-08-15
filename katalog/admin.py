from django.contrib import admin
from katalog.models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name']    
    fields = [('first_name', 'last_name'), 'date_of_birth', 'date_of_death']

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    search_fields = ['genre__name', 'title', 'author__first_name', 'author__last_name']
    list_filter = ['genre__name']
    show_full_result_count = True
    inlines = [BooksInstanceInline]

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        ("Default", {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

#admin.site.register(Book)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)
