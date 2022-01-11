
from generalbrowser.assets.base.clientmodel import GeneralClientModel
from generalbrowser.assets.account.clientpage import _GeneralAccountPage


class AccountClientModel(GeneralClientModel):
    _page_cls = _GeneralAccountPage

    def __init__(self, email):
        self.email = email
