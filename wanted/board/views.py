import json
from json.decoder import JSONDecodeError

from django.http  import JsonResponse
from django.views import View

from users.models import User
from users.utils  import login_decorator
from board.models import Board

class BoardView(View):
    @login_decorator
    def post(self, request):
        try:    
            data       = json.loads(request.body)
            account_id = request.user.id
            title      = data['title']
            body       = data['body']

            Board.objects.create(
                account_id = account_id,
                title      = title,
                body       = body
            )

            return JsonResponse({'message': 'CREATE'}, status=201)
    
        except KeyError :
                return JsonResponse({'MASSAGE':'KEY_ERROR'}, status=400)
            
        except JSONDecodeError :
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)

    def get(self, request):
        offset = int(request.GET.get('offset', None))
        limit  = int(request.GET.get('limit', None))
        boards = Board.objects.all().order_by('-created_at')[offset:limit+offset]
            
        board_list = []
        for board in boards:
            board_list.append({
                'id'         : board.id,   
                'writer'     : board.account.account,
                'body'       : board.body,
                'created_at' : board.created_at.strftime('%Y.%m.%d')
            })

        return JsonResponse({'board_list':board_list}, status=200)

class BoardDetailView(View):
    @login_decorator
    def post(self, request, board_id):
        try:
            data    = json.loads(request.body)
            account = request.user
            title   = data['title']
            body    = data['body']

            if not Board.objects.filter(id=board_id).exists():
                return JsonResponse({'message':'BOARD_DOES_NOT_EXIST'}, status=404)

            board = Board.objects.get(id=board_id) 

            if account != board.account:
                return JsonResponse({'message' : 'INVALID_ACCOUNT'}, status=401)     
            
            board.title = title
            board.body  = body
            board.save()

            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError :
                return JsonResponse({'MASSAGE':'KEY_ERROR'}, status=400)
            
        except JSONDecodeError :
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)
   
    @login_decorator
    def delete(self, request, board_id):
        account = request.user
            
        if not Board.objects.filter(id=board_id).exists():
            return JsonResponse({'message' : 'BOARD_DOES_NOT_EXIST'}, status=404)

        board = Board.objects.get(id=board_id)

        if board.account != account:
            return JsonResponse({'message' : 'INVALID_ACCOUNT'}, status=401)
            
        board.delete()

        return JsonResponse({'message' : 'SUCCESS'}, status=200)

    def get(self, request, board_id):
        if not Board.objects.filter(id=board_id).exists():
            return JsonResponse({'message' : 'BOARD_DOES_NOT_EXIST'}, status=404)
            
        board = Board.objects.get(id=board_id)

        board_detail = [{
            'board_id'   : board.id,
            'writer'     : board.account.account,
            'title'      : board.title,
            'body'       : board.body,
            'created_at' : board.created_at.strftime('%Y.%m.%d')
        }]

        return JsonResponse({'board_detail': board_detail}, status=200)

