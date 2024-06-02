from faker import Faker
from random import choice
from app import app, db
from models import Message

fake = Faker()

usernames = [fake.first_name() for _ in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    Message.query.delete()
    messages = []
    for _ in range(20):
        message = Message(
            body=fake.sentence(),
            username=choice(usernames),
        )
        messages.append(message)
    db.session.add_all(messages)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_messages()
