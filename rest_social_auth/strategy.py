from social.strategies.django_strategy import DjangoStrategy


class DRFStrategy(DjangoStrategy):

    def __init__(self, storage, request=None, tpl=None):
        self.request = request
        self.session = {}
        super(DjangoStrategy, self).__init__(storage, tpl)

    def request_data(self, merge=True):
        if self.request:
            return getattr(self.request, 'auth_data', {})
        else:
            return {}

    def session_set(self, name, value):
        pass

    def session_get(self, name, default=None):
        return default
