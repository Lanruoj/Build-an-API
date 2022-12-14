from main import ma

# CREATE THE Card SCHEMA WITH MARSHMALLOW, IT WILL PROVIDE SERIALISATION
class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date', 'status', 'priority')


# SINGLE CARD SCHEMA, WHEN ONE CARD NEEDS TO BE RETRIEVED
card_schema = CardSchema()
# MULTIPLE CARD SCHEMA, WHEN MULTIPLE CARDS NEED TO BE RETRIEVED
cards_schema = CardSchema(many=True)
