# coding: utf-8

from .const import from_morse
from .const import DEBUG


class MorseDecoder(object):
    """From morse to txt
    """
    abc = from_morse

    @classmethod
    def decode_char(cls, char: str) -> str:
        return cls.abc.get(char.lower())

    @classmethod
    def decode_str(cls, string: list, debug=DEBUG) -> str:
        res = []
        for char in string:
            res.append(
                cls.decode_char(char)
            )
        if debug:
            print('coded str', string)
            print('decoded str', res)
        return ''.join(res)

    def __init__(self, lang=None):
        pass

