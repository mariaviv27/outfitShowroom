# Generated by Django 5.1.2 on 2024-11-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOutfitShowroom', '0003_outfit_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='\\static\\layout\\images\\outfits'),
        ),
    ]
