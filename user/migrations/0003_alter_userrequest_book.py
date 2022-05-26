# Generated by Django 3.2 on 2022-05-22 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_bookitem'),
        ('user', '0002_userrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.bookitem'),
        ),
    ]
