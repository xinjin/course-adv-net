# Assignment 2

In this assignment, you will use P4 and Mininet to design network features.

## Outline

- [Introduction](#introduction)
- [Set Up Virtual Machine](#set-up-virtual-machine)
- [Source Routing](#exercise-1)
- [Key-value Store](#exercise-2)
## Deliverables

Submit your p4 code for the two exercises, in two separate folders `exercise1` and `exercise2`, and together in one
`assignment2.zip` file.

You will get full points if your code could be run successfully and generate required performance. If your code cannot
be run or doesn't have the right performance, we will first deduct half of the total points then look at your code to
assign partial credit (meaning that you will not get more than half of the credit).


## Introduction

This assignment includes 2 exercises: *Source Routing*
and *Key-Value Store*. Both exercises assume that you possess basic networking
knowledge and some familiarity with the P4 language. Please take a look at the
[P4 language spec](https://p4.org/p4-spec/docs/P4-16-v1.0.0-spec.html) and at the example `simple_router`
target [on
p4lang](https://github.com/p4lang/p4factory/tree/master/targets/simple_router/p4src).
*Source Routing* asks you to write a P4 program to implement a
custom source routing protocol. *Key-Value Store* asks you to write a P4 program to implement a key-value store in the switch. We use P4_16 in this assignment.

## Set Up Virtual Machine
The first part of this assignment is to set up the virtual machine (VM) you will use for the rest of the course. This will make it easy to install all dependencies for the programming assignments, saving you the tedium of installing individual packages and ensuring your development environment is correct.

**Note:** [step 6](#step-6) This will take about **1 hour** or even longer.

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

Run `vagrant ssh` from your terminal. This is the command you will use every time you want to access the VM. If it works, your terminal prompt will change to `vagrant@vagrant:/vagrant/`. All further commands will execute on the VM. You can then run `cd /vagrant` to get to the course directory that's shared between your regular OS and the VM.

Vagrant is especially useful because of this shared directory structure.  You don't need to copy files to and from the VM. Any file or directory in the `course-adv-net/assignments/assignment2` directory where the `Vagrantfile` is located is automatically shared between your computer and the virtual machine. This means you can use your IDE of choice from outside the VM to write your code (but will still have to build and run within the VM).

The command `logout` will stop the SSH connection at any point.

### Extra Note for Windows users

Line endings are symbolized differently in DOS (Windows) and Unix (Linux/MacOS). In the former, they are represented by a carriage return and line feed (CRLF, or "\r\n"), and in the latter, just a line feed (LF, or "\n"). Given that you ran `git pull` from Windows, git detects your operating system and adds carriage returns to files when downloading. This can lead to parsing problems within the VM, which runs Ubuntu (Unix). Fortunately, this only seems to affect the shell scripts (\*.sh files) we wrote for testing. The `Vagrantfile` is set to automatically convert all files back to Unix format, so **you shouldn't have to worry about this**. **However**, if you want to write/edit shell scripts to help yourself with testing, or if you encounter this problem with some other type of file, use the preinstalled program `dos2unix`. Run `dos2unix [file]` to convert it to Unix format (before editing/running in VM), and run `unix2dos [file]` to convert it to DOS format (before editing on Windows). A good hint that you need to do this when running from the VM is some error message involving `^M` (carriage return). A good hint you need to do this when editing on Windows is the lack of new lines. Remember, doing this should only be necessary if you want to edit shell scripts.

### Step 8: Go take a break. You've earned it!

## Exercise 1
[Source Routing](exercise1)

## Exercise 2
[Key-value Store](exercise2)
