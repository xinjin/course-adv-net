# Assignment 2

In this assignment, you will use P4 and Mininet to design network features.

## Outline

- [Introduction](#introduction)
- [Set Up Virtual Machine](#set-up-virtual-machine)
- [Exercise 1: Source Routing](#exercise-1-source-routing)
  - [Description of the EasyRoute protocol](#description-of-the-easyroute-protocol)
  - [A few hints](#a-few-hints)
  - [Populating the tables](#populating-the-tables)
  - [Testing your code](#testing-your-code)
  - [Debugging your code](#debugging-your-code)
- [Exercise 2: Key-Value Store](#exercise-2-key-value-store)
  - [What is key-value store](#what-is-key-value-store)
  - [What you need to do](#what-you-need-to-do)

## Deliverables

Submit your source code for the two exercises, in two separate folders `exercise1` and `exercise2`, and together in one
`assignment2.zip` file. Please provide a `README.txt` file for each exercise in their corresponding folder describing any
specific instructions needed to run your code. We will run your code exactly in the `assignment2_src` directory of this
course repository (as described in the **NOTE** in the exercise 1 part below) with only the files you provided adding to
the right place or replacing the original files there, so please make sure to submit **all** and **only** the code files
you generated or modified and make sure they work well in the right place.

You will get full points if your code could be run successfully and generate required performance. If your code cannot
be run or doesn't have the right performance, we will first deduct half of the total points then look at your code to
assign partial credit (meaning that you will not get more than half of the credit).


## Introduction

This assignment includes 2 exercises: *Source Routing*
and *Key-Value Store*. Both exercises assume that you possess basic networking
knowledge and some familiarity with the P4 language. Please take a look at the
[P4 language spec](http://p4.org/spec/) and at the example `simple_router`
target [on
p4lang](https://github.com/p4lang/p4factory/tree/master/targets/simple_router/p4src).
*Source Routing* asks you to write a P4 program to implement a
custom source routing protocol. *Key-Value Store* asks you to write a P4 program to implement a key-value store in the switch. We use P4_14 in this assignment.

## Set Up Virtual Machine
The first part of this assignment is to set up the virtual machine (VM) you will use for the rest of the course. This will make it easy to install all dependencies for the programming assignments, saving you the tedium of installing individual packages and ensuring your development environment is correct.

**Note:** [step 6](#step-6)This will take about **1 hour** or even longer.

### Step 1: Install Vagrant
Vagrant is a tool for automatically configuring a VM using instructions given in a single "Vagrantfile."

**macOS & Windows:** You need to install Vagrant using the correct download link for your computer here: https://www.vagrantup.com/downloads.html.

**Windows only**: You will be asked to restart your computer at the end of the installation. Click Yes to do so right away, or restart manually later,
but don't forget to do so or Vagrant will not work!

**Linux:** First, make sure your package installer is up to date by running the command `sudo apt-get update`. To install Vagrant, you must have the "Universe" repository on your computer; run `sudo apt-add-repository universe` to add it. Finally, run `sudo apt-get install vagrant` to install vagrant.

### Step 2: Install VirtualBox
VirtualBox is a VM provider (hypervisor).

**macOS & Windows:** You need to install VirtualBox using the correct download link for your computer here: https://www.virtualbox.org/wiki/Downloads. The links are under the heading "VirtualBox 5.x.x platform packages."

**Windows only:** Use all the default installation settings, but you can uncheck the "Start Oracle VirtualBox 5.x.x after installation" checkbox.

**Linux:** Run the command `sudo apt-get install virtualbox`.

**Note:** This will also install the VirtualBox application on your computer, but you should never need to run it, though it may be helpful (see Step 6).

### Step 3: Install Git (and SSH-capable terminal on Windows)
Git is a distributed version control system.

**macOS & Windows:** You need to install Git using the correct download link for your computer here: https://git-scm.com/downloads.

**macOS only:** Once you have opened the .dmg installation file, you will see a Finder window including a .pkg file, which is the installer. Opening this normally may give you a prompt saying it can't be opened because it is from an unidentified developer. To override this protection, instead right-click on thet .pkg file and select "Open". This will show a prompt asking you if you are sure you want to open it. Select "Yes". This will take you to the (straightforward) installation.

**Windows only:** You will be given many options to choose from during the installation; using all the defaults will be sufficient for this course (you can uncheck "View release notes" at the end). The installation includes an SSH-capable Bash terminal usually located at `C:\Program Files\Git\bin\bash.exe`. You should use this as your terminal in this class, unless you prefer another SSH-capable terminal (the command prompt will not work). Feel free to create a shortcut to it; copying and pasting the executable somewhere else will not work, however.

**Linux:** `sudo apt-get install git`.

### Step 4: Install X Server
You will need an X Server to input commands to the virtual machine.

**macOS:** Install [XQuartz](https://www.xquartz.org/). You will need to log out and log back in to complete the installation (as mentioned by the prompt at the end).

**Windows:** Install [Xming](https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download). Use default options and uncheck "Launch Xming" at the end.

**Linux:** The X server is pre-installed!

### Step 5: Clone course Git repository
Open your terminal (use the one mentioned in step 3 if using Windows) and `cd` to wherever you want to keep files for this course on your computer.  

Run `git clone https://github.com/xinjin/course-adv-net` to download the course files from GitHub.

`cd course-adv-net/assignments/assignment2` to enter the course assignment directory.

### Step 6: Provision virtual machine using Vagrant
From the `course-adv-net/assignments/assignment2` directory you just entered, run the command  `vagrant up` to start the VM and  provision it according to the Vagrantfile. You will likely have to wait several minutes. You may see warnings/errors in red, such as "default: stdin: is not a tty", but you shouldn't have worry about them.

**Note 1**: The following commands will allow you to stop the VM at any point (such as when you are done working on an assignment for the day):
* `vagrant suspend` will save the state of the VM and stop it.
* `vagrant halt` will gracefully shutdown the VM operating system and power down the VM.
* `vagrant destroy` will remove all traces of the VM from your system. If you have important files saved on the VM (like your assignment solutions) **DO NOT** use this command.

Additionally, the command `vagrant status` will allow you to check the status of your machine in case you are unsure (e.g. running, powered off, saved...).
You must be in some subdirectory of the directory containing the Vagrantfile to use any of the commands above, otherwise Vagrant will not know which VM you are referring to.

**Note 2**: The VirtualBox application that was installed in Step 2 provides a visual interface as an alternative to these commands, where you can see the status of your VM and power it on/off or save its state. It is not recommended to use it, however, since it is not integrated with Vagrant, and typing commands should be no slower. It is also not an alternative to the initial `vagrant up` since this creates the VM.

### Step 7: Test SSH to VPN

Run `vagrant ssh` from your terminal. This is the command you will use every time you want to access the VM. If it works, your terminal prompt will change to `vagrant@vagrant:~$`. All further commands will execute on the VM. You can then run `cd /vagrant` to get to the course directory that's shared between your regular OS and the VM.

Vagrant is especially useful because of this shared directory structure.  You don't need to copy files to and from the VM. Any file or directory in the `course-adv-net/assignments/assignment2` directory where the `Vagrantfile` is located is automatically shared between your computer and the virtual machine. This means you can use your IDE of choice from outside the VM to write your code (but will still have to build and run within the VM).

The command `logout` will stop the SSH connection at any point.

### Extra Note for Windows users

Line endings are symbolized differently in DOS (Windows) and Unix (Linux/MacOS). In the former, they are represented by a carriage return and line feed (CRLF, or "\r\n"), and in the latter, just a line feed (LF, or "\n"). Given that you ran `git pull` from Windows, git detects your operating system and adds carriage returns to files when downloading. This can lead to parsing problems within the VM, which runs Ubuntu (Unix). Fortunately, this only seems to affect the shell scripts (\*.sh files) we wrote for testing. The `Vagrantfile` is set to automatically convert all files back to Unix format, so **you shouldn't have to worry about this**. **However**, if you want to write/edit shell scripts to help yourself with testing, or if you encounter this problem with some other type of file, use the preinstalled program `dos2unix`. Run `dos2unix [file]` to convert it to Unix format (before editing/running in VM), and run `unix2dos [file]` to convert it to DOS format (before editing on Windows). A good hint that you need to do this when running from the VM is some error message involving `^M` (carriage return). A good hint you need to do this when editing on Windows is the lack of new lines. Remember, doing this should only be necessary if you want to edit shell scripts.

### Step 8: Go take a break. You've earned it!

## Exercise 1: Source Routing

Place yourself in the `assignment2_src` directory [here](https://github.com/xinjin/course-adv-net/tree/master/assignments/assignment2/assignment2_src).

In this problem, we will implement a very simple source routing protocol in
P4. We will call this protocol EasyRoute. You will be designing the P4 program
from scratch. To test your implementation, a Mininet network needs to be
established to allow messages being sent between hosts, which is already implemented
and provided for you by topo.py.

Your job is
1. implementing the parser and the ingress control flow in the provided
skeleton program:
[source_routing.p4](https://github.com/xinjin/course-adv-net/blob/master/assignments/assignment2_src/p4src/source_routing.p4);
2. filling the `commands.txt` file with necessary commands.


### Description of the EasyRoute protocol

The EasyRoute packets looks like this:

```
preamble (8 bytes) | num_valid (4 bytes) | port_1 (1 byte) | port_2 (1 byte) |
... | port_n (1 byte) | payload
```

The preamble is always set to 0. You can use this to distinguish the EasyRoute
packets from other packets (Ethernet frames) your switch may receive. We do not
guarantee that your P4 switch will exclusively receive EasyRoute packets.

The num_valid field indicates the number of valid ports in the header. If your
EasyRoute packet is to traverse 3 switches, num_valid will initially be set to
3, and the port list will be 3 byte long. When a switch receives an EasyRoute
packet, the first port of the list is used to determine the outgoing port for
the packet. num_valid is then decremented by 1 and the first port is removed
from the list.

We will use the EasyRoute protocol to send text messages. The payload will
therefore correspond to the text message we are sending. You do not have to
worry about the encoding of the text message.

![Source Routing topology](../figures/source_routing_topology.png)

If I wish to send message "Hello" from h1 to h3, the EasyRoute packet will look
like this:

- when it leaves h1:
`00000000 00000000 | 00000002 | 03 | 01 | Hello`

- when it leaves sw1:
`00000000 00000000 | 00000001 | 01 | Hello`

- when it leaves sw3:
`00000000 00000000 | 00000000 | Hello`

Note that the last switch should not remove the EasyRoute header; otherwise the
application running in the end hosts won’t be able to handle incoming packets
properly.

Your P4 implementation needs to adhere to the following requirements:

1. **all non-EasyRoute packets should be dropped**
2. **if a switch receives an EasyRoute packet for which num_valid is 0, the
packet should be dropped**

### A few hints

1. in the start parse state, you can use `current()` to check if the packet is
an EasyRoute packet. A call to `current(0, 64)` will examine the first 64 bits
of the packet, **without shifting the packet pointer**.
2. do not forget that a table can match on the validity of a header. Furthermore
if a header is not valid, our software switch will set all its fields to 0.
3. a table can "match" on an empty key, which means the default action will
always be executed - if configured correctly by the runtime. Just omit the
"reads" attribute to achieve this.
4. you can remove a header with a call to `remove_header()`
5. when parsing the EasyRoute header, you do not have to parse the whole port
list. Actually P4 is currently missing language constructs needed to parse a
general Type-Length-Value style header<sup>[1](#myfootnote1)</sup>, and hence
you’ll need to simply extract the first port of the list and ignore the rest
(including the payload). Also preamble, num_valid and the port number don't have
to all be placed in the same header type.
6. finally, we advise you to put all your logic in the ingress control flow and
leave the egress empty. You will not need more than 1 or 2 tables to implement
EasyRoute.

<a name="myfootnote1">1</a>: Members of [P4.org](http://p4.org) are working
together to come up with language constructs needed to be able to parse
TLV-style headers soon.

### Populating the tables

Once your P4 code is ready (you can validate it easily by running `p4-validate`
on it), you need to think about populating the tables. We made it easy for you:
you just have to fill the commands.txt file with `bmv2` CLI commands. We think
that you only need to know 2 commands:

- `table_set_default <table_name> <action_name> [action_data]`: this is used to
set the default action of a given table
- `table_add <table_name> <action_name> <match_fields> => [action_data]`: this
is used to add an entry to a table

### Testing your code

`./run_sr.sh` will compile your code and create the Mininet network described
above. It will also use commands.txt to configure each one of the switches.
Once the network is up and running, you should type the following in the Mininet
CLI:

- `xterm h1`
- `xterm h3`

This will open a terminal for you on h1 and h3.

On h3 run: `./receive.py`.

On h1 run: `./send.py h1 h3`.

You should then be able to type messages on h1 and receive them on h3. The
`send.py` program finds the shortest path between h1 and h3 using Dijkstra, then
send correctly-formatted packets to h3 through s1 and s3.

**Note** `chmod +x <file_name>` will make your scripts executable.

### Debugging your code

.pcap files will be generated for every interface (9 files: 3 for each of the 3
switches). You can look at the appropriate files and check that your packets are
being processed correctly.

## Exercise 2: Key-Value Store

### What is key-value store

A key-value store is a storage service. Each item in the key-value store has a key, which is the name of the item, and a value, which is the actual content of the item. A key-value store provides two basic functions: `get(key)` and `put(key, value)`. The function `get(key)` gets the value of the corresponding key from the key-value store. The function `put(key, value)` updates the value of the corresponding in the key-value store.

### What you need to do

You will implement a key-value store in the switch with P4. The key-value packets may look like this:
```
preamble (8 bytes) | num_valid (4 bytes) | port (1 byte) | type (1 byte)
| key (4 bytes) | value (4 bytes)
```

The preamble is always set to 1. You can use this to distinguish the key-value
packets from other packets (EasyRoute packets and Ethernet frames) your switch may receive. We do not
guarantee that your P4 switch will exclusively receive EasyRoute packets.

The type field indicates the type of the query, which can be 0 (get request), 1 (put request), 2 (get reply), and 3 (put reply). The key and value field contains the key and value of a item, respectively.

For a `get` query, the type field should be 0 and the key field contains the key for the queried item. The value field is not meaningful. The switch should update the type field to 2, and update the value field based on the value stored in the switch. Then the switch sends the packet back to the sender as the reply.

For a `put` query, the type field should be 1, the key field should contain the key for the queried item, and the value field should contain the new value of the item. The switch should update its key-value store with the new value, update the type field to 3, and then send the packet back to the sender as the reply.

To make it simple, you do not need to implement sophisticated routing in this assignment. You can assume that the client is directly connect to the switch, and the switch simply sends the packet to the ingress port to reply to the client.

You can use part of the code in EasyRoute and implement the key-value store functionality. Set the size of the key-value store in the switch to be 1000. You need to modify the kv.py in order to implement a simple client that can issue get and put queries to the switch.

Your job is
1. implementing a p4 program that realizes key-value store.
2. (optional) filling the `commands.txt` file with necessary commands.
2. writing a python script `kv.py` that sends key-value requests, displays the requests on the screen, receives reply and displays reply messages on the screen.


### Performance requirement

1. Do not modify the topology used in exercise 1. Run the key-value store process on host 1 and switch 1.
2. `./run_kv.sh` and then open a terminal on host 1 with `xterm h1` and run `./kv.py`, you should be able to issue the `get` and `put` query with commands `put [key] [value]` and `get [key]`, for example `put 1 11` and `get 1`.
3. You should receive reply messages from switch 1 on host 1 and display the type, key and value fields in each reply
message.

### Hints

1. You could just implement kv.py with a modified version of send.py.
2. You can assume the key and value are both integers, and use key as the array index to access register.
