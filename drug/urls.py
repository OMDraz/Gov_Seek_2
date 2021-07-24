from django.urls import path
from .views import DrugDetail, DrugList

urlpatterns = [
    path('', DrugList.as_view()),
    path('<int:pk>', DrugDetail.as_view()),
]

