from django import forms

from .models import Obfuscated


class ObfuscatedForm(forms.ModelForm):

    class Meta:
        model = Obfuscated
        fields = ('id','NUMDOS','NUMDOSVERLING','ANCART','FILIERE','ETAPE','VERLING','FORMAT')