# Generated by Django 4.2.16 on 2024-11-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOutfitShowroom', '0006_alter_outfit_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='foto',
            field=models.URLField(blank=True, null=True),
        ),
    ]
