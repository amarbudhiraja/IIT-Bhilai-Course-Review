# Generated by Django 4.1.7 on 2023-04-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('informative', models.IntegerField()),
                ('need_to_go_to_class', models.IntegerField()),
                ('difficulty', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('professor', models.ManyToManyField(blank=True, null=True, to='reviews.professor')),
            ],
        ),
    ]