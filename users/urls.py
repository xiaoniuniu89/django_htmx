from django.urls import path
from .views import (
    RegisterView,
    check_username,
    login_user,
    logout_user
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register' ),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

htmx_url_patterns = [
    path('register/check_username/', check_username, name='check-username')
]


urlpatterns += htmx_url_patterns