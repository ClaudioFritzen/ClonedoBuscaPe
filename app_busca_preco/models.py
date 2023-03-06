from django.db import models

# Create your models here.
class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=300)
    preco = models.DecimalField(decimal_places=2, max_digits=12)
    site = models.TextField(error_messages=255)
    data_cotacao = models.DateField()
    link_imagem = models.TextField(max_length=500, default= 'https://via.placeholder.com/150')


    def __str__(self):
        return self.nome
    
    