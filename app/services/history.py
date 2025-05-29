from typing import Self

from app.repository.base import BaseRepositoryProtocol
from app.services.base import BaseService


class HistoryService(BaseService):
    def __init__(self: Self, repository: BaseRepositoryProtocol):
        self.repository = repository
        super().__init__(repository=repository)
