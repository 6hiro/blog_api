from django.contrib.auth import get_user_model
from rest_framework import generics, status, viewsets, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
import math
# from rest_framework.pagination import PageNumberPagination
from posts.models import (
    PostModel,
    TagModel,
    CategoryModel
)
from ..serializers import (
    # CreateUpdateDeletePostSerializer,
    CategorySerializer,
    GetPostIdSerializer,
    GetPostSerializer,
    TagSerializer
)
# from ..permissions import IsOwnPostOrReadOnly


# class CreateUpdateDeletePostView(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
#     queryset = PostModel.objects.all()
#     serializer_class = CreateUpdateDeletePostSerializer
#     permission_classes = (IsOwnPostOrReadOnly, IsAuthenticated)

#     def perform_create(self, serializer):
#         serializer.save(posted_by=self.request.user)


class GetPostView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = PostModel.objects.filter(is_public="public")
    serializer_class = GetPostSerializer
    # permission_classes = (IsOwnPostOrReadOnly,)

    def get_queryset(self):
        return PostModel.objects.filter(is_public="public")


class GetPostIdsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = PostModel.objects.filter(is_public="public")
    serializer_class = GetPostIdSerializer
    # permission_classes = (IsOwnPostOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        return PostModel.objects.filter(is_public="public")


@ api_view(['GET'])
def post_pages(request):
    """ number of page """
    counts = PostModel.objects.filter(is_public="public").count()
    page_size = 10
    return Response(
        [{'page': i} for i in range(1, math.ceil(counts/page_size)+1)]
    )


class GetAllCategoriesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ return all categories """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class GetAllTagsView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ return all tags """
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


# @api_view(['GET'])
# def posts_searched(request, word):
#     """return searched posts"""
#     posts = PostModel.objects.filter(Q(post__contains=word, is_public="public") | Q(
#         title__contains=word, is_public="public"))
#     # paginator = PageNumberPagination()
#     # paginator.page_size = 10
#     # result_page = paginator.paginate_queryset(posts, request)
#     # serializer = GetPostSerializer(result_page, many=True)
#     # return paginator.get_paginated_response(serializer.data)
#     serializer = GetPostSerializer(posts, many=True)
#     return Response(serializer.data)


@ api_view(['GET'])
def posts_category(request, name):
    """return posts that fit into the category"""
    posts = PostModel.objects.filter(category__name=name, is_public="public")
    # paginator = PageNumberPagination()
    # paginator.page_size = 10
    # result_page = paginator.paginate_queryset(posts, request)
    # return paginator.get_paginated_response(serializer.data)
    serializer = GetPostSerializer(posts, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def posts_tag(request, name):
    """return posts that fit into the tag"""
    posts = PostModel.objects.filter(tags__name=name, is_public="public")
    # paginator = PageNumberPagination()
    # paginator.page_size = 10
    # result_page = paginator.paginate_queryset(posts, request)
    # serializer = GetPostSerializer(result_page, many=True)
    # return paginator.get_paginated_response(serializer.data)
    serializer = GetPostSerializer(posts, many=True)
    return Response(serializer.data)
