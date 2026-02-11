from django.urls import path
from . import views
urlpatterns=[
    
    #function based Views
    path('students/',views.studentView),
    path('student/<int:pk>/',views.studentDetailView),
    
    #class based Views 
    path('employees/',views.EmployeeView.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetails.as_view())
]
