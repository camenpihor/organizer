from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('<str:core_object_type>/', include([
        path('', views.home, name='home'),
        path('archive', views.archive, name='archive'),
        path('item/<int:object_id>', views.item, name='item'),
        path('stats', views.stats, name='stats'),
    ]))
]
