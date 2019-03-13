#!/usr/bin/env python

import socket
from hostfileupdate import validIP

if __name__ == '__main__':
    assert validIP('0.0.0.0')
    assert validIP('1.2.3.4')
    assert validIP('10.10.10.10')
    assert validIP('255.255.255.255')
    assert not validIP('0.0.0.256')
    assert not validIP('256.0.0.0')
    assert not validIP('0.0.0')
    assert not validIP('0.0.0.')
    assert not validIP('...')
    assert not validIP('wtf?')

