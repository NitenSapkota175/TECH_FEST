# Generated by Django 3.2.10 on 2022-04-29 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['updated', 'created']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commentdislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commentlikes',
        ),
    ]
