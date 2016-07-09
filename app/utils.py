# coding: utf-8

from subprocess import Popen, PIPE
from .const import DEBUG


def sys_ping(dst: str, size: int, debug=DEBUG) -> int:
    ping = Popen(
        ['ping', '-W', '0', '-c', '1', '-s', str(size), dst],
        stderr=PIPE,
        stdin=PIPE,
        stdout=PIPE
    )
    result = ping.communicate()
    if debug:
        [print(res) for res in result]
    return ping.returncode
