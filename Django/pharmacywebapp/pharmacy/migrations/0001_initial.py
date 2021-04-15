# Generated by Django 3.2 on 2021-04-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('batch', models.CharField(max_length=20)),
                ('manufacture', models.CharField(max_length=122)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AddUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('age', models.IntegerField(max_length=2)),
                ('sex', models.CharField(max_length=10)),
                ('bloodgroup', models.CharField(max_length=3)),
                ('email', models.CharField(max_length=122)),
                ('phonenumber', models.IntegerField(max_length=12)),
                ('address', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
