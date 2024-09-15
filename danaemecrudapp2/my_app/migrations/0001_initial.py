# Generated by Django 5.1.1 on 2024-09-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ingredients', models.TextField(max_length=500)),
                ('instructions', models.TextField(max_length=1000)),
                ('prep_time', models.IntegerField(help_text='Preparation time in minutes')),
                ('cook_time', models.IntegerField(help_text='Cooking time in minutes')),
            ],
        ),
    ]
