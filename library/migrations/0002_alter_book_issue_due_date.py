# Generated by Django 4.2.1 on 2023-05-07 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 22, 35, 9, 433443), help_text='Date the book is due to'),
        ),
    ]
