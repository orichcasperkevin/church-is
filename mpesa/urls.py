from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import STKPush,STKConfirmation

# TODO add delete views
urlpatterns = [
    # listing
    path('stk-push/<slug:phone>/<int:amount>/', STKPush),
    path('stk_confirmation/', STKConfirmation),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
