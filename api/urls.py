from django.urls import include, path

from api.router import urlpatterns

urlpatterns += [
    path('auth/', include("api.auth.urls")),
]
