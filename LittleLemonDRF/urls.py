from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('book-lists',views.BookListView.as_view()),
     path('book-lists/<int:pk>',views.SingleBookView.as_view()),
     path('secret/',views.secret),
     path('api-token-auth/',obtain_auth_token),
     path('manager-view',views.manager_view),
     path('groups/managers/users',views.managers)
     #path('author/<int:pk>', views.author_detail, name='authordet-detail'), #fOR HyperLink
     #path('books/<int:pk>', views.book_detail, name='book-detail'),
     ]
     # path('books', views.books),
     # path('',views.home),
     #path('orders',views.Orders.listOrders),
     #path('books', views.BookView.as_view()),
     #path('books/<int:pk>',views.Book.as_view())
# 	path('books', views.BookView.as_view(
#           {
#                'get': 'list',
#                'post': 'create',
#           })
# 	),
#      path('books/<int:pk>',views.BookView.as_view(
#      {
#                'get': 'retrieve',
#                'put': 'update',
#                'patch': 'partial_update',
#                'delete': 'destroy',
#       })
# 	)


#Routing with SimpleRouter class in DRF
# from rest_framework.routers import SimpleRouter

# router = SimpleRouter(trailing_slash=False)
# router.register('books',views.BookView, basename='books')
# urlpatterns = router.urls

#Routing with DefaultRouter class in DRF
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter(trailing_slash=False)
# router.register('books',views.BookView, basename='books')
# urlpatterns = router.urls