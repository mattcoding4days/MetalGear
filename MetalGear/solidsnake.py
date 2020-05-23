"""
Solid snake was made from Big Boss's genetics
"""
from bigboss import Boss

class Snake(Boss):
    """
    Since Solid Snake was derived from Big Boss,
    it only makes sense the Snake class would inherit
    from the Boss class
    """
    def __str__(self):
        return f'Hello from {self.__class__.__name__}'
