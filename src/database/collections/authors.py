from src.database import db_session
from src.database.config import DATABASE_NAME, USERNAME, PASSWORD

COLLECTION_NAME = "authors"


def main():
    if db.has_collection(COLLECTION_NAME):
        return
    authors = db.create_collection(COLLECTION_NAME)
    authors.add_hash_index(fields=["name", "surname"], unique=False)


if __name__ == "__main__":
    db_session.global_init(DATABASE_NAME, USERNAME, PASSWORD)
    db = db_session.create_session()

    main()
