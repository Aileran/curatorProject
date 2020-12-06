# Generated by Django 3.1.3 on 2020-12-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('artist', models.CharField(max_length=60)),
                ('label', models.CharField(max_length=60)),
                ('genre', models.CharField(max_length=60)),
                ('year', models.CharField(max_length=4)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=60)),
                ('publisher', models.CharField(max_length=60)),
                ('genre', models.CharField(max_length=60)),
                ('year', models.CharField(max_length=4)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('director', models.CharField(max_length=60)),
                ('studio', models.CharField(max_length=60)),
                ('genre', models.CharField(max_length=60)),
                ('year', models.CharField(max_length=4)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
    ]
