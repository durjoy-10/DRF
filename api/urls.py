from django.urls import path
from . import views

from django.urls import include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('viewset-employees', views.EmployeeViewSet, basename='employee')
# Here don't need to create another url pattern for detail view because router automatically handles that.

router.register('ModelViewset-employees', views.EmployeeModelViewSet, basename='employee-modelviewset')

router.register('blog', views.BlogViewSet, basename='blog')
router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentdetailView), # Function based view
    
    path('employees/', views.employees_class_view.as_view()),  # New URL pattern for Employee Class based view
    path('employees/<int:pk>/', views.employee_detail_view.as_view()),  # Placeholder for potential detail view
    
    path('mixins-employees/', views.mixinsEmployeesListCreateView.as_view()),  # Generic CBV for Employees List and Create usign mixins
    path('mixins-employees/<int:pk>/', views.mixinsEmployeesDetailView.as_view()),  # Generic CBV for Employee Detail, Update, Delete using mixins  
    
    path('generic-employees/', views.GenericEmployeesListCreateView.as_view()),  # Generic CBV for Employees List and Create using generics
    path('generic-employees/<int:pk>/', views.GenericEmployeesDetailView.as_view()),  # Generic CBV for Employee Detail, Update, Delete using generics
    
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),  # Generic Class Based View for Blog Detail, Update, Delete using generics
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),  # Generic Class Based View for Comment List and Create using generics
]
