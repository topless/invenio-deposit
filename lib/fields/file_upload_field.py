from wtforms import FileField

__all__ = ['FileUploadField']


class FileUploadField(FileField):

    def __init__(self, **kwargs):
        self._icon_html = '<i class="icon-file"></i>'
        super(FileUploadField, self).__init__(**kwargs)

    def pre_validate(self):
        return dict(error=0, error_message='')

    def autocomplete(self):
        return []
