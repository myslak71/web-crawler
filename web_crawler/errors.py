class InvalidContentType(Exception):
    def __init__(self, content_type):
        self.content_type = content_type

    def __str__(self):
        return f'Invalid Content-Type. Expected text/html, given {self.content_type}'

