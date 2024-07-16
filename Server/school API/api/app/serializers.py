from rest_framework import serializers
from .models import contact
from .models import register
# from .models import Booking
from .models import Book

class ContactSerializer(serializers.ModelSerializer):
    class Meta :
        model=contact
        fields='__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=register
        fields='__all__'

class RegisterloginSerializer(serializers.ModelSerializer):
    class Meta:
        model=register
        fields=('email','password')

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
