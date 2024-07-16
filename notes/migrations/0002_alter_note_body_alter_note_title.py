# Generated by Django 4.1.5 on 2024-07-16 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]
