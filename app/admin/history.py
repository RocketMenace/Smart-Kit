from sqladmin import ModelView
from app.models.history import RequestHistory


class HistoryAdmin(ModelView, model=RequestHistory):
    column_list = [
        RequestHistory.id,
        RequestHistory.latitude,
        RequestHistory.longitude,
        RequestHistory.cadastral_number,
    ]
