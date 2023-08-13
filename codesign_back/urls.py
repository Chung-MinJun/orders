from django.urls import path
from .views import ReactAppView
from . import views

urlpatterns = [
    # 기존에 있던 다른 URL 패턴들
    # ...
    
    # ReactAppView를 '/react-app/' URL에 매핑
    path('', ReactAppView.as_view(), name='react-app'),
    # path('api/orders/', views.api_orders, name='api_orders'),
    
]
