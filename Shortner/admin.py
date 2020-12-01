from django.contrib import admin
from .models import Input_URL,User
# Register your models here.



@admin.register(Input_URL)
class Admin_Url(admin.ModelAdmin):
    list_display = ['UserID', 'ip_addresss','input_url', 'shorten_url', 'CreationDate', 'ExpirationDate']


@admin.register(User)
class Admin_User(admin.ModelAdmin):
    list_display = ['Name', 'Email']

