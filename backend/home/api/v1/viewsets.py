import json

from django import apps
from django.core.management import call_command
from .permissions import CrowboticsExclusive

from rest_framework import status
from rest_framework import generics

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from home.api.v1.serializers import SignupSerializer, CustomTextSerializer, HomePageSerializer, UserSerializer,PreferencesSerializer,UserByUserNameSerializer,SignupVerifySerializer
from home.models import CustomText, HomePage
from users.models import Preferences,User
 
class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ['post']


class SignupVerifyViewSet(ModelViewSet):
    serializer_class = SignupVerifySerializer
    http_method_names = ['post']


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({'error_code':200, error_message:'', 'token': token.key, 'user': user_serializer.data})

 

class UserByUserNameViewSet(ModelViewSet): 
  #  @action(detail=True)
    def vote(self, request, pk=None):
        User.objects.filter(id=pk).update(username='addddddddddd')
        return Response()

   

class PreferenceViewSet(ModelViewSet):
     serializer_class = PreferencesSerializer
    




class UserView(generics.RetrieveUpdateDestroyAPIView): # details View
    # pass
     lookup_field           ='id'
     serializer_class       =UserSerializer

     def get_queryset(self):
        return User.objects.all()

class UserByUnameView(generics.RetrieveUpdateDestroyAPIView): # details View
    # pass
     lookup_field           ='username'
     serializer_class       =UserSerializer

     def get_queryset(self):
      return User.objects.all()

   #  def get_object

 

class CustomTextViewSet(ModelViewSet):
    serializer_class = CustomTextSerializer
    queryset = CustomText.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'put', 'patch']



class HomePageViewSet(ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'put', 'patch']


class AppReportView(APIView):
    """
    DO NOT REMOVE THIS CODE SNIPPET, YOUR DASHBOARD MAY NOT REFLECT THE CORRECT
    RESOURCES IN YOUR APP.
    """
    permission_classes = [CrowboticsExclusive]

    def _get_models(self):
        project_models = apps.apps.get_models(
            include_auto_created=True, include_swapped=True
        )
        parsed_data = [
            str(model).split(".")[-1].replace("'", "").strip(">") for model in
            project_models
        ]
        return parsed_data

    def _get_urls(self):
        parsed_data = json.loads(call_command("show_urls", format="json"))
        return parsed_data

    def get(self, request):
        return Response({
            "models": self._get_models(),
            "urls": self._get_urls()
        }, status=status.HTTP_200_OK)
