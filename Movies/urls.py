from django.urls import path
from .views import MovieViewSet, HallViewSet, SessionViewSet, BookingViewSet, RegisterView


urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/movies/', MovieViewSet.as_view(), name='get-all-movies'),
    path('api/halls/', HallViewSet.as_view(), name='get-all-halls'),
    path('api/sessions/', SessionViewSet.as_view(), name='get-all-sessions'),
    path('api/bookings/', BookingViewSet.as_view(), name='get-all-bookings'),
]
