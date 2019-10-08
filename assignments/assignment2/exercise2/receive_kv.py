#!/usr/bin/python
from scapy.all import sniff, sendp
from scapy.all import Packet
from scapy.all import ShortField, IntField, LongField, BitField

import sys
import struct
import pdb
def handle_pkt(pkt_in):
    pkt = str(pkt_in)
    # if len(pkt) < 12: return
    preamble = pkt[:8]
    msg_type = ord(pkt[8:9])
    key = struct.unpack(">L",pkt[9:13])[0]
    value = struct.unpack(">L",pkt[13:17])[0]
    # if msg_type < 4:
    print "msg_type:", msg_type, "\nkey:", key, "\nvalue:", value, "\n"
    print pkt_in.show()
    sys.stdout.flush()

def main():
    sniff(iface = "eth0",
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
