from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('<int:pk>', views.product_detail, name='detail'),
]
