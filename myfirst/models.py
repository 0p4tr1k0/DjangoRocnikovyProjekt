from django.db import models
from django.core.validators import MinLengthValidator

class Types(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Tank type', help_text='Enter Tank type')
    abbr = models.CharField(max_length=3, unique=True, validators=[MinLengthValidator(2)], verbose_name='Tank type Abbreviation',
                            help_text='Enter Abbreviation')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Tank(models.Model):
    #charfield je varchar, integer field je int
    HT = 'Heavy'
    MT = 'Medium'
    LT = 'Light'
    TD = 'Destroyer'
    ART = 'Arty'

    TYPES = [
        (HT, 'Heavy'),
        (MT, 'Medium'),
        (LT, 'Light'),
        (TD, 'Destroyer'),
        (ART, 'Arty')
    ]
    NATIONS = [
        ('U.S.A.', 'U.S.A.'),
        ('GERMANY', 'GERMANY'),
        ('U.K.', 'U.K.'),
        ('U.S.S.R.', 'U.S.S.R.'),
        ('FRANCE', 'FRANCE'),
        ('JAPAN', 'JAPAN'),
        ('CHINA', 'CHINA'),
        ('CZECHOSLOVAKIA', 'CZECHOSLOVAKIA'),
        ('SWEDEN', 'SWEDEN'),
        ('POLAND', 'POLAND'),
        ('ITALY', 'ITALY'),
    ]
    DEPLOYMENT = [
        ('FRONTLINE', 'FRONTLINE'),
        ('REAR', 'REAR'),
    ]

    name = models.CharField(max_length=50, unique=True, verbose_name='Tank name', help_text='Enter Tank name')
    types = models.CharField(max_length=50, choices=TYPES, verbose_name='Type of tank')
    tank_class = models.CharField(max_length=50, choices=NATIONS, verbose_name='Choose nation')
    deploy = models.CharField(max_length=50, choices=DEPLOYMENT, verbose_name='Choose deployment')

    class Meta:
        ordering = ['name']

    def __str__(self):
            return self.name




