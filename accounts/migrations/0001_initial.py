# Generated by Django 2.2.2 on 2019-07-01 22:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='ФИО')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Телефон')),
                ('industry', models.CharField(blank=True, choices=[('Электрик', 'Электрик'), ('Сантехник', 'Сантехник'), ('Слесарь', 'Слесарь'), ('Охранник', 'Охранник')], max_length=255, null=True, verbose_name='Тип деятельности')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
