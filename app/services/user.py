from app.services.base import BaseService
from app.repository.base import BaseRepositoryProtocol


class UserService(BaseService):
    def __init__(self, repository: BaseRepositoryProtocol):
        self.repository = repository
        super().__init__(repository=repository)
