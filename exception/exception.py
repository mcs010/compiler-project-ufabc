class IsiSemanticException(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)

class IsiSyntaxException(IsiSemanticException):
    def __init__(self, *args):
        super().__init__(*args)