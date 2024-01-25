from django.contrib import admin

from .models import Service, Saloon, Master, Sign, Client, Administrator


class SaloonInline(admin.TabularInline):
    model = Saloon


@admin.register(Administrator)
class Administrator(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'display_saloon', 'orders',)
    inlines = [SaloonInline]


@admin.register(Service)
class Administrator(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', )
    search_fields = ('name', )
    ordering = ('price', )


admin.site.register(Saloon)
admin.site.register(Master)
admin.site.register(Sign)
admin.site.register(Client)
