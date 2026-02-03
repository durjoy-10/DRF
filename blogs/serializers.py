from rest_framework import serializers
from .models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) # Nested serialization of comments
    # Here, we include all fields from the Blog model along with its related comments
    # Here comments is related_name in ForeignKey of Comment model
    class Meta:
        model = Blog
        fields = '__all__'