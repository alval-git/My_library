from django.contrib import admin
from p_library.models import book, author, PublishHouse, Friend,WhoAndWhatTook


# Register your models here.
@admin.register(book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')
@admin.register(author)
class AuthorAdmin(admin.ModelAdmin):
	pass
@admin.register(PublishHouse)
class PublishAdmin(admin.ModelAdmin):
    pass
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass
@admin.register(WhoAndWhatTook)
class FriendBooksAdmin(admin.ModelAdmin):
    pass