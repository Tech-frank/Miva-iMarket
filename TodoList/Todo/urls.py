from django.urls import path
from .views import Index, detailViews, updateViews, deleteViews, createViews

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('details/<int:pk>/', detailViews.as_view(), name='details_todo'),
    path('add/', createViews.as_view(), name='add_todo'),
    path('details/edit/<int:pk>/', updateViews.as_view(), name='edit_todo'),
    path('details/<int:pk>/delete', deleteViews.as_view(), name='delete_todo'),
]