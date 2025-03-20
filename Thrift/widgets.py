from django.forms.widgets import ClearableFileInput

class MultiFileInput(ClearableFileInput):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        if attrs is not None:
            attrs['multiple'] = True
        else:
            self.attrs['multiple'] = True

    def format_value(self, value):
        """Return the file objects in a list."""
        if self.is_initial(value):
            return [value] if not isinstance(value, list) else value
        return []

    def value_from_datadict(self, data, files, name):
        """Return the list of files."""
        return files.getlist(name)