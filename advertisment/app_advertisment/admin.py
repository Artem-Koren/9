from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'author', 'data', 'handle_date']
    list_filter = ['author','date', 'title']
    actions = ['delete_description', 'make_auction_as_true']

    fieldsets = (
            ('Общее', {
                'fields': ('title', 'text')
            }),
            ("Финансы", {
                "fields": ("price", "auction"),
                "classes": ['collapse']
            })
            ("Дата", {
                "fields": ('date')
            })
    )

    @admin.action(description="Удалить выбраное")
    def delete_description(self, request, queryset):
        queryset.update(text ='')

    @admin.action(description="Включить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction =True)

admin.site.register(Advertisement,AdvertisementAdmin)



# Register your models here.
