from main import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'admin')


user_schema = UserSchema()
users_schema = UserSchema(many=True)