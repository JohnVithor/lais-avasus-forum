from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=100, help_text='Informe o nome da categoria')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self) -> str:
        return self.name

