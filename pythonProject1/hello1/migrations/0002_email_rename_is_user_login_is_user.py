# Generated by Django 4.0.3 on 2022-04-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=75)),
                ('Phone', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='login',
            old_name='is_User',
            new_name='is_user',
        ),
    ]
