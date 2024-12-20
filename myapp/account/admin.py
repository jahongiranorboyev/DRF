from django.contrib import admin
from myapp.account.models import Account
from rest_framework.authtoken.admin import TokenAdmin # Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('username', 'date_joined')
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')

TokenAdmin.raw_id_fields = ['user']