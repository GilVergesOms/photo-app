from django.urls import path
from apps.users.api.api import user_api_view, user_detail_api_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user/',user_api_view,name = 'user_api'),
    path('user/<int:pk>/', user_detail_api_view,name='user_detail_api_view'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token')
]