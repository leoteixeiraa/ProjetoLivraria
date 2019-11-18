from django.urls.conf import path
from AppLivraria.views import Index

urlpatterns = [
    path('', Index.as_view(), name="index"),
    ]