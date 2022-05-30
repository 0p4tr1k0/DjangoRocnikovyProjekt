from django.db import models
from django.core.validators import MinLengthValidator
def img_path(instance, filename):
    return "tanky/" + str(instance.attachmentid) + "/img/" + filename


class Tank(models.Model):
    # charfield je varchar, integer field je int
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
    TIER = [
        ('I', '1'),
        ('II', '2'),
        ('III', '3'),
        ('IV', '4'),
        ('V', '5'),
        ('VI', '6'),
        ('VII', '7'),
        ('VIII', '8'),
        ('IX', '9'),
        ('X', '10'),
    ]

    tankid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='Tank name',
                            help_text='Enter Tank name')
    types = models.CharField(max_length=50, choices=TYPES, blank=True, null=True, verbose_name='Type of tank')
    nations = models.CharField(max_length=50, choices=NATIONS, blank=True, null=True, verbose_name='Tank nation')
    tier = models.CharField(max_length=50, choices=TIER, blank=True, null=True, verbose_name='Level of tank')

    def __str__(self):
        return self.name


class Attachment(models.Model):
    attachmentid = models.AutoField(primary_key=True)
    tank = models.ForeignKey(Tank, models.DO_NOTHING, blank=True, null=True, verbose_name='idk')
    name = models.CharField(max_length=200, verbose_name='Tank info', blank=True, null=True,
                            help_text='Enter tank information')
    image = models.ImageField(upload_to=img_path, blank=True, null=True, verbose_name="Image")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
