# coding: utf-8

from .utils import sys_ping
from .const import DEBUG,\
    MNG_EOC_AV,\
    MNG_EOM_AV,\
    DASH_AV,\
    DOT__AV


class IcmpSender(object):
    @staticmethod
    def _send__dot(dst: str, debug=DEBUG) -> None:
        size = DOT__AV
        if debug:
            print('dot', size, ':')
        sys_ping(dst, size, debug)

    @staticmethod
    def _send_dash(dst: str, debug=DEBUG) -> None:
        size = DASH_AV
        if debug:
            print('dash', size, ':')
        sys_ping(dst, size, debug)

    @staticmethod
    def _send__eoc(dst: str, debug=DEBUG) -> None:
        """management, End of char
        """
        size = MNG_EOC_AV
        if debug:
            print('eoc', size, ':')
        sys_ping(dst, size, debug)

    @staticmethod
    def _send__eom(dst: str, debug=DEBUG) -> None:
        """management, End of message
        """
        size = MNG_EOM_AV
        if debug:
            print('eom', size, ':')
        sys_ping(dst, size, debug)

    @classmethod
    def _send_symbol(cls, dst: str, symbol: str, debug=DEBUG) -> None:
        {
            '.': cls._send__dot,
            '-': cls._send_dash
        }[symbol](dst, debug)

    @classmethod
    def _send_msg(cls, dst, msg, debug=DEBUG):
        for char in msg:
            for symbol in char:
                cls._send_symbol(dst, symbol, debug)
            cls._send__eoc(dst)
        cls._send__eom(dst)

    def __init__(self, coder):
        self.coder = coder

    def send_msg(self, dst, msg, debug=DEBUG):
        if debug:
            print('original', msg)
        self._send_msg(
            dst,
            self.coder.code_str(msg)
        )





