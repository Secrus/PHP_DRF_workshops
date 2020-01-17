from django.db import models
from django.contrib.auth.models import AbstractUser


class ChessPlayer(models.Model):
    email = models.EmailField(null=True, blank=True)
    birth_date = models.DateField()
    pesel = models.CharField(max_length=11)
    rodo_accepted = models.BooleanField()


class User(AbstractUser):
    pass


class ChessMatch(models.Model):
    AGE_CATEGORIES = (
        ("Under 20", "Under 20"),
        ("Under 30", "Under 30"),
        ("Under 40", "Under 40"),
        ("Under 50", "Under 50"),
        ("OPEN", "OPEN"),
    )
    RESULT_CHOICES = (
        ("W", "W"),
        ("B", "B"),
        ("D", "D"),
    )
    start_datetime = models.DateTimeField()
    white_player = models.ForeignKey(
        ChessPlayer,
        on_delete=models.CASCADE,
        related_name='matches_white'
    )
    black_player = models.ForeignKey(
        ChessPlayer,
        on_delete=models.CASCADE,
        related_name='matches_black'
    )

    result = models.CharField(max_length=1, choices=RESULT_CHOICES)

    age_category = models.CharField(max_length=1, choices=AGE_CATEGORIES)
