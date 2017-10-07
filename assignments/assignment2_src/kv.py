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

import networkx as nx

import sys

class KeyValue(Packet):
    name = "KeyValue"
    fields_desc = [
        LongField("preamble", 0),
        ByteField("type", 0),
        IntField("key", 0),
        IntField("value", 0),
    ]

def main():
    if len(sys.argv) != 3:
        print "Usage: kv.py [type] [parameters]"
        print "For example: kv.py get 0"
        print "             kv.py put 1 10"
        sys.exit(1)

    # TODO: implement get and put

if __name__ == '__main__':
    main()
