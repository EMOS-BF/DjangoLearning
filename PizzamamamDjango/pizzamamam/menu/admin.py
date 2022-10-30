from django.contrib import admin

# Register your models here.
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ["nom", "ingredients", "prix", "vegetarien"]
    search_fields = ["nom"]
# Register your models here.
admin.site.register(Pizza, PizzaAdmin)