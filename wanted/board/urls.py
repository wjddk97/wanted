from django.urls import path

from board.views import BoardDetailView, BoardView

urlpatterns = [
    path('', BoardView.as_view()),
    path('/<int:board_id>', BoardDetailView.as_view())
]