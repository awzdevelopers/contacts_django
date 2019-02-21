from django.contrib import admin
from app1.models import ContactsTable,PhonesTable
# Register your models here.

admin.site.register(ContactsTable)
admin.site.register(PhonesTable)
