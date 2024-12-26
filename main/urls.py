from django.urls import path
from .views import HomeView, TrainView, PredictView


urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('train/', TrainView.as_view(), name='Train'),
    path('predict/', PredictView.as_view(), name='Predict'),
]
