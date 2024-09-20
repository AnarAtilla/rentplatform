from django.contrib.auth import update_session_auth_hash
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Регистрация пользователя
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Получение профиля пользователя
class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# Изменение пароля
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Проверка старого пароля
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "Неправильный пароль."}, status=status.HTTP_400_BAD_REQUEST)
            # Установка нового пароля
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            update_session_auth_hash(request, self.object)
            return Response({"detail": "Пароль успешно изменен."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
