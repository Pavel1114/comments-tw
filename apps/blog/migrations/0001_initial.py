# Generated by Django 3.2.3 on 2021-05-30 09:39

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=500, verbose_name='название')),
                ('text', models.TextField(verbose_name='текст')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
                'ordering': ('-created',),
            },
        ),
    ]