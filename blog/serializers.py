from rest_framework import serializers

class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=128)
    cover = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=256)
    context = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=2048)
    created_at = serializers.DateTimeField(required=True, allow_null=False)
    
    
class SearchArticleSeializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=128)
    cover = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=256)
    context = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=2048)
    created_at = serializers.DateTimeField(required=True, allow_null=False)
    category = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=128)
    author = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=128)
    promot = serializers.BooleanField(required=True, allow_null=False)    
    
class CreateArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    context = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=2048)
    category = serializers.IntegerField(required=True, allow_null=False)
    author = serializers.IntegerField(required=True, allow_null=False)
    promot = serializers.BooleanField(required=True, allow_null=False)   