from django.db import models
from django.contrib import admin
from django.utils import timezone, html

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("загаловок", max_length=128)
    text = models.TextField("описание")
    author = models.CharField("автор", max_length=64)
    date = models.DateField("дата", auto_now_add = True )
    price = models.FloatField("цена")
    auction = models.BooleanField("торг", default=False)

    @admin.display(description="Дата создания")
    def handl_date(self):
        if self.date.date() == timezone.now().date():
            return html.format_html(
                '<span style="color: green; font-weight: bold;">Сегодня</span>'
            )
        return self.date.strftime("%d.%m.%Y")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"


