from django.core.management.base import BaseCommand
from django.utils import timezone
import csv
from cores.models import Obfuscated
import logging


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Affiche heure actuelle'

    def handle(self, *args, **kwargs):
       with open('csv/obfuscated.csv') as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            next(reader)  # Advance past the header

            Obfuscated.objects.all().delete()

            for row in reader:
                
                if row:
                    
                    Obf = Obfuscated(NUMDOS=row[0],
                                NUMDOSVERLING=row[1],ANCART=row[2],
                                FILIERE=row[3],ETAPE=row[4],
                                VERLING=row[5],FORMAT=row[6]
                                )
                    print(Obf)
                    Obf.save()
                    