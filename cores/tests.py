import json

from django.test import TestCase
from .models import Obfuscated

class ObfuscatedTest(TestCase):

    def setUp(self):
        self.dataobf= {
            
            "NUMDOS": "DD237051",
            "NUMDOSVERLING": "DD237051",
            "ANCART": "LNEN50289-1-3",
            "FILIERE": "ETR",
            "ETAPE": "7990.62",
            "VERLING": "E",
            "FORMAT": "PDFC"
            }
        
######### CREATE OBFUSCATED 
    def test_Obfuscated_create(self):
        response = self.client.post(
            '/api/v2/obfuscateds/',
            data=self.dataobf,
            content_type='application/json'
        )
        resultat = json.loads(response.content)
        esper = {
            "data": {
                "id": 1,
                **self.dataobf
            }
        }
        self.assertEqual(esper, resultat)


######### ALL LIST OBFUSCATED 
    def test_Obfuscated_list(self):
        Obfuscated.objects.create(**self.dataobf)

        response = self.client.get(
            '/api/v2/obfuscateds/',
            content_type='application/json'
        )
        resultat = json.loads(response.content)
        esper = {
            "data": [
                {
                    "id": 1,
                    **self.dataobf
                }
            ]
        }
        self.assertEqual(esper, resultat)



#########  UPDATE OBFUSCATED 

    def test_obfuscated_update(self):
        Obfuscated.objects.create(**self.dataobf)

        data = {
            "NUMDOS": "DD237051",
        }

        response = self.client.post(
            '/api/v2/obfuscateds/1/',
            data=data,
            content_type='application/json'
        )
        resultat = json.loads(response.content)
        esper = {
            "data":
            {
                "id": 1,
                "NUMDOS": "DD237051",
                "NUMDOSVERLING": "DD237051",
                "ANCART": "LNEN50289-1-3",
                "FILIERE": "ETR",
                "ETAPE": "7990.62",
                "VERLING": "E",
                "FORMAT": "PDFC"
            }
        }
        self.assertEqual(esper, resultat)

########### DELETE OBFUSCATED
        
    def test_obfuscated_delete(self):
        Obfuscated.objects.create(**self.dataobf)

        response = self.client.delete(
            '/api/v2/obfuscateds/1/',
            content_type='application/json'
        )
        resultat = json.loads(response.content)
        esper = {"data": "element delete avec succes"}

        self.assertEqual(esper, resultat)
######### LIST DETAIL OBFUSCATED 
        
    def test_obfuscated_detail(self):
            Obfuscated.objects.create(**self.dataobf)

            response = self.client.get(
                '/api/v2/obfuscateds/1/',
                content_type='application/json'
            )
            resultat = json.loads(response.content)
            esper = {
                "data": {
                    "id": 1,
                    **self.dataobf
                }
            }
            self.assertEqual(esper, resultat)
