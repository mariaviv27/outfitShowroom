# Generated by Django 5.1.2 on 2024-10-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOutfitShowroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outfit',
            name='nombre',
            field=models.CharField(default='hi', max_length=50),
            preserve_default=False,
        ),
    ]