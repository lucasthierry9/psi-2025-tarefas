from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    desenvolvedor = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)


    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    data = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="imagens/")

    def __str__(self):
        return self.titulo