import datetime
import pytest
from chess.models import ChessPlayer


@pytest.fixture
def chess_player(db):
    return ChessPlayer.objects.create(
        email='test-email@chess.pl',
        birth_date=datetime.date(year=1990, month=10, day=20),
        pesel='12345678910',
        rodo_accepted=True
    )


@pytest.fixture
def other_chess_player(db):
    return ChessPlayer.objects.create(
        email='test-email2@chess.pl',
        birth_date=datetime.date(year=1990, month=1, day=2),
        pesel='01987654321',
        rodo_accepted=True
    )