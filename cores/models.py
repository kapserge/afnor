from django.db import models


class Obfuscated(models.Model):
    
    NUMDOS = models.CharField( max_length=255)
    NUMDOSVERLING = models.CharField( max_length=255)
    ANCART = models.CharField( max_length=255)
    FILIERE = models.CharField( max_length=255)
    ETAPE = models.CharField( max_length=255)
    VERLING = models.CharField( max_length=255)
    FORMAT = models.CharField( max_length=255)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Obfuscated'
        verbose_name_plural = 'Obfuscateds'

    def __str__(self):
        return f'{self.NUMDOS}'

    def to_dict(self):
        return {
            'id': self.id,
            'NUMDOS': self.NUMDOS,
            'NUMDOSVERLING': self.NUMDOSVERLING,
            'ANCART': self.ANCART,
            'FILIERE': self.FILIERE,
            'ETAPE': self.ETAPE,
            'VERLING': self.VERLING,
            'FORMAT': self.FORMAT,
        }