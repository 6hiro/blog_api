from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from posts.models import CategoryModel, PostModel, TagModel


# class LoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         max_length=255, min_length=3, write_only=True)
#     password = serializers.CharField(
#         max_length=68, min_length=6, write_only=True)
#     tokens = serializers.SerializerMethodField()

#     def get_tokens(self, obj):
#         user = get_user_model().objects.get(email=obj['email'])

#         return {
#             'refresh': user.tokens()['refresh'],
#             'access': user.tokens()['access']
#         }

#     class Meta:
#         model = get_user_model()
#         fields = ['email', 'password', 'tokens']

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         password = attrs.get('password', '')

#         # if the given credentials are valid, return a User object.
#         user = auth.authenticate(email=email, password=password)

#         if not user:
#             raise AuthenticationFailed('Invalid Credentials, try again')
#         if not user.is_active:
#             raise AuthenticationFailed('Account disabled, contact admin')
#         if not user.is_verified:
#             raise AuthenticationFailed('Email is not verified')

#         return {
#             'email': user.email,
#         }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ['id', 'name']


# class CreateUpdateDeletePostSerializer(serializers.ModelSerializer):
#     tags = serializers.CharField(max_length=100, required=False)

#     class Meta:
#         model = PostModel
#         fields = ['id', 'title', 'post', 'preview_content',
#                   'posted_by', 'is_public', 'category', 'tags']
#         extra_kwargs = {
#             'posted_by': {'read_only': True},
#         }

#     def create(self, validated_data):
#         tag_list = []
#         if validated_data.get('tags', None) is not None:
#             for word in validated_data['tags'].split():
#                 tag = TagModel.objects.filter(name=word).first()
#                 if tag:
#                     tag_list.append(tag.pk)

#                 else:
#                     new_tag = TagModel(name=word)
#                     new_tag.save()
#                     tag_list.append(new_tag.pk)
#         validated_data['tags'] = []
#         post = super().create(validated_data)
#         post.tags.set(tag_list)
#         print(tag_list)
#         print(post.tags)

#         return post

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.post = validated_data.get('post', instance.post)
#         instance.preview_content = validated_data.get(
#             'preview_content', instance.preview_content)
#         instance.is_public = validated_data.get(
#             'is_public', instance.is_public)
#         instance.category = validated_data.get(
#             'category', instance.category)

#         tags = []
#         if validated_data.get('tags', None) is not None:
#             for word in validated_data['tags'].split():
#                 tag = TagModel.objects.filter(name=word).first()
#                 if tag:
#                     tags.append(tag.pk)

#                 else:
#                     new_tag = TagModel(name=word)
#                     new_tag.save()
#                     tags.append(new_tag.pk)
#             validated_data['tags'] = None

#         instance.save()
#         instance.tags.clear()
#         instance.tags.set(tags)

#         return instance


class GetPostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d", read_only=True)
    updated_at = serializers.DateTimeField(
        format="%Y-%m-%d", read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')
    tags = TagSerializer(many=True)

    class Meta:
        model = PostModel
        fields = ['id', 'title', 'post', 'preview_content', 'posted_by', 'created_at', 'updated_at',
                  'is_public', 'tags', 'category', 'category_name']
        extra_kwargs = {'posted_by': {'read_only': True}}


class GetPostIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id', ]
