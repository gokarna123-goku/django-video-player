from django.urls import path
from .views import RegisterView, LoginView, UserProfileView
app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('verify-link/<str:action>/<str:email>/<str:token>/', VerifyLinkView.as_view(), name='verify-link'),
    # path('logout', DLogoutView.as_view(),name='logout'),
    # path('forgot-password', ForgetPasswordUserFind.as_view(), name='forgot-password'),
    # path('reset-password/<str:email>/<str:reset_token>/', ResetPasswordView.as_view(), name='reset-password'),
    #  path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]