from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from strawberry.django.views import AsyncGraphQLView

urlpatterns = [
    path('admin2024/', admin.site.urls),
    path('', include('api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^filer/', include('filer.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    #path('graphql2', AsyncGraphQLView.as_view(schema=schema)),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

