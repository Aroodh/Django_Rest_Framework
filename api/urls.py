from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')

urlpatterns=[
    
    #function based Views
    path('students/',views.studentView),
    path('student/<int:pk>/',views.studentDetailView),
    
    #class based Views 
    # path('employees/',views.EmployeeView.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetails.as_view())
    
    path('',include(router.urls))
]
