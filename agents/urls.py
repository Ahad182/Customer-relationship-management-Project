from django import views
from django.urls import include, path
from  .import views

urlpatterns = [
   
    path('', views.AgentListView.as_view() , name = 'agent_list'),
    path('agent_create/', views.AgentCreateView.as_view() , name = 'agent_create'),
    path('agent_detail/<int:pk>/', views.AgentDetailView.as_view() , name = 'agent_detail'),
    path('agent_update/<int:pk>/', views.AgentUpdateView.as_view() , name = 'agent_update'),
    path('agent_delete/<int:pk>/', views.AgentDeleteView.as_view() , name = 'agent_delete'),

]
