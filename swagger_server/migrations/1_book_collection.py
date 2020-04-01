from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.create_collection('book')

    def downgrade(self):
        self.db['book'].drop()
