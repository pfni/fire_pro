from django.urls import path
from . import views

urlpatterns = [
    path('api/chat/', views.chat_with_qwen, name='chat_with_qwen'),
    # path('api/upload-image/', views.upload_image, name='upload_image'),
    # path('api/upload-file/', views.upload_file, name='upload_file'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
