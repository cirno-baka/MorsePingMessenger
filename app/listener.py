# coding: utf-8

import socket
from multiprocessing import Process
import sys
from .const import DEBUG,\
    MNG_EOC_MIN,\
    MNG_EOC_MAX,\
    MNG_EOM_MIN,\
    MNG_EOM_MAX,\
    DASH_MIN,\
    DASH_MAX,\
    DOT__MIN,\
    DOT__MAX


class Helper(object):
    def __init__(self):
        self._jump = False
        self._counter = 0

    @property
    def jump(self):
        if self._jump is True:
            self._jump = False
        else:
            self._jump = True
        return self._jump

    @property
    def count(self):
        print('Helper\'s count:', self._counter)
        self._counter += 1
        return None


class IcmpListener(object):
    DEBUG = DEBUG
    CHUNCK = 128  # max_local 1541
    DELTA = 61    # underlying data + headers?
    # TIMEOUT = 0.15

    def __init__(self, decoder, thread=not DEBUG):
        self.thread = thread
        self.decoder = decoder
        self.srv = Process(target=self._listen, name='IcmpListener')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        self.socket.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
        self.socket.setblocking(True)
        self.helper = Helper()

    @classmethod
    def _make_morse(cls, raw_data):
        clean_data = sys.getsizeof(raw_data) - cls.DELTA
        if cls.DEBUG:
            print('raw num', sys.getsizeof(raw_data))
            print('clean num', clean_data)
        if DOT__MIN <= clean_data <= DOT__MAX:
            return '.'
        if DASH_MIN <= clean_data <= DASH_MAX:
            return '-'
        if MNG_EOC_MIN <= clean_data <= MNG_EOC_MAX:
            return True
        if MNG_EOM_MIN <= clean_data <= MNG_EOM_MAX:
            return False

    def _decode(self, data):
        return self.decoder.decode_str(data)

    def _listen(self):
        msg = list()
        char = list()
        while True:
            data, addr = self.socket.recvfrom(self.CHUNCK)
            if not data: continue
            # to local tests activate:
            # if self.helper.jump: continue

            unknown = self._make_morse(data)

            if not unknown:
                if msg:
                    print('{}: {}'.format(
                        addr[0],
                        self._decode(msg)
                    ))
                    msg = list()
            elif unknown is True:
                if char:
                    msg.append(''.join(char))
                    char = list()
            else:
                char.append(unknown)

            if self.DEBUG:
                # self.helper.count
                print('symbol {}; char {}; msg {}'.format(unknown, char, msg))
            # sleep(self.TIMEOUT)

    def start(self):
        if self.thread:
            self.srv.start()
        else:
            self._listen()

    def stop(self):
        self.srv.terminate()

    def join(self):
        self.srv.join()






