from wtforms import DateField

__all__ = ['Date']


class Date(DateField):

    def __init__(self, **kwargs):
        self._icon_html = '<i class="icon-calendar"></i>'
        super(Date, self).__init__(**kwargs)

    def pre_validate(self):
        return dict(error=0, error_message='')

    def autocomplete(self):
        return []
