# Generated by Django 5.0.7 on 2024-07-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_animais/'),
        ),
    ]