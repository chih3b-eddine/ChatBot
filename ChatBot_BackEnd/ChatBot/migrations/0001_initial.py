# Generated by Django 2.2 on 2019-07-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=4)),
                ('message', models.CharField(max_length=500)),
                ('previous_message_id', models.IntegerField(null=True)),
            ],
        ),
    ]