from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]





# from django.urls import path
# from .views import members
# from . import views

# urlpatterns = [
#     path('', views.main, name='main')
#     path('members/', views.members, name='members'),
#     path('members/details/<int:id>',views.details, name='details'),
# ]
