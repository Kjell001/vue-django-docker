from django.core.management.base import BaseCommand
from app.models import Platform, Game


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **options):
        self.clear_data()
        self.create_platforms()
        self.create_games()

    def clear_data(self):
        Game.objects.all().delete()
        Platform.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Data cleared"))

    def create_platforms(self):
        platforms = ["Nintendo Switch", "PlayStation 4", "Xbox One", "PC"]
        for platform in platforms:
            Platform.objects.create(name=platform)
        self.stdout.write(self.style.SUCCESS("Platforms created"))

    def create_games(self):
        games = [
            ("The Legend of Zelda: Breath of the Wild", 2017, "Nintendo Switch"),
            ("Horizon Zero Dawn", 2017, "PlayStation 4"),
            ("Uncharted 4: A Thief's End", 2016, "PlayStation 4"),
            ("Gears of War 4", 2016, "Xbox One"),
            ("Forza Horizon 3", 2016, "Xbox One"),
            ("Overwatch", 2016, "PC"),
            ("Stardew Valley", 2016, "PC"),
        ]
        for game in games:
            title, year, platform = game
            Game.objects.create(
                title=title, year=year, platform=Platform.objects.get(name=platform)
            )
        self.stdout.write(self.style.SUCCESS("Games created"))
