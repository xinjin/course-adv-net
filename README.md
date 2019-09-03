# EN.601.714: Advanced Computer Networks

## Logistics

- Instructor: [Xin Jin](http://www.cs.jhu.edu/~xinjin/)
- Teaching assistants: Hang Zhu
- Lecture time: Tuesday and Thursday, 1:30-2:45pm
- Location: Hodson 316
- Office hours: Tuesday 2:45-3:45pm, Malone 233
- Credits: 3 credits
- Area for MSE and PhD requirements: Systems
- Homework submission: [Gradescope](https://www.gradescope.com/), join the course with entry code 9J4JNJ

## Course Description

This is a graduate-level course on computer networks. It provides a comprehensive overview on advanced topics in network protocols and networked systems. The course will cover both classic papers on Internet protocols and recent research results. It will examine a wide range of topics, e.g., routing, congestion control, network architectures, datacenter networks, network virtualization, software-defined networking, and programmable networks, with an emphasis on core networking concepts and principles. The course will include lectures, paper discussions, programming assignments and a research project.

## Prerequisites

One undergraduate course in computer networks (e.g., EN.601.414/614 Computer Networks or the equivalent), or permission of the instructor. The course assignments and projects assume students to be comfortable with programming.

## Announcements

- Tuesday, September 3: First day of class.

## Course Syllabus

| Date    | Topics  | Readings | Notes   |
| :------ | :------ | :------  | :------ |
| | **Classics** | | |
| Tue 09/03 | Course Overview | [How to Read](papers/CCR07_HowToRead.pdf), [You and Your Research](papers/Bell86_YouAndYourResearch.pdf) | |
| Thu 09/05 | End Host | [Packet Switching](papers/TOC74_CerfKahn.pdf), [E2E Argument](papers/TOCS84_EndToEnd.pdf) | |
| Tue 09/10 | Control Plane | [Design Philosophy](papers/SIGCOMM88_DesignPhilosophy.pdf), [E2E Routing Behavior](papers/TON97_E2ERouting.pdf) | |
| Thu 09/12 | Data Plane | [Click](papers/TOCS00_Click.pdf), [P4](papers/CCR14_P4.pdf) | [50Gbps Router](papers/TON98_50GbpsRouter.pdf), [RMT](papers/SIGCOMM13_RMT.pdf) |
| Tue 09/17 | Overlay Networks | [Chord](papers/SIGCOMM01_Chord.pdf), [CAN](papers/SIGCOMM01_CAN.pdf)  | [Pastry](papers/Middleware01_Pastry.pdf), [Tapestry](papers/JSAC04_Tapestry.pdf) |
| Thu 09/19 | Golden Age of Programmable Hardware | | |
| | **Datacenter Networking** | | |
| Tue 09/24 | Datacenter Architectures | [VL2](papers/SIGCOMM09_VL2.pdf), [Jupiter Rising](papers/SIGCOMM15_Jupiter.pdf) | [PortLand](papers/SIGCOMM09_PortLand.pdf) |
| Thu 09/26 | Optical Datacenters | [Helios](papers/SIGCOMM10_Helios.pdf), [ProjecToR](papers/SIGCOMM16_ProjecToR.pdf) | [FireFly](papers/SIGCOMM14_FireFly.pdf) |
| Tue 10/01 | Congestion Control 1 | [DCTCP](papers/SIGCOMM10_DCTCP.pdf), [pFabric](papers/SIGCOMM13_pFabric.pdf) | [PDQ](papers/SIGCOMM12_PDQ.pdf) |
| Thu 10/03 | No Class | |
| Tue 10/08 | Congestion Control 2 | NDP, HPCC | |
| Thu 10/10 | Resource Disaggregation | InfiniSwap, LegoOS |  |
| | **Software-Defined Networking** | | |
| Tue 10/15 | Control Plane | [Ethane](papers/SIGCOMM07_Ethane.pdf), [Onix](papers/OSDI10_Onix.pdf) | [FlowVisor](papers/OSDI10_FlowVisor.pdf) |
| Thu 10/17 | No Class | | |
| Tue 10/22 | Wide Area Networks | [B4](papers/SIGCOMM13_B4.pdf), [Owan](papers/SIGCOMM16_Owan.pdf) | [SWAN](papers/SIGCOMM13_SWAN.pdf) |
| | **Programmable Networks** | | |
| Thu 10/24 | Caching | SwitchKV, NetCache ||
| Tue 10/29 | Consensus | NOPaxos, Eris ||
| Thu 10/31 | Coordination and Measurement | NetChain, Sonata ||
| | **Networking Meets AI** | | |
| Tue 11/05 | AI for networking 1 | NeuroCuts, Pensieve |  |
| Thu 11/07 | AI for networking 2 | Aurora, Decima |  |
| Tue 11/12 | Networking for AI 1 | TBD | |
| Thu 11/14 | Networking for AI 2 | TBD | |
| | **Middleboxes** | | |
| Tue 11/19 | Frameworks | [E2](papers/SOSP15_E2.pdf), [NetBricks](papers/OSDI16_NetBricks.pdf) | [SIMPLE](papers/SIGCOMM13_SIMPLE.pdf) |
| Thu 11/21 | Load Balancers | [Ananta](papers/SIGCOMM13_Ananta.pdf), [SilkRoad](papers/SIGCOMM17_SilkRoad.pdf) | [Duet](papers/SIGCOMM14_Duet.pdf) |
| Tue 11/26 | Thanksgiving Vacation | | Gobble, gobble! |
| Thu 11/28 | Thanksgiving Vacation | | Gobble, gobble! |
| | **Project Presentations** | | |
| Tue 12/03 | Project presentations 1 | | |
| Thu 12/05 | Project presentations 2 | | Project Report due Mon 12/11 |

## Paper Reviews and Presentations

- Each student reviews 1 paper/class; submit reviews before the class
- Each student presents 2 papers

How to write reviews

- 4 sections in review
  - Summary
  - Paper strengths
  - Paper weaknesses
  - Detailed comments
- Summary (points in sentence or bullet form)
  - 1-2 points:  What problem?
  - 1-2 points:  Core novel ideas or technical contributions
  - 3-5 points: Summarize approach, mechanisms, findings
- Strengths/Weaknesses:  2-4 points each
- Detailed comments
  - Longer exposition. Be constructive.  Imagine conversation w/ authors:  What would you tell them?
  - May include
      - Problem: What is it? Is it new? Is it real? Is it important?
      - Solution: What is the technique(s)? Is it novel? How is it compared to past solutions? What is the intuition(s)?
      - Implementation/evaluation: Does it have a real system prototype? Is the evaluation dataset(s) representative? Does the evaluation cover all aspects?
      - Looking forward: Can you come up with a new/different/better solution? Can you find a new/related problem to solve?

## Programming Assignments

- [Assignment 1](assignments/assignment1.md): Use iperf3 and wireshark to explore TCP.
- [Assignment 2](assignments/assignment2.md): Use P4 and Mininet to design network features. ([Tutorial 1](slides/P4_tutorial.pdf), [Turorial 2](https://github.com/p4lang/tutorials/blob/master/SIGCOMM_2016/p4-tutorial-slides.pdf))

## Course Project
- Final project
  - Topic: reproduce a paper discussed in class, or novel research with a system-building component
  - Can work alone, or in groups of two students
  - Must involve writing some software
- Can overlap with other projects, with permission
  - Undergraduate research projects
  - PhD qualifying research projects
- Deliverables
  - Two-page short proposal: Oct 20
  - Project presentation: Dec 5 (last class)
  - Six-page final report: Dec 9

## Policies

### Academic Integrity Policy

This course strictly enforces the university and department policies on academic integrity. The details can be found on the [department website](https://www.cs.jhu.edu/academic-integrity-code/).

### Late Policy

25% off for each 24 hours late, rounded up

## Grading

- Class participation: 20%
- Paper reviews: 20%
- Programming assignments: 20%
- Project report and presentation: 40%

