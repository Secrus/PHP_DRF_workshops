import pytest

from chess.serializers import ChessMatchSerializer
from chess.models import ChessPlayer


@pytest.fixture
def chess_match_request_data(
        chess_player: ChessPlayer,
        other_chess_player: ChessPlayer
):
    return {
        "start_datetime": "1990-10-10T10:10:00Z",
        "white_player": chess_player.id,
        "black_player": other_chess_player.id
    }


@pytest.mark.django_db
def test_should_pass_validation_when_all_required_data_is_supplied():
    serializer = ChessMatchSerializer(
        data=chess_match_request_data
    )
    assert serializer.is_valid() is True


@pytest.mark.parametrize('missing_data', [
    'start_datetime',
    'white_player',
    'black_player'
])
def test_should_fail_validation_when_any_of_required_data_is_missing(missing_data, chess_match_request_data):
    del chess_match_request_data[missing_data]
    serializer = ChessMatchSerializer(data=chess_match_request_data)
    assert serializer.is_valid() is False
