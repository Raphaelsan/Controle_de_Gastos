# Generated by Django 4.1 on 2022-08-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas_2', '0005_alter_transacao_options_alter_transacao_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='dt_criacao',
            field=models.DateTimeField(max_length=50),
        ),
    ]