import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from stores.models import Store
from users.models import User


class Command(BaseCommand):
    help = "This command creates stores"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many stores are you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        seeder.add_entity(Store, number, {"user": lambda x: random.choice(all_users)})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))
