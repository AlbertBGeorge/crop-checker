# Generated by Django 2.0.5 on 2018-08-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='check_crop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('temp_start', models.IntegerField()),
                ('temp_end', models.IntegerField()),
                ('pH_start', models.IntegerField()),
                ('pH_end', models.IntegerField()),
                ('info', models.TextField()),
            ],
        ),
    ]
