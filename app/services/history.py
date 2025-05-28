from app.services.base import BaseService
from typing import Self
from app.repository.base import BaseRepositoryProtocol



class HistoryService(BaseService):
    
    def __init__(self: Self, repository: BaseRepositoryProtocol):
        self.repository = repository