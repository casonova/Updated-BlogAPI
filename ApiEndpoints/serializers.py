from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 15:
            raise serializers.ValidationError("Max title length is 15 characters")
        return value
                
    def validate_post_body(self,value):
        if len(value) > 300:
            raise serializers.ValidationError("Max Body length is 300 characters")
        return value

class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, data):
        comment_body = data.get("comment_body")
        if len(comment_body) > 50:
            raise serializers.ValidationError("Max Comment length is 50 characters")  
        return data