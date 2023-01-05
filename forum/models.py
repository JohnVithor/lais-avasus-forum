from django.db import models

from users.models import CustomUser
# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=120, help_text='Informe o nome da categoria')
    is_active = models.BooleanField('Ativo', default=True, help_text='Indica se a categoria está ativa')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class SubForum(models.Model):
    title = models.CharField('Título', max_length=120, help_text='Informe o título do subfórum')
    description = models.TextField('Descrição', help_text='Informe a descrição do subfórum')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_subforuns')
    students = models.ManyToManyField(CustomUser)

    is_active = models.BooleanField('Ativo', default=True, help_text='Indica se o subfórum está ativo')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    @property
    def sorted_topics(self):
        return self.topic_set.order_by('-created_at')
    
    @property
    def qtd_posts(self):
        qtd = 0
        for topic in self.topic_set.all():
            qtd += topic.topicresponse_set.all().count()
        return qtd

class Topic(models.Model):
    title = models.CharField('Título', max_length=120, help_text='Informe o título do tópico')
    content = models.TextField('Conteúdo', help_text='Informe o conteúdo do tópico')
    subforum = models.ForeignKey(SubForum, on_delete=models.CASCADE)

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_closed = models.BooleanField('Trancado', default=False, help_text='Indica se o tópico está trancado')

    is_active = models.BooleanField('Ativo', default=True, help_text='Indica se o tópico está ativo')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    def __str__(self) -> str:
        return "[Trancado] " + self.title if self.is_closed else self.title

    @property
    def sorted_responses(self):
        return self.topicresponse_set.order_by('-created_at')
    
    @property
    def qtd_responses(self):
        return self.topicresponse_set.all().count()
    
    @property
    def datetime_last_response(self):
        resps = self.topicresponse_set.order_by('created_at').all() 
        if (len(resps) > 0):
            return resps[0].created_at
        return self.updated_at

class TopicResponse(models.Model):
    content = models.TextField('Resposta', help_text='Informe a resposta ao tópico')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    
    def __str__(self) -> str:
        return self.content