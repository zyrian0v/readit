from .models import Board

def board_list(request):
        boards = Board.objects.all()
        return {
                "boards": boards,
        }