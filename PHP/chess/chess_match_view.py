from .serializers import ChessMatch, ChessMatchSerializer
from rest_framework import viewsets


class ChessMatchViewSet(viewsets.ModelViewSet):
    queryset = ChessMatch.objects.all()
    serializer_class = ChessMatchSerializer
