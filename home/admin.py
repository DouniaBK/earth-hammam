from django.contrib import admin
from .models import Testimonial

# Register your models here.


@admin.register(Testimonial)
class TestimonyAdmin(admin.ModelAdmin):

    list_display = ('name', 'status')
    list_filter = ('status', 'name')
    search_fields = ('name', 'status')
