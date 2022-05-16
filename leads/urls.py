from django import views
from django.urls import include, path
from  .import views

urlpatterns = [
   
    path('', views.LeadListView.as_view() , name = 'lead_list'),
    path('lead_create/', views.LeadCreateView.as_view() , name = 'lead_create'),
    path('lead_detail/<int:pk>/', views.LeadDetailView.as_view() , name = 'lead_detail'),
    path('lead_update/<int:pk>/', views.LeadUpdateView.as_view() , name = 'lead_update'),
    path('lead_delete/<int:pk>/', views.LeadsDeleteView.as_view() , name = 'lead_delete'),
    path('category/', views.CategoryListView.as_view() , name = 'category_list'),
    path('category/detail/<int:pk>/', views.CategoryDetailView.as_view() , name = 'category_detail'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view() , name = 'category_update'),

]
