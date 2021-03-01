from django.urls import path

from . import views

app_name = "crudapp"

urlpatterns = [
    path('',views.IndexView.as_view(), name='contact_index'),
    path('<int:pk>/',views.ContactDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete, name='delete'),
]
