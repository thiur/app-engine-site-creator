from django.template.loader import render_to_string
from core.middleware.debug_toolbar.panels import DebugPanel

class HeaderDebugPanel(DebugPanel):
    """
    A panel to display HTTP headers.
    """
    name = 'Header'
    has_content = True
    # List of headers we want to display
    header_filter = (
        'CONTENT_TYPE',
        'HTTP_ACCEPT',
        'HTTP_ACCEPT_CHARSET',
        'HTTP_ACCEPT_ENCODING',
        'HTTP_ACCEPT_LANGUAGE',
        'HTTP_CACHE_CONTROL',
        'HTTP_CONNECTION',
        'HTTP_HOST',
        'HTTP_KEEP_ALIVE',
        'HTTP_REFERER',
        'HTTP_USER_AGENT',
        'QUERY_STRING',
        'REMOTE_ADDR',
        'REMOTE_HOST',
        'REQUEST_METHOD',
        'SCRIPT_NAME',
        'SERVER_NAME',
        'SERVER_PORT',
        'SERVER_PROTOCOL',
        'SERVER_SOFTWARE',
    )

    def nav_title(self):
        return 'HTTP Headers'

    def title(self):
        return 'HTTP Headers'

    def url(self):
        return ''

    def process_request(self, request):
        self.headers = dict(
            [(k, request.META[k]) for k in self.header_filter if k in request.META]
        )

    def content(self):
        context = {
            'headers': self.headers
        }
        return render_to_string('debug_toolbar/panels/headers.html', context)
