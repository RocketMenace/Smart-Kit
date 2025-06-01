from sqladmin import ModelView
from app.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [User.email, User.first_name, User.last_name]
