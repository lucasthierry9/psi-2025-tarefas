from django.db import models

class Tarefa(models.Model):
    em_andamento = "Em andamento"
    concluida = "Concluída"
    pendente = "Pendente"

    status = [
        (em_andamento, "Em andamento"), (concluida, "Concluída"), (pendente, "Pendente")
    ]
    nome = models.CharField("Nome", max_length = 100)
    status = models.CharField("Status", choices = status, default=pendente)
    prazo = models.DateField("Prazo")

    def __str__(self):
        return self.nome