# import json
# from django.contrib.auth import get_user_model
# from rest_framework.test import APITestCase
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.urls import reverse


# class TestRefreshToken(APITestCase):
#     REFRESHTOKEN_URL = "/api/v1/token/refresh/"

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.user = get_user_model().objects.create_user(
#             email="test@test.test",
#             password="testpassword"
#         )

#     def test_refreshtoken_success(self):
#         refresh_token = str(RefreshToken.for_user(self.user))
#         # print(refresh_token)
#         params = {
#             'refresh': refresh_token
#         }
#         response = self.client.post(
#             self.REFRESHTOKEN_URL, params, format='json')
#         self.assertEqual(response.status_code, 200)

#         content = json.loads(response.content)
#         # print(content["access"])

#     def test_refreshtoken_bad_request(self):
#         refresh_token = str(RefreshToken.for_user(self.user))
#         params = {
#             'refresh': "BAD_TOKEN"
#         }
#         response = self.client.post(
#             self.REFRESHTOKEN_URL, params, format='json')
#         self.assertEqual(response.status_code, 401)


# class TestLoginViewSet(APITestCase):

#     LOGIN_URL = "/api/v1/login/"

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.user = get_user_model().objects.create_user(
#             email="test@test.test",
#             password="testpassword"
#         )

#     def test_login_success(self):
#         params = {
#             'email': 'test@test.test',
#             'password': 'testpassword'
#         }
#         response = self.client.post(self.LOGIN_URL, params, format='json')

#         self.assertEqual(response.status_code, 200)

#         content = json.loads(response.content)
#         refresh = content["tokens"]["refresh"]
#         access = content["tokens"]["access"]

#     def test_login_with_wrong_password(self):
#         params = {
#             'email': 'test@test.test',
#             'password': 'wrongpassword'
#         }
#         response = self.client.post(self.LOGIN_URL, params, format='json')

#         self.assertEqual(response.status_code, 401)
#         content = json.loads(response.content)
#         self.assertEqual(content["detail"], 'Invalid Credentials, try again')

#     def test_login_with_wrong_password(self):
#         params = {
#             'email': 'wrong@wrong.wrong',
#             'password': 'testpassword'
#         }
#         response = self.client.post(self.LOGIN_URL, params, format='json')

#         self.assertEqual(response.status_code, 401)
#         content = json.loads(response.content)
#         self.assertEqual(content["detail"], 'Invalid Credentials, try again')
