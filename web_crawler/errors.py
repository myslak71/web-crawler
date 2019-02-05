class InvalidContentType(Exception):
    def __init__(self, content_type):
        self.content_type = content_type


