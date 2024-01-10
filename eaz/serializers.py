from rest_framework import serializers
from .models import Thing , Category , Image
from django.contrib.auth.models import User

# class ImageSer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ['image']

class ThingSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    # images = serializers.HyperlinkedRelatedField(query_set=)
    # images = ImageSer(read_only=True,many=True)

    class Meta:
        model = Thing
        fields = ['id','name','description','category','link','images']
        # read_only_fields = ['id','name','description','category','link']

    def get_images(self,obj):
        request = self.context.get('request')
        try:
            images= [request.build_absolute_uri(i.image.url) for i in obj.images.all()]
            # images= [i.image.url for i in obj.images.all()]

        except:
            images = None
        return images


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','slug']


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    # class Meta:
    #     model = User
    #     fields = ['id','username','password']
    #     # extra_kwargs = {'password':{'write_only':True}}