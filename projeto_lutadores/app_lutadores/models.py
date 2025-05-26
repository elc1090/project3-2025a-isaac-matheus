from django.db import models


class Lutador(models.Model):
    """
    Representa um lutador.
    Campos:
      - id_lutador: auto incremento, primary key
      - nome: nome do lutador
      - idade: idade do lutador
      - profissao: profissão do lutador
      - historia: texto com a história do lutador
    """
    id_lutador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField(default=18)  # ou null=True, blank=True
    profissao = models.CharField(max_length=255, default='Desconhecida')
    historia = models.TextField(default='Sem história cadastrada.')

    class Meta:
        db_table = 'lutador'

    def __str__(self):
        return self.nome


class Golpe(models.Model):
    """
    Representa um golpe de um lutador.
    Campos:
      - id_golpe: auto incremento, primary key
      - lutador: FK para Lutador
      - nome: nome do golpe
      - tipo: membro do corpo (cabeça, braços, pernas, especial)
      - descricao: descrição do golpe
      - forca: intensidade, velocidade (leve, médio, forte)
    """
    id_golpe = models.AutoField(primary_key=True)
    lutador = models.ForeignKey(
        Lutador,
        on_delete=models.CASCADE,
        db_column='id_lutador',
        related_name='golpes'
    )
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    forca = models.CharField(max_length=30)

    class Meta:
        db_table = 'golpe'

    def __str__(self):
        return f"{self.nome} ({self.lutador.nome})"


class Amizade(models.Model):
    """
    Relação de amizade entre lutadores (muitos-para-muitos não simétrico).
    """
    lutador = models.ForeignKey(
        Lutador,
        on_delete=models.CASCADE,
        db_column='id_lutador',
        related_name='amizades'
    )
    amigo = models.ForeignKey(
        Lutador,
        on_delete=models.CASCADE,
        db_column='id_amigo',
        related_name='amigos_de'
    )

    class Meta:
        db_table = 'amizades'
        unique_together = (('lutador', 'amigo'),)

    def __str__(self):
        return f"{self.lutador.nome} é amigo de {self.amigo.nome}"


class Inimizade(models.Model):
    """
    Relação de inimizade entre lutadores.
    """
    lutador = models.ForeignKey(
        Lutador,
        on_delete=models.CASCADE,
        db_column='id_lutador',
        related_name='inimizades'
    )
    inimigo = models.ForeignKey(
        Lutador,
        on_delete=models.CASCADE,
        db_column='id_inimigo',
        related_name='inimigos_de'
    )

    class Meta:
        db_table = 'inimizades'
        unique_together = (('lutador', 'inimigo'),)

    def __str__(self):
        return f"{self.lutador.nome} é inimigo de {self.inimigo.nome}"
