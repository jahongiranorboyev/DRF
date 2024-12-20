from  rest_framework.routers import DefaultRouter

from myapp.account.api_viewset import AccountViewSet

router = DefaultRouter()

router.register(r'', AccountViewSet)
