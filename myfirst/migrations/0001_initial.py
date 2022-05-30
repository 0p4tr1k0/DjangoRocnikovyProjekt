# Generated by Django 4.0.4 on 2022-05-30 18:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('tankid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Enter Tank name', max_length=50, null=True, unique=True, verbose_name='Tank name')),
                ('types', models.CharField(blank=True, choices=[('Heavy', 'Heavy'), ('Medium', 'Medium'), ('Light', 'Light'), ('Destroyer', 'Destroyer'), ('Arty', 'Arty')], max_length=50, null=True, verbose_name='Type of tank')),
                ('nations', models.CharField(blank=True, choices=[('U.S.A.', 'U.S.A.'), ('GERMANY', 'GERMANY'), ('U.K.', 'U.K.'), ('U.S.S.R.', 'U.S.S.R.'), ('FRANCE', 'FRANCE'), ('JAPAN', 'JAPAN'), ('CHINA', 'CHINA'), ('CZECHOSLOVAKIA', 'CZECHOSLOVAKIA'), ('SWEDEN', 'SWEDEN'), ('POLAND', 'POLAND'), ('ITALY', 'ITALY')], max_length=50, null=True, verbose_name='Tank nation')),
                ('tier', models.CharField(blank=True, choices=[('I', '1'), ('II', '2'), ('III', '3'), ('IV', '4'), ('V', '5'), ('VI', '6'), ('VII', '7'), ('VIII', '8'), ('IX', '9'), ('X', '10')], max_length=50, null=True, verbose_name='Level of tank')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('attachmentid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Enter tank information', max_length=200, null=True, verbose_name='Tank info')),
                ('abbr', models.CharField(help_text='Enter Abbreviation', max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Tank type Abbreviation')),
                ('tank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myfirst.tank', verbose_name='idk')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
