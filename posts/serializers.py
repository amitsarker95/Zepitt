from .models import Posts, Vote
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = [
            'id',
            'title',
            'url',
            'user',
            'created_at'
        ]

        read_only_fields = ['id', 'created_at']

    # def create(self, validated_data):
    #     user = self.context['request'].user

    #     post = Posts.objects.create(
    #         user = user,
    #         **validated_data
    #     )

    #     return post