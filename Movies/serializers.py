from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Hall, Session, Booking


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    hall = HallSerializer()

    class Meta:
        model = Session
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    session = SessionSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
