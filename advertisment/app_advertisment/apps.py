from django.apps import AppConfig
from django.contrib import admin
from django.utils import timezone, html


class AppAdvertismentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Объявления'

    @admin.display(description="Дата создания")
    def handl_date(self):
        if self.date.date() == timezone.now().date():
            return html.format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня</span>'
            )
        return self.date.strftime("%d.%m.%Y")
