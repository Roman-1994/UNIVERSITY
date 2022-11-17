# Generated by Django 4.1.2 on 2022-11-17 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('univer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertutorstudent',
            name='gender',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genders', to='univer.gender', verbose_name='Пол'),
        ),
    ]