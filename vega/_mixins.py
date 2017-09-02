"""
Provides mixin classes.
"""
import json


class FromFileMixin(object):
    """
    Class mixin providing class initialization from file.
    """

    @classmethod
    def from_file(cls, filename, *args, mode='r', encoding=None, loader=json,
                  **kwargs):
        """
        Initializes a class from `filename` using text deserializer `loader`.

        Parameters
        ----------
        filename : unicode
            Path to a local file to load the data from.
        encoding : unicode
            Encoding of the file to load the date from.
        loader : object
            An object with a `load` method.
        """

        with open(filename, mode=mode, encoding=encoding) as file:
            data = loader.load(file)

        return cls(data, *args, **kwargs)


class FromUrlMixin(object):
    """
    Class mixin providing class initialization from a URL.
    """

    @classmethod
    def from_url(cls, url, *args, **kwargs):
        """
        Initializes a class from `filename` from given `url`.

        Parameters
        ----------
        url : unicode
            A URL to download the data from.
        """

        def _extract_encoding_from_response_header(response):
            for sub in response.headers['content-type'].split(';'):
                _sub = sub.strip()
                if _sub.startswith('charset'):
                    return _sub.split('=')[-1].strip()

        try:
            from urllib.request import urlopen, URLError
            response = urlopen(url)
            txt = response.read()
            encoding = _extract_encoding_from_response_header(response)
            data = json.loads(txt, encoding=encoding if encoding else None)
        except URLError:
            data = {}

        return cls(data, *args, **kwargs)


class FromTemplateMixin(object):
    """
    Class mixin providing class initialization from python str.format based
    template file.
    """

    @classmethod
    def from_template(cls, filename, context, *args, mode='r', encoding=None,
                      loader=json, **kwargs):
        """
        Initializes a class from a python str.format template `filename` using
        text deserializer `loader`.

        Parameters
        ----------
        filename : unicode
            Path to a local file to load the data from.
        context : dict
            Mapping with template context
        encoding : unicode
            Encoding of the file to load the date from.
        loader : object
            An object with a `load` method.
        """

        with open(filename, mode=mode, encoding=encoding) as file:
            s = file.read(encoding=encoding)
            data = loader.loads(s.format(**context))

        return cls(data, *args, **kwargs)
