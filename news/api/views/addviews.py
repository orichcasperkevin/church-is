from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# from news.api.serializers import NewsSerializer
# from news.models import News
#
# class AddNews(APIView):
#     def post(self,request):
#         heading = request.data.get("heading")
#         article = request.data.get("article")
#         author = request.data.get("author")
#         data = {'heading': heading, 'article': article, 'author': author}
#
#         serializer = NewsSerializer(data=data)
#         if serializer.is_valid():
#             created = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
