from django.contrib import admin
from pharmacy.models import AddUser
from pharmacy.models import AddMedicine

# Register your models here.
admin.site.register(AddUser)
admin.site.register(AddMedicine)