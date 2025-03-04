class InvalidJsonException(Exception):

    
    def __init__(self, message):
        super().__init__('Invalid JSON: ' + message)
