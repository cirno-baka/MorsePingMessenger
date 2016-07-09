#!/usr/bin/env python
# coding: utf-8

from app.coder import MorseCoder
from app.decoder import MorseDecoder
from app.listener import IcmpListener
from app.sender import IcmpSender


if __name__ == '__main__':
    print('App started')
    sender = IcmpSender(MorseCoder)
    listener = IcmpListener(MorseDecoder, thread=True)
    listener.start()
    while True:
        dst = input('Destination:')
        msg = input('Message:')
        if not (dst or msg):
            continue
        sender.send_msg(dst, msg)








