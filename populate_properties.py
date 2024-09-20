from faker import Faker
from property_service.models import Property
from user_service.models import User
import random

fake = Faker()

def create_fake_properties():
    # Предполагаем, что есть пользователи в базе данных
    user = User.objects.first()  # Убедитесь, что у вас есть хотя бы один пользователь

    if not user:
        print("В базе данных нет пользователей.")
        return

    PROPERTY_TYPES = ['apartment', 'house', 'room']

    for _ in range(20):
        title = fake.sentence(nb_words=4)
        description = fake.text(max_nb_chars=200)
        location = fake.address()
        price = round(random.uniform(50000, 500000), 2)  # Генерация случайной цены
        rooms = random.randint(1, 5)
        bathrooms = random.randint(1, 3)
        property_type = random.choice(PROPERTY_TYPES)
        amenities = {
            'WiFi': fake.boolean(),
            'Air Conditioning': fake.boolean(),
            'Swimming Pool': fake.boolean(),
            'Parking': fake.boolean(),
        }
        # Фото пока можно оставить пустым
        Property.objects.create(
            title=title,
            description=description,
            location=location,
            price=price,
            owner=user,
            rooms=rooms,
            bathrooms=bathrooms,
            property_type=property_type,
            amenities=amenities
        )

    print("Создано 20 фейковых объявлений.")
