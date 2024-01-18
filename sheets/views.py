from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from .serializers import BooksSerializer

class BooksListView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Yangi kitobni qo'shishda user_id ni olib qo'yish
        serializer.save(user_id=self.request.user)

class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Kitobni tahrirlashda faqat ozi kiritgan kitob malumotlarini tahrirlash
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
