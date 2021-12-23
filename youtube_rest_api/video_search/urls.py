from django.urls import path, include
from . import views
from rest_framework import routers


# urlpatterns = [
#     path('',views.index,name='index'),
#     # path('api/',views.FeedViewSet,name='api'), # added
#     path('search/',views.search,name='search')
# ]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
router=routers.DefaultRouter() 
router.register(r'api/get_feed',views.FeedViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/',views.index,name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('search/',views.search,name='search')
]
