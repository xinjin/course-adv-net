#!/usr/bin/python

# Copyright 2013-present Barefoot Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from scapy.all import sniff, sendp
from scapy.all import Packet
from scapy.all import ShortField, IntField, LongField, BitField, ByteField
from scapy.all import Ether, IP, UDP

import sys
import pdb
class KeyValue(Packet):
    name = "KeyValue"
    fields_desc = [
        LongField("preamble", 1),
        ByteField("mtype", 0),
        IntField("key", 0),
        IntField("value", 0),
    ]

def main():

    while(1):
        msg = raw_input("get or put or quit. eg: put 1 11, get 1, q :")
        paras = msg.split()
        # p = Ether() / IP() / UDP()
        # p = None
        if paras[0]=='put':
            #pdb.set_trace()
            p = KeyValue(mtype = 1, key = int(paras[1]), value = int(paras[2]))
            print p.show()
            sendp(p, iface = "eth0")
        elif paras[0]=='get':
            p = KeyValue(mtype = 0, key = int(paras[1]))
            print p.show()
            sendp(p, iface = "eth0")
        elif paras[0]=='q':
            break
        else:
            print "Not supported request type. Please input again"


if __name__ == '__main__':
    main()
