from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class NartCaseTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.username

        return token