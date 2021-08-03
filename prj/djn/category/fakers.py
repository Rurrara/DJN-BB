import factory

from category.models import Category

class CategoryFaker(factory.Factory):
    class Meta:
        model = Category
    name_category = factory.Faker('sentence', nb_words=2)
    description_category = factory.Faker('sentence', nb_words=4)