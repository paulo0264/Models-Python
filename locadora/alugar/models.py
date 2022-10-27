from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length = 150)
    email = models.EmailField()
    endereco = models.CharField(max_length = 150)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length = 150)
    ano_lancamento = models.DateField()
    valor_locacao = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo

class Locacao(models.Model):
    valor = models.FloatField()
    data_entrega = models.DateField()
    data_locacao = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    filme = models.ManyToManyField(Filme)

    def __str__(self):
        return self.data_locacao
