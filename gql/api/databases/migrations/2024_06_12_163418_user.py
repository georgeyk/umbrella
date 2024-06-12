"""User Migration."""

from masoniteorm.migrations import Migration


class User(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.uuid("id")
            table.string("name", length=128)
            table.string("email", length=128)
            table.string("username", length=64)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
