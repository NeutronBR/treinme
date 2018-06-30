# Generated by Django 2.0.6 on 2018-06-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0016_inscricao_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='comentario',
            field=models.TextField(blank=True, null=True, verbose_name='Comentário do curso'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='nota_questionario',
            field=models.FloatField(null=True, verbose_name='Nota'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='qtd_videos',
            field=models.FloatField(null=True, verbose_name='Vídeos Assistidos'),
        ),
    ]