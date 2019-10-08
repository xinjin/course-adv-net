# Key-Value Store

## What is key-value store

A key-value store is a storage service. Each item in the key-value store has a key, which is the name of the item, and a value, which is the actual content of the item. A key-value store provides two basic functions: `get(key)` and `put(key, value)`. The function `get(key)` gets the value of the corresponding key from the key-value store. The function `put(key, value)` updates the value of the corresponding in the key-value store.

## What you need to do

You will implement a key-value store in the switch with P4.
To make it simple, we use the packet format below instead of a common UDP packet:
```
preamble (8 bytes) | type (1 byte) | key (4 bytes) | value (4 bytes)
```

The preamble is always set to 1. You can use this to distinguish the key-value
packets from other packets your switch may receive. We do not
guarantee that your P4 switch will exclusively receive EasyRoute packets.

The type field indicates the type of the query, which can be 0 (get request), 1 (put request), 2 (get reply), and 3 (put reply). The key and value field contains the key and value of a item, respectively.

For a `get` query, the type field should be 0 and the key field contains the key for the queried item. The value field is not meaningful. The switch should update the type field to 2, and update the value field based on the value stored in the switch. Then the switch sends the packet back to the sender as the reply.

For a `put` query, the type field should be 1, the key field should contain the key for the queried item, and the value field should contain the new value of the item. The switch should update its key-value store with the new value, update the type field to 3, and then send the packet back to the sender as the reply.

To make it simple, you can assume that the client is directly connect to the switch, and the switch simply sends the packet to the ingress port to reply to the client.

You can use part of the code in exercise1 and implement the key-value store functionality. Set the size of the key-value store in the switch to be 1000. Run kv.py in order to implement a simple client that can issue get and put queries to the switch.

## Step 1: Implementing kv_store

1. Implementing the p4 program `kv_store.p4` from scratch under the path with this README.
    **Note** primitives you may use:
    - write into a register: `<register_name>.write(<index>, <value>)`
    - read value from a register: `<register_name>.read(<value>, <index>)`
2. In your shell, run:
   ```bash
   make
   ```
   This will:
   * compile `kv_store.p4`, and
   * start a Mininet instance with one switch (`s1`), connected to one host (`h1`).

3. You should now see a Mininet command prompt. Open two terminal for
   `h1`:
   ```bash
   mininet> xterm h1 h1
   ```
4. In one xterm, send a message from the client:
   ```bash
   ./receive_kv.py
   ```
5. In the other xterm, send queries from the client:
    ```bash
    ./kv.py
    ```
6. Type `q` to exit kv.py and type `exit` to leave each xterm and
   the Mininet command line.
