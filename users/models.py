from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from datetime import date

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField('CPF', max_length=11, help_text='Informe o CPF', unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    name = models.CharField('nome', max_length=100, help_text='Informe o nome')
    social_name = models.CharField('nome social', max_length=100, blank=True, help_text='Informe o nome social (opcional)')
    birth_date = models.DateField('Data de nascimento', help_text='Informe a data de nascimento')
    is_staff = models.BooleanField(default=False)

    STATE_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
        ('DF', 'Distrito Federal')
    )
    state = models.CharField(
        max_length=2, choices=STATE_CHOICES,
        help_text='Selecione um Estado')
    city = models.CharField(max_length=100, help_text='Indique uma Cidade')

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['name', 'social_name', 'birth_date', 'state', 'city']

    objects = CustomUserManager()

    @property
    def age(self):
        return int((date.today() - self.birth_date).days / 365.25)

    def __str__(self):
        return self.name if self.social_name == '' else self.social_name 