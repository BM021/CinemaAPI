from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Movie, Hall, Session, Booking
from .serializers import (
    MovieSerializer, HallSerializer, SessionSerializer, BookingSerializer, RegisterSerializer
)


# Представление для регистрации
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Представления для фильмов
class MovieViewSet(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Представления для залов
class HallViewSet(generics.CreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


# Представления для сеансов
class SessionViewSet(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


# Представления для бронирования билетов
class BookingViewSet(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
