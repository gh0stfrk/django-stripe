from django.urls import path
from .views import StoriesView, ProjectsView
from . import views 

urlpatterns = [
   path('', views.home, name='home'),
   path('config/', views.stripe_config, name="config"),
   path('checkout-session/', views.create_checkout_session),
   path('cancelled/', views.cancel, name='cancel'),
   path('stories/', StoriesView.as_view(), name='stories'),
   path('projects/', ProjectsView.as_view(), name='projects'),
   path('success/', views.success, name='success')
]  