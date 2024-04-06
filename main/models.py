from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    user = models.CharField(max_length=250, blank=True)
    title = models.CharField("Описание", max_length=20)
    anons = models.CharField("Анонс", max_length=60)
    full_text = models.TextField("Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

