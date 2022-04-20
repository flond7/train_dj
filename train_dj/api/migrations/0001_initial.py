# Generated by Django 4.0.4 on 2022-04-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default='')),
                ('answerOne', models.TextField(default='')),
                ('answerTwo', models.TextField(default='')),
                ('answerThree', models.TextField(default='')),
                ('correct', models.TextField(default='')),
                ('id_path', models.IntegerField()),
                ('id_video', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correct', models.BooleanField()),
                ('id_question', models.IntegerField()),
                ('id_user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('surname', models.CharField(blank=True, default='', max_length=50)),
                ('mail', models.EmailField(max_length=150)),
                ('pw', models.CharField(max_length=50)),
            ],
        ),
    ]
