# Generated by Django 2.2 on 2019-04-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=200)),
                ('to_email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('file', models.FileField(null=True, upload_to='files/')),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='sent', max_length=200)),
                ('important', models.BooleanField(default=False, max_length=10)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
