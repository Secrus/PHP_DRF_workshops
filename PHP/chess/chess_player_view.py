from .serializers import ChessPlayer, ChessPlayerSerializer
from rest_framework import viewsets


class ChessPlayerViewSet(viewsets.ModelViewSet):
    queryset = ChessPlayer.objects.all()
    serializer_class = ChessPlayerSerializer
