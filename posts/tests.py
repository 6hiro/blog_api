import json
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
# from rest_framework_simplejwt.tokens import RefreshToken
from .models import CategoryModel, PostModel, TagModel


class TestGetPostsView(APITestCase):
    TARGET_URL = "/api/v1/post/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            email="test@test.test",
            password="testpassword"
        )
        cls.category = CategoryModel.objects.create(name='test_category')
        cls.tag = TagModel.objects.create(name='test_tag')
        cls.post1 = PostModel.objects.create(
            posted_by=cls.user,
            title='test1',
            post='test1 post',
            preview_content='test1 preview content',
            is_public='public',
            category=cls.category,
            # tags=cls.tag,
        )
        cls.post2 = PostModel.objects.create(
            posted_by=cls.user,
            title='test2',
            post='test2 post',
            preview_content='test2 preview content',
            is_public='public',
            category=cls.category,
        )

    def test_get_posts_success(self):
        response = self.client.get(self.TARGET_URL, format='json')
        content = json.loads(response.content)
        # print(content["results"][0])
        self.assertEqual(content["results"][1]["post"], self.post1.post)
        self.assertEqual(content["results"][0]["post"], self.post2.post)
        self.assertEqual(content["count"], 2)


class TestGetPostsView(APITestCase):
    TARGET_URL = "/api/v1/post/category/test_category/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            email="test@test.test",
            password="testpassword"
        )
        cls.category = CategoryModel.objects.create(name='test_category')
        cls.tag = TagModel.objects.create(name='test_tag')
        cls.post1 = PostModel.objects.create(
            posted_by=cls.user,
            title='test1',
            post='test1 post',
            preview_content='test1 preview content',
            is_public='public',
            category=cls.category,
            # tags=cls.tag,
        )
        cls.post2 = PostModel.objects.create(
            posted_by=cls.user,
            title='test2',
            post='test2 post',
            preview_content='test2 preview content',
            is_public='public',
            category=cls.category,
        )

    def test_get_posts_by_category_success(self):
        response = self.client.get(self.TARGET_URL, format='json')
        content = json.loads(response.content)
        # print(content["results"][0])
        self.assertEqual(content[1]["post"], self.post1.post)
        self.assertEqual(content[0]["post"], self.post2.post)
        # self.assertEqual(content["count"], 2)

# class TestCreateUpdateDeletePostView(APITestCase):
#     TARGET_URL = "/api/v1/create_update_delete_post/"

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.user = get_user_model().objects.create_user(
#             email="test@test.test",
#             password="testpassword"
#         )
#         cls.category = CategoryModel.objects.create(name='test_tag')

#     def test_create_post_success(self):
#         token = str(RefreshToken.for_user(self.user).access_token)
#         self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
#         params = {
#             'title': 'title',
#             'post': 'test #test',
#             'isPublic': 'public',
#             'category': self.category.pk,
#             'tags': 'python django'
#         }

#         response = self.client.post(self.TARGET_URL, params, format='json')
#         # print(response.content)
#         self.assertEqual(PostModel.objects.count(), 1)
#         self.assertEqual(response.status_code, 201)
#         post = PostModel.objects.get()

#         content = json.loads(response.content)
#         # print(content)
#         self.assertEqual(content["post"], post.post)
#         self.assertEqual(content["isPublic"], post.is_public)
#         self.assertEqual(content["id"], str(post.id))

#     def test_create_post_without_access_token(self):
#         token = str(RefreshToken.for_user(self.user).access_token)
#         # self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
#         params = {
#             'title': 'title',
#             'post': 'test #test',
#             'isPublic': 'public',
#         }
#         response = self.client.post(self.TARGET_URL, params, format='json')
#         self.assertEqual(PostModel.objects.count(), 0)
#         self.assertEqual(response.status_code, 401)

#     def test_create_post_without_content(self):
#         token = str(RefreshToken.for_user(self.user).access_token)
#         self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
#         params = {
#             'title': 'title',
#             'post': '',
#             'is_public': 'public',
#         }
#         response = self.client.post(self.TARGET_URL, params, format='json')
#         self.assertEqual(PostModel.objects.count(), 0)
#         self.assertEqual(response.status_code, 400)
