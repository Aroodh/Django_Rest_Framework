from django.http import Http404, JsonResponse
from django.shortcuts import render
from students.models import Student
from .Serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from rest_framework import mixins
from rest_framework import generics
# Create your views here.

@api_view(['GET','POST'])
def studentView(request):
    #The below code for the manual serializer
    #Serializer is used to convert the queryset data to json data
    
    # students=Student.objects.all()
    # student_list=list(students.values())
    # print(student_list)
    # return JsonResponse(student_list,safe=False)


    if request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages)


#fetch each student separately by primary Key
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
#class Based view

# class EmployeeView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         serializer.is_valid()
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    # def get(self,request,pk):
    #     employee=Employee.objects.get(pk=pk)
    #     serializer=EmployeeSerializer(employee)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    
        


# class EmployeeDetails(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
#     def delete(self,request,pk):
#         employee=self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



"""
#Mixins
class EmployeeView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
        
    
#mixins
class EmployeeDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
"""

#Generics
class EmployeeView(generics.ListAPIView,generics.CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeDetails(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='pk'