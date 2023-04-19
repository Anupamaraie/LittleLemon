from rest_framework import generics
from .models import Book
from .serializers import BookListSerializer

class BookListView(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookListSerializer

class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookListSerializer










































# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from django.db import IntegrityError
# from .models import Book
# from django.views.decorators.csrf import csrf_exempt
# from django.forms.models import model_to_dict

# Create your views here.
# @csrf_exempt
# def books(request):
#     if request.method == 'GET':
#         books = Book.objects.all().values()
#         return JsonResponse({'books':list(books)})
#     elif request.method == 'POST':
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         price = request.POST.get('price')
#         inventory = request.POST.get('inventory')
#         book = Book(title=title, author=author, price=price, inventory=inventory)

#         try:
#             book.save()
#         except IntegrityError:
#             return JsonResponse({'error':'true','message':'required field missing'},status=400)

#         return JsonResponse(model_to_dict(book), status=201)

# def home(request):
#     return HttpResponse("Hi there.")

#Routing to a class method

from rest_framework.decorators import api_view, APIView

from rest_framework.response import Response
from rest_framework import status

# class Orders():
#     @staticmethod
#     @api_view()
#     def listOrders(request):
#         return Response({'message':'list of orders'},200)


#Routing class-based views

# class BookView(APIView):
# 	def get(self, request):
# 		author = request.GET.get('author')
# 		if (author):
# 			return Response({"message":"List of books by " + author},status = status.HTTP_200_OK)
# 		return Response({"message":"list of books"}, status=status.HTTP_200_OK)

# 	def post(self,request):
# 		return Response({"message":"new book created"}, status=status.HTTP_201_CREATED)

# class Book(APIView):

# 	def get(self,request,pk):
# 		return Response({"message":"single book with id " + str(pk)}, status = status.HTTP_200_OK)

# 	def put(self, request, pk):
# 		return Response({"title":request.data.get('title')}, status =status.HTTP_200_OK)


#Routing classes that extend viewsets
# from rest_framework import viewsets

# class BookView(viewsets.ViewSet):
# 	def list(self, request):
#         	return Response({"message":"All books"}, status.HTTP_200_OK)
# 	def create(self, request):
#         	return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
# 	def update(self, request, pk=None):
#         	return Response({"message":"Updating a book"}, status.HTTP_200_OK)
# 	def retrieve(self, request, pk=None):
#         	return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
# 	def partial_update(self, request, pk=None):
#             return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
# 	def destroy(self, request, pk=None):
#         	return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
	
	#getting permission for authenticated users
	# def get_permission(self):
	# 	permission_classes = []
	# 	if self.request.method != 'GET':
	# 		permission_classes = [IsAuthenticated]

	# 	return [permission() for permission in permission_classes]
