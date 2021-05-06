from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title news')
    anons = models.CharField(max_length=250, verbose_name='Anons site')
    full_text = models.TextField(verbose_name='Article')
    date = models.DateTimeField(verbose_name='Time')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'
    

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"