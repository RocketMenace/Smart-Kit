from typing import Self
from app.repository.user import UserRepository


class AuthService:

    def __init__(self: Self, repository: UserRepository):