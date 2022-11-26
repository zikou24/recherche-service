from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('category/<str:pk>', views.categoryservice, name='category'),

    path('categorydetail/<str:pk>', views.categoryDetail, name='categorydetail'),

    path('createservice', views.createservice, name='create-service'),

    path('servicedetail/<str:pk>', views.serviceDetail, name='show-detail'),

    path('submitreview/<str:service_id>',
         views.submit_review, name="submit-review"),
]
