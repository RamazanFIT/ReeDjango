# Generated by Django 5.0.3 on 2024-03-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_reestr'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoiskPravoobladateley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('file', models.FileField(upload_to='catalogs/')),
            ],
        ),
    ]
