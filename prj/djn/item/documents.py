
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from item.models import Item
from category.models import Category

@registry.register_document
class ItemDocument(Document):
    categories = fields.NestedField(properties={
        'name_category': fields.TextField()
    })
    class Index:
        name = 'items'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Item
        fields = ['title_item', 'description_item']