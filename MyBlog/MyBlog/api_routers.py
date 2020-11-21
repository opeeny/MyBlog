from rest_framework import routers
from Blog import api_viewsets as Blog_views

router = routers.DefaultRouter()
router.register('posts', Blog_views.PostViewset)