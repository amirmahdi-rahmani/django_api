from rest_framework import serializers
from .models import Thing , Category 


class ThingSerializer(serializers.ModelSerializer):
    # images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Thing
        fields = ['id','name','description','category','link','images']

    # def get_images(self,obj):
    #     request = self.context.get('request')
    #     try:
    #         images= [request.build_absolute_uri(i.image.url) for i in obj.images.all()]

    #     except:
    #         images = None
    #     return images


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','slug']


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
