from rest_framework import serializers
from .models import Product,GST


class GSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = GST
        fields = '__all__'




class StockSerializer1(serializers.ModelSerializer):
    product_gst = GSTSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, attrs):
        product_name = attrs.get('product_name')
        if Product.objects.filter(product_name=product_name):
            raise serializers.ValidationError('Product Already Exists')
        return super().validate(attrs)
    

    def validate_product_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError('Product Quantity can not be in minus')
        return value

    
    def create(self, validated_data):
        
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product_name = validated_data.get("product_name",instance.product_name)
        instance.product_cost_per_quantity = validated_data.get("product_cost_per_quantity",instance.product_cost_per_quantity)       
        instance.product_cost_with_gst = validated_data.get("product_cost_with_gst",instance.product_cost_with_gst)
        if 'product_quantity' in validated_data:
            instance.product_quantity += validated_data.get ("product_quantity",instance.product_quantity)
        else:      
            instance.product_quantity = validated_data.get("product_quantity",instance.product_quantity)       
        instance.product_total_cost = validated_data.get("product_total_cost",instance.product_total_cost)       
        instance.product_category = validated_data.get("product_category",instance.product_category)       
        instance.product_gst = validated_data.get("product_gst",instance.product_gst)       
        instance.product_offer = validated_data.get("product_offer",instance.product_offer) 
        instance.save()
        return instance


    

    