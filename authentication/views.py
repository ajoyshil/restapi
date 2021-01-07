import datetime
from rest_framework.generics import GenericAPIView, \
    get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, LoginSerializer, ProfileSerializer, EmployeeSerializer
from django.conf import settings
from django.contrib import auth
import jwt
from .models import User, Profile, Employee
from rest_framework import generics, mixins, permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
import pytz
from restapi.settings import TIME_ZONE


# class RegisterView(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if user:
            payload = {"email": email,
                       'exp': datetime.datetime.now(tz=pytz.timezone(TIME_ZONE)) + datetime.timedelta(days=300)}
            auth_token = jwt.encode(
                payload, settings.JWT_SECRET_KEY, 'HS256')

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = "id"

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class EmployeeView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated,]
    lookup_field = "id"





