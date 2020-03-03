# from rest_framework import generics
#
# from news.api.serializers import NewsSerializer
# from news.models import News
#
#
# class NewsList(generics.ListCreateAPIView):
#     '''
#         a list of all news recently
#     '''
#     queryset = News.objects.all()[:20]
#     serializer_class = NewsSerializer
