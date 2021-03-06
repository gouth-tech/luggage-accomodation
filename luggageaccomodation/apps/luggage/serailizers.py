from .models import Luggage, Booking
from rest_framework import serializers


class LuggageSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        luggage = Luggage.objects.get(id=obj.id)
        type = luggage.type.all()
        total = 0
        for cost in type:
            total += cost.cost
        return total

    class Meta:
        model = Luggage
        fields = ('id', 'type', 'space_alloted', 'total_amount',)


class LuggageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Luggage
        fields = ('id', 'space_status',)


class BookingSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()
    total_slots = serializers.SerializerMethodField()

    def validate(self, attrs):
        if not attrs.get('owner_id') == []:
            self.owner = attrs.get('owner_id')
        return attrs

    def get_total_slots(self, obj):
        luggage = Luggage.objects.get(id=self.owner.id).space_alloted
        return luggage

    def get_total_amount(self, obj):
        luggage = Luggage.objects.get(id=self.owner.id)
        type = luggage.type.all()
        total = 0
        for cost in type:
            total += cost.cost
        return total

    class Meta:
        model = Booking
        fields = ('id', 'owner_id', 'total_slots', 'total_amount',)

