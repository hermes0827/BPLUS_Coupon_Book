import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from users.models import User
from stores.models import Store


class Command(BaseCommand):
    help = "This command creates lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many lists are you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        all_stores = Store.objects.all()
        seeder.add_entity(
            List,
            number,
            {
                "user": lambda x: random.choice(all_users),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = List.objects.get(pk=pk)
            to_add = all_stores[random.randint(0, 5) : random.randint(6, 30)]
            list_model.stores.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} lists created"))
