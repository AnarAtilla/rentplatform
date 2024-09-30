import factory
from faker import Faker
from property_service.models import Property
from user_service.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda _: fake.email())
    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=4))
    description = factory.LazyAttribute(lambda _: fake.text())
    location = factory.LazyAttribute(lambda _: fake.address())
    price = factory.LazyAttribute(lambda _: fake.pydecimal(left_digits=5, right_digits=2, positive=True))
    owner = factory.SubFactory(UserFactory)
    rooms = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=5))
    bathrooms = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=3))
    property_type = factory.LazyAttribute(lambda _: fake.random_element(elements=['apartment', 'house', 'room']))
    amenities = factory.LazyAttribute(lambda _: {"wifi": True, "parking": True})
