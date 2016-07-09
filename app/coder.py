# coding: utf-8

from .const import to_morse
from .const import DEBUG


class MorseCoder(object):
    """From txt to morse
    """
    abc = to_morse

    @classmethod
    def code_char(cls, char: str) -> str:
        return cls.abc.get(char.lower(), '')

    @classmethod
    def code_str(cls, string: str, debug=DEBUG) -> list:
        res = []
        for char in string:
            res.append(
                cls.code_char(char)
            )
        if debug:
            print('coded str', res)
        return res

    def __init__(self, lang=None):
        pass
