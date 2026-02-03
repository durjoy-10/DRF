from django.shortcuts import render ,get_object_or_404
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404
from .paginations import CustomPagination
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.

# def studentsView(request):
    # students=Student.objects.all() 
    # students_list=list(students.values())              Manual way without serializer
    
    
    # return JsonResponse(students_list,safe=False)
    
#------------------------------------------------------------------------------------    
#Function Based Views    
    
@api_view(['GET', 'POST'])  
def studentsView(request):
    if request.method=='GET':
        students=Student.objects.all() 
        serializer=StudentSerializer(students,many=True)  # using serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET','PUT','DELETE'])
def studentdetailView(request, pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method=='PUT':
        serializer=StudentSerializer(student, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#------------------------------------------------------------------------------------    
    
    
    
#Clsss Based Views

class employees_class_view(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class employee_detail_view(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist as e:
            raise Http404 from e    # from django.http import Http404
    
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, pk):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request, pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#------------------------------------------------------------------------------------
# Generic Class Based Views using mixins 
from rest_framework import mixins, generics


class mixinsEmployeesListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class mixinsEmployeesDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, pk):                 # Retrieve method using RetrieveModelMixin
        return self.retrieve(request, pk=pk)
    
    def put(self, request, pk):                    # Update method using UpdateModelMixin
        return self.update(request, pk=pk)
    
    def delete(self,request, pk):
        return self.destroy(request, pk=pk)      # Delete method using DestroyModelMixin
    
    
    
#------------------------------------------------------------------------------------   
#------------------------------------------------------------------------------------
# Using Generic Class Based Views directly
from rest_framework import generics
class GenericEmployeesListCreateView(generics.ListAPIView, generics.CreateAPIView):  
    #class GenericEmployeesListCreateView(generics.ListCreateAPIView):  # Alternative way using ListCreateAPIView
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
class GenericEmployeesDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    #class GenericEmployeesDetailView(generics.RetrieveUpdateDestroyAPIView):  # Alternative way using RetrieveUpdateDestroyAPIView
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    
    
    
#------------------------------------------------------------------------------------
# ViewSets and Routers
from rest_framework import viewsets 
class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees, many=True)                        # fetch all employees
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()                                                       # create new employee
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def retrieve(self, request, pk=None):
        # from django.shortcuts import render ,get_object_or_404
        employee=get_object_or_404(Employee, pk=pk)                             # fetch single employee        
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        employee=get_object_or_404(Employee, pk=pk)
        serializer=EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()                                                   # update existing employee
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        employee=get_object_or_404(Employee, pk=pk)
        employee.delete()                                                       # delete existing employee
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
#------------------------------------------------------------------------------------
# ModelViewSet and Routers

class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination  # from .paginations import CustomPagination
    filterset_class = EmployeeFilter  # from employees.filters import EmployeeFilter
    
    # filterset_fields = ['position']  # Enable filtering by position
    
    # The ModelViewSet class automatically provides implementations for list, create, retrieve, update, and destroy actions.
    


#------------------------------------------------------------------------------------
# Blog and Comment ViewSets
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends= [SearchFilter,OrderingFilter] # from rest_framework.filters import SearchFilter, OrderingFilter
    search_fields = ['^title', '^content']  # Enable searching by title and content
    ordering_fields = ['created_at'] # Enable ordering by created_at

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
    
    
#------------------------------------------------------------------------------------    
# Generic Class Based Views for a particular Blog and Comment using generics and pk

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class= BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class= CommentSerializer
    lookup_field = 'pk'    