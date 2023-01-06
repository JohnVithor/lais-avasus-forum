from django.core.management.base import BaseCommand, CommandError
from forum.models import Category
import json

class Command(BaseCommand):
    help = 'Insere algumas categorias básicas'

    def handle(self, *args, **options):
        f = open('data/eixos_tematicos.json')
        categories = json.load(f)
        for cat_info in categories:
            cat = Category()
            cat.name = cat_info["nome"]
            cat.save()
        self.stdout.write(self.style.SUCCESS('Categorias adicionadas com sucesso'))
            