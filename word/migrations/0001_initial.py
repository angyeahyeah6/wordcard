<<<<<<< HEAD
# Generated by Django 2.1.4 on 2019-01-12 07:36
=======
# Generated by Django 2.0.9 on 2019-01-12 07:34
>>>>>>> 267d1423b31615286347ea78150c95188c31a144

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phraseDef', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
<<<<<<< HEAD
                ('catDef', models.CharField(blank=True, max_length=64)),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='word.Word')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('cat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='word.Category')),
>>>>>>> 267d1423b31615286347ea78150c95188c31a144
            ],
        ),
    ]
