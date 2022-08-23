from main import ma
from marshmallow import fields


class CommentSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "message", "date", "user")
    user = fields.Nested("UserSchema", only=("email",))


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)