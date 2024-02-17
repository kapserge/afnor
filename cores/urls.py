from django.urls import include, path
from . import views 

app_name ='cores'

v1_urlpatterns = [
    path('Obf/', views.Obfuscated_list, name='Obfuscated_list'),
    path('Obf/<int:pk>/', views.Obfuscated_detail, name='Obfuscated_detail'),
    path('Obf/create/', views.Obfuscated_create, name='Obfuscated_create'),
    path('Obf/<int:pk>/update/', views.Obfuscated_update, name='Obfuscated_update'),
    path('Obf/<int:pk>/delete/', views.Obfuscated_delete, name='Obfuscated_delete'),
]

v2_urlpatterns = [
    path('obfuscateds/', views.obfuscateds, name='obfuscateds'),
    path('obfuscateds/<int:pk>/', views.obfuscated, name='obfuscated'),
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns)),
    path('api/v2/', include(v2_urlpatterns)),
    
]