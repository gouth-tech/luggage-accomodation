from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .serailizers import LuggageSerializer, LuggageUpdateSerializer, BookingSerializer
from rest_framework import status
from .models import Luggage, Booking
from rest_framework.permissions import IsAuthenticated
from apps.accounts.models import ExpiringToken


class LuggageCreationAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LuggageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        token = request.headers.get('Authorization')
        key = token.split(' ', 1)[1]
        lug_id = data['id']
        owner_name = ExpiringToken.objects.get(key=key).user
        to_edit = Luggage.objects.get(id=lug_id)
        to_edit.owner_name = owner_name
        to_edit.save()
        return Response(data={'data': data, 'message': 'Successfully Created'}, status=status.HTTP_201_CREATED)


class BookingCreationAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        token = request.headers.get('Authorization')
        key = token.split(' ', 1)[1]
        id = data['id']
        owner_id = data['owner_id']
        lug_obj = Luggage.objects.get(id=owner_id)
        types = lug_obj.type.all()
        lst = [i.name for i in types]
        customer_name = ExpiringToken.objects.get(key=key).user
        to_edit = Booking.objects.get(id=id)
        to_edit.customer_name = customer_name
        to_edit.save()
        return Response(data={'data': data, 'types': lst, 'message': 'Booking Successful'},
                        status=status.HTTP_201_CREATED)


class LuggageUpdateView(RetrieveUpdateAPIView):
    permission_classes = ()
    serializer_class = LuggageUpdateSerializer

    def get_object(self):
        queryset = Luggage.objects.get(id=self.request.GET.get('luggage_id'))
        return queryset

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        return Response(data={'data': data, 'message': 'Successfully Updated'}, status=status.HTTP_200_OK)
