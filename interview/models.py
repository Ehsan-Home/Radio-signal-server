from django.db import models


class RadioModel(models.Model):
    type = models.CharField(max_length=300)
    dispersion = models.DecimalField(decimal_places=3, max_digits=8)
    right_ascension = models.DecimalField(decimal_places=3, max_digits=6)
    declination = models.DecimalField(decimal_places=3, max_digits=5)

    def __str__(self):
        return self.type
