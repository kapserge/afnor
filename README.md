# Django API without DRF

This is a API project made with Django, Migrate CSV in SQLlite and without Django REST framework.

## How to run project?
* Clone this repository.
* open folder afnor
* Built docker compose
* Migrate CSV in SQLlite
* Run project
* Run unit test

```
git clone https://github.com/kapserge/afnor.git
cd afnor
docker-compose up --build   
docker-compose run web python manage.py csv_obfuscated_db
docker-compose up
docker-compose run web python manage.py test

```
## endpoints
```
/api/v1/Obf/                       cores.views.Obfuscated_list     cores:Obfuscated_list
/api/v1/Obf/<int:pk>/              cores.views.Obfuscated_detail   cores:Obfuscated_detail
/api/v1/Obf/<int:pk>/delete/       cores.views.Obfuscated_delete   cores:Obfuscated_delete
/api/v1/Obf/<int:pk>/update/       cores.views.Obfuscated_update   cores:Obfuscated_update
/api/v1/Obf/create/                cores.views.Obfuscated_create   cores:Obfuscated_create
/api/v2/obfuscateds/               cores.views.obfuscateds         cores:obfuscateds
/api/v2/obfuscateds/<int:pk>/      cores.views.obfuscateds         cores:obfuscated
```
### List data Obfuscated

```
http http://localhost:8000/api/v2/obfuscateds/
```
```
http http://localhost:8000/api/v1/Obf/
```
## TDD

https://github.com/kapserge/afnor/blob/main/cores/tests.py
