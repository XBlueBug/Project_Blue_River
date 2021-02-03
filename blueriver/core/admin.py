from django.contrib import admin
from core.models import Contact, User_Registration

# Register your models here.
admin.site.register(Contact)
admin.site.register(User_Registration)


class Contact_user(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'address', 'comment')

# class User_register_model(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'address', 'phone', 'password')


