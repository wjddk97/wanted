import json, bcrypt, jwt
from json.decoder import JSONDecodeError

from django.http  import JsonResponse
from django.views import View

from users.models import User
from my_settings  import SECRET_KEY, ALGORITHM


class SiupView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            account  = data['account']
            password = data['password']
        
            if User.objects.filter(account=account).exists():
                return JsonResponse({'message':'ERROR_ACCOUNT_ALREDAY_EXIST'})

            User.objects.create(
                account  = data['account'],
                password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            )

            return JsonResponse({'message':'SUCCESS'}, status=200)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERORR'})


class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            account  = data['account']
            password = data['password']

            if not User.objects.filter(account=account).exists():
                    return JsonResponse({'message': 'INVALID_USER_ID'}, status=401)
                
            user = User.objects.get(account=account)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm=ALGORITHM)
                return JsonResponse({'token':token}, status=200)
                    
            return JsonResponse({'message': 'INVALID_USER_PASSWORD'}, status=401)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'})

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
