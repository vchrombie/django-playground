from rest_framework import serializers

from .models import User, Cart, DeliveryCost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'created_at', 'updated_at', ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'item', 'quantity', 'created_at', 'updated_at', ]


class DeliveryCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['id', 'status', 'cost_per_delivery', 'cost_per_product', 'fixed_cost', 'created_at', 'updated_at', ]
