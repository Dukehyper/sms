from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('students/<int:id>',views.students,name='student'),
    path('subject/<int:id>',views.subject,name='subject')
    
]
