from django.urls import path, include
# from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import account, posts

app_name = 'apiv1'

router = DefaultRouter()
router.register('post', posts.GetPostView)
router.register('post-ids', posts.GetPostIdsView)
# router.register('create_update_delete_post', posts.CreateUpdateDeletePostView)
router.register('categories', posts.GetAllCategoriesView)
router.register('tags', posts.GetAllTagsView)


urlpatterns = [
    path('', include(router.urls)),
    # login
    # path('login/', account.LoginApiView.as_view(), name="login"),
    # path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    # post
    path('post/page', posts.post_pages, name='post-page'),
    # path('post/search/<str:word>/', posts.posts_searched, name="search-post"),
    path('post/category/<str:name>/', posts.posts_category, name='post-category'),
    path('post/tag/<str:name>/', posts.posts_tag, name="post-tag"),
]
