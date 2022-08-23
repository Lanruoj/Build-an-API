from main import ma
from marshmallow import fields

# CREATE THE Card SCHEMA WITH MARSHMALLOW, IT WILL PROVIDE SERIALISATION
class CardSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('id', 'title', 'description', 'date', 'status', 'priority', 'user', 'comments')
    user = fields.Nested("UserSchema", only=("email",))
    comments = fields.List(fields.Nested("CommentSchema"))


# SINGLE CARD SCHEMA, WHEN ONE CARD NEEDS TO BE RETRIEVED
card_schema = CardSchema()
# MULTIPLE CARD SCHEMA, WHEN MULTIPLE CARDS NEED TO BE RETRIEVED
cards_schema = CardSchema(many=True)
