from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('lego/', views.lego_index, name='index'),
  path('lego/<int:lego_id>/', views.lego_detail, name='detail'),
  path('lego/create/', views.LegoCreate.as_view(), name='lego_create'),
  path('lego/<int:pk>/update/', views.LegoUpdate.as_view(), name='lego_update'),
  path('lego/<int:pk>/delete/', views.LegoDelete.as_view(), name='lego_delete'),
  path('lego/<int:lego_id>/add_building/', views.add_building, name='add_building'),
  path('lego/<int:lego_id>/assoc_builder/<int:builder_id>/', views.assoc_builder, name='assoc_builder'),
  path('lego/<int:lego_id>/unassoc_builder/<int:builder_id>/', views.unassoc_builder, name='unassoc_builder'),
  path('builders/', views.BuilderList.as_view(), name='builders_index'),
  path('builders/<int:pk>/', views.BuilderDetail.as_view(), name='builders_detail'),
  path('builders/create/', views.BuilderCreate.as_view(), name='builders_create'),
  path('builders/<int:pk>/update/', views.BuilderUpdate.as_view(), name='builders_update'),
  path('builders/<int:pk>/delete/', views.BuilderDelete.as_view(), name='builders_delete'),
]
