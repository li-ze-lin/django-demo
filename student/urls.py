from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('to_add/', views.to_add, name='to_add'),
    # ex: /polls/5/results/
    path('add/', views.add, name='add'),
    # ex: /polls/5/vote/
    path('delete/<int:student_id>', views.delete, name='delete'),
]