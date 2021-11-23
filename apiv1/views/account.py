# from ..serializers import LoginSerializer
# from rest_framework.response import Response
# from rest_framework import generics, status


# class LoginApiView(generics.GenericAPIView):
#     """return JWT token"""
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializers = self.serializer_class(data=request.data)
#         serializers.is_valid()

#         return Response(serializers.data, status=status.HTTP_200_OK)
