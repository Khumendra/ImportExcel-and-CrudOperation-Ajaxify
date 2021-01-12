from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.simple_upload),

    # path('', views.CrudView.as_view(), name='crud_ajax'),
    path('crud/', views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/', views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/', views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
]
