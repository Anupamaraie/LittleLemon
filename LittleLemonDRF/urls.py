from django.urls import path
from . import views

#urlpatterns = [
     # path('books', views.books),
     # path('',views.home),
     # path('orders',views.Orders.listOrders)
     # path('books/<int:pk>',views.BookView.as_view())
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
# ]


#Routing with SimpleRouter class in DRF
# from rest_framework.routers import SimpleRouter

# router = SimpleRouter(trailing_slash=False)
# router.register('books',views.BookView, basename='books')
# urlpatterns = router.urls

#Routing with DefaultRouter class in DRF
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('books',views.BookView, basename='books')
urlpatterns = router.urls