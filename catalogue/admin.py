from django.contrib import admin
from catalogue.models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname")
    search_fields = ("firstname", "lastname")


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from catalogue.models import UserMeta

# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserMetaInline(admin.StackedInline):
    model = UserMeta
    can_delete = False
    verbose_name_plural = "user_meta"

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserMetaInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
