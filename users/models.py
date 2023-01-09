from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from datetime import date

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    cpf = models.CharField('CPF', max_length=11, help_text='Informe o CPF', unique=True)
    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    name = models.CharField('Nome', max_length=100, help_text='Informe o nome')
    social_name = models.CharField('Nome social', max_length=100, blank=True, help_text='Informe o nome social (opcional)')
    birth_date = models.DateField('Data de nascimento', help_text='Informe a data de nascimento dd/mm/aaaa')
    is_professor = models.BooleanField('Professor', default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

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
    state = models.CharField("Estado",
        max_length=2, choices=STATE_CHOICES,
        help_text='Selecione um Estado')
    city = models.CharField("Cidade", max_length=100, help_text='Indique uma Cidade')

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['name', 'social_name', 'birth_date', 'state', 'city']

    objects = CustomUserManager()

    @property
    def age(self):
        return int((date.today() - self.birth_date).days / 365.25)

    def __str__(self):
        return self.name if self.social_name == '' else self.social_name 
    
    @property
    def call_name(self):
        return self.name if self.social_name == '' else self.social_name 
    
    @property
    def qtd_subforums(self):
        return self.created_subforuns.all().count() + self.subforum_set.all().count()