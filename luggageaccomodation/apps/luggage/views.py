from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .serailizers import LuggageSerializer, LuggageUpdateSerializer, BookingSerializer
from rest_framework import status
from .models import Luggage


class LuggageCreationAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = LuggageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data={'data': data, 'message': 'Successfully Created'}, status=status.HTTP_201_CREATED)


class BookingCreationAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data={'data': data, 'message': 'Booking Successful'}, status=status.HTTP_201_CREATED)


class LuggageUpdateView(RetrieveUpdateAPIView):
    permission_classes = ()
    serializer_class = LuggageUpdateSerializer

    def get_object(self):
        queryset = Luggage.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        return Response(data={'data': data, 'message': 'Successfully Updated'}, status=status.HTTP_200_OK)
