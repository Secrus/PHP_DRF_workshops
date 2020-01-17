from rest_framework import serializers
from .models import ChessPlayer, ChessMatch
from datetime import datetime
from rest_framework.validators import UniqueValidator


class ChessPlayerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    age = serializers.SerializerMethodField()
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=ChessPlayer.objects.all()),
        ]
    )

    class Meta:
        model = ChessPlayer
        fields = ['id', 'email', 'birth_date', 'pesel', 'rodo_accepted', 'age']

    def validate_pesel(self, value):

        check_sum = 1 * int(value[0]) + 3 * int(value[1]) + 7 * int(value[2]) + 9 * int(value[3]) + 1 * int(value[4]) + 3 * int(value[5]) + 7 * int(value[6])\
                    + 9 * int(value[7]) + 1 * int(value[8]) + 3 * int(value[9]) + 1 * int(value[10])
        if check_sum % 10 == 0:
            return value
        else:
            return serializers.ValidationError

    def get_age(self, obj: ChessPlayer):
        return datetime.now().year - obj.birth_date.year


class ChessMatchSerializer(serializers.ModelSerializer):
    white_player = ChessPlayerSerializer(read_only=True)
    black_player = ChessPlayerSerializer(read_only=True)

    class Meta:
        model = ChessMatch
        fields = '__all__'