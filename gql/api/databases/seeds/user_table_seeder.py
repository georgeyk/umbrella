"""UserTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.User import User
from faker import Faker


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        fake = Faker()

        for _ in range(1000):
            profile = fake.simple_profile()
            User.create({
                "name": profile["name"],
                "email": profile["mail"],
                "username": profile["username"]
            })

