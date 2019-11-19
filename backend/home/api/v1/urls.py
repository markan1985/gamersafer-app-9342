from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import SignupViewSet, LoginViewSet, HomePageViewSet, CustomTextViewSet, AppReportView,PreferenceViewSet,UserByUserNameViewSet,UserView,UserByUnameView,SignupVerifyViewSet

router = DefaultRouter()

router.register('userbyusername', UserByUserNameViewSet, base_name='userbyusername')



router.register('signupverify', SignupVerifyViewSet, base_name='signupverify')

router.register('signup', SignupViewSet, base_name='signup')
router.register('login', LoginViewSet, base_name='login')
router.register('add-preferences', PreferenceViewSet, base_name='preferences')
#router.register('getuser', UserViewSet, base_name='getuser')
router.register('customtext', CustomTextViewSet)


router.register('homepage', HomePageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("report", AppReportView.as_view(), name="app_report"),
    url(r'^userbyid/(?P<id>\d+)/$',UserView.as_view(), name="userbyid" ),
    url(r'^usersbyusername/(?P<username>[ A-Za-z0-9\[\]()*\-+/%]+)/$',UserByUnameView.as_view(), name="usersbyusername" )
]

 
