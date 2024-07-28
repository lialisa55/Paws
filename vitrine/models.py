from django.db import models

# Create your models here.

class Resgatador(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Animal(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]

    PORTE_CHOICES = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]

    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    idade_aproximada = models.IntegerField(null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    microchip = models.CharField(max_length=15, unique=True, null=True, blank=True)
    especie = models.CharField(max_length=50)
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES)
    raca = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    sobre_o_pet = models.TextField()
    adotado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos_animais/', null=True, blank=True)
    resgatador = models.ForeignKey(Resgatador, on_delete=models.CASCADE, related_name='animais')
    data_resgate = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.especie})"
