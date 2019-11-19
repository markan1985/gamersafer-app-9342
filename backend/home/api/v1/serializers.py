from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from allauth.account import app_settings as allauth_settings
from allauth.account.forms import ResetPasswordForm
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.serializers import PasswordResetSerializer

from home.models import CustomText, HomePage
from users.models import Preferences


 

User = get_user_model()


class SignupVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email','username', 'password','dob','country','state','face_data','first_name','last_name','face_id')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'email': {
                'required': True,
                'allow_blank': False,
            }
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

 

     



class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email','username', 'password','dob','country','state','face_data','first_name','last_name','face_id')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'email': {
                'required': True,
                'allow_blank': False,
            }
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            username=generate_unique_username([
                validated_data.get('name'),
                validated_data.get('email'),
                'user'
            ])
        )

        user.dob=validated_data.get('dob')
        user.country=validated_data.get('country')
        user.state=validated_data.get('state')
        user.face_data=validated_data.get('face_data')
        user.first_name=validated_data.get('first_name')
        user.last_name=validated_data.get('last_name')
        user.face_id=validated_data.get('face_id')



        




        user.set_password(validated_data.get('password'))
        user.save()
        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class PreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = ('interaction', 'streaming', 'playstyle', 'usagepattern', 'userid')

    def create(self, validated_data):
            preferences = Preferences()

            preferences.interaction=validated_data.get('interaction')
            preferences.streaming=validated_data.get('streaming')
            preferences.playstyle=validated_data.get('playstyle')
            preferences.usagepattern=validated_data.get('usagepattern')
            preferences.userid=validated_data.get('userid')
            preferences.save()
            request = self._get_request()
            return user
 
         
 
class UserByUserNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = User
         fields = ('id', 'name', 'email','username', 'password','dob','country','state','face_data','first_name','last_name')
        
             
               

 








class CustomTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomText
        fields = '__all__'


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','dob','country','state','face_data','first_name','last_name']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PasswordSerializer(PasswordResetSerializer):
    """Custom serializer for rest_auth to solve reset password error"""
    password_reset_form_class = ResetPasswordForm
