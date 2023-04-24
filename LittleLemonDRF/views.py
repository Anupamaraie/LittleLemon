from rest_framework import generics
from .models import Book, AuthorDet
from .serializers import BookListSerializer, AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


#For Hyperlink
#@api_view()
# def author_detail(request, pk):
# 	authdet = get_object_or_404(AuthorDet,pk=pk)
# 	serialized_category = AuthorSerializer(authdet)
# 	return Response(serialized_category.data)

# def book_detail(request, pk):
# 	book = get_object_or_404(Book,pk=pk)
# 	serialized_book = BookListSerializer(book, many = True, context={'request':request})
# 	return (serialized_book.data)

class BookListView(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookListSerializer

class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookListSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
	return Response({"message":"Some secret message"})

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
	if request.user.groups.filter(name='Manager').exists():
		return Response({'message':'Only manager should see this'})
	else:
		return Response({'message':'You are not authorized'},403)

@api_view()
@permission_classes([IsAdminUser])
def managers(request):
	username = request.data['username']
	if username:
		user = get_object_or_404(User, username=username)
		managers = Group.objects.get(name="Manager")
		if request.method == 'POST':
			managers.user_set.add(user)
		if request.method == 'DELETE':
			managers.user_set.remove(user)
		return Response({"message":"ok"})

	return Response({"message":"error"}, status.HTTP_400_BAD_REQUEST)







































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
