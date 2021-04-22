from .models import Exercise, Profile


def create_default_exercises(sender, **kwargs):
    Exercise.objects.get_or_create(name='スクワット', exercise_type='AB', default_rep=5)
    Exercise.objects.get_or_create(name='ベンチプレス', exercise_type='A', default_rep=5)
    Exercise.objects.get_or_create(name='バーベルロウ', exercise_type='A', default_rep=5)
    Exercise.objects.get_or_create(name='ショルダープレス', exercise_type='B', default_rep=5)
    Exercise.objects.get_or_create(name='デッドリフト', exercise_type='B', default_rep=1)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
