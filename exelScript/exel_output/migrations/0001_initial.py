# Generated by Django 4.0.4 on 2022-05-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_exel_file', models.FileField(upload_to='media/exel/first')),
                ('second_exel_file', models.FileField(upload_to='media/exel/second')),
            ],
        ),
    ]
