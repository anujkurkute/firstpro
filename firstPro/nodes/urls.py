from django.urls import path
from . import views
urlpatterns = [
    path('nodes', views.listView.as_view(),name="nodes.list"),
    path('nodes/<int:pk>',views.detailView.as_view(),name="nodes.detail"),
    path('nodes/new',views.createView.as_view(), name="nodes.new"),
    path('nodes/<int:pk>/edit',views.UpdateView.as_view(),name='nodes.update'),
    path('nodes/<int:pk>/delete',views.DeleteView.as_view(),name='nodes.delete')
]

