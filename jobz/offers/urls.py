from django.urls import path

from . import views

app_name = 'jobz'

urlpatterns = [
    # ex: /jobz/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /jobz/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /jobz/new/offer
    path('new/offer/', views.new_offer, name='new_offer'),
    # ex: /jobz/new/offer
    path('new/company/', views.new_company, name='new_company'),
    # ex: /jobz/save/
    path('save/', views.save_new, name='save'),
    # ex: jobz/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    # ex: /jobz/save_edit/
    path('<int:pk>/save_edit/', views.save_edit, name='save_edit'),
	# ex: /jobz/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
]
