
from django.contrib import admin

# Register your models here.
from .models import form

class formAdmin(admin.ModelAdmin):
    list_display = ('id','gname','bname','date')
    list_display_links =('id','gname','bname')
admin.site.register(form,formAdmin)
