from urllib.request import Request

# from api import settings
from django.conf import settings
from api.utils.download import download_binary_file


class RetrieveFileMixin:
    def retrieve_file(self):
        headers = settings.LAZY_REMOTE_FILE_REQUEST_HEADERS
        request = Request(self.url, headers=headers)
        return download_binary_file(request)
