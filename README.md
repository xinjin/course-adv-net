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

- Tuesday, November 19: Sign up for project presentations [here](https://docs.google.com/spreadsheets/d/1UUT69h7W5EqzjCecCH68ubv9eu29a6h0EKkMJLpjVKs/edit?usp=sharing).
- Thursday, September 12: Sign up for paper presentations [here](https://docs.google.com/spreadsheets/d/1UUT69h7W5EqzjCecCH68ubv9eu29a6h0EKkMJLpjVKs/edit?usp=sharing).
- Tuesday, September 3: First day of class.

## Course Syllabus

| Date    | Topics  | Readings | Notes   |
| :------ | :------ | :------  | :------ |
| | **Classics** | | |
| Tue 09/03 | Course Overview | [How to Read](papers/CCR07_HowToRead.pdf), [You and Your Research](papers/Bell86_YouAndYourResearch.pdf) | |
| Thu 09/05 | End Host | [Packet Switching](papers/TOC74_CerfKahn.pdf), [E2E Argument](papers/TOCS84_EndToEnd.pdf) | |
| Tue 09/10 | Control Plane | [Design Philosophy](papers/SIGCOMM88_DesignPhilosophy.pdf), [E2E Routing Behavior](papers/TON97_E2ERouting.pdf) | |
| Thu 09/12 | Data Plane | [Click](papers/TOCS00_Click.pdf), [P4](papers/CCR14_P4.pdf) | [50Gbps Router](papers/TON98_50GbpsRouter.pdf), [RMT](papers/SIGCOMM13_RMT.pdf) |
| Tue 09/17 | Overlay Networks | [Chord](papers/SIGCOMM01_Chord.pdf), [CAN](papers/SIGCOMM01_CAN.pdf)  | [Pastry](papers/Middleware01_Pastry.pdf), [ToR](papers/Security04_ToR.pdf) |
| Thu 09/19 | The Big Picture | [GoldenAge](papers/CACM19_GoldenAge.pdf), [Microseconds](papers/CACM17_Microseconds.pdf) | [TuringAward'17 Lecture](https://www.youtube.com/watch?v=3LVeEjsn8Ts) |
| | **Datacenter Networking** | | |
| Tue 09/24 | Datacenter Architectures | [VL2](papers/SIGCOMM09_VL2.pdf), [Jupiter Rising](papers/SIGCOMM15_Jupiter.pdf) | [PortLand](papers/SIGCOMM09_PortLand.pdf); Assingment 1 is out |
| Thu 09/26 | Optical Datacenters | [Helios](papers/SIGCOMM10_Helios.pdf), [ProjecToR](papers/SIGCOMM16_ProjecToR.pdf) | [FireFly](papers/SIGCOMM14_FireFly.pdf)|
| Tue 10/01 | Congestion Control 1 | [DCTCP](papers/SIGCOMM10_DCTCP.pdf), [pFabric](papers/SIGCOMM13_pFabric.pdf) | [PDQ](papers/SIGCOMM12_PDQ.pdf) |
| Thu 10/03 | Assignment 1 | | Assignment 1 due on Monday, October 7 |
| Tue 10/08 | Congestion Control 2 | [NDP](papers/SIGCOMM17_NDP.pdf), [HPCC](papers/SIGCOMM19_HPCC.pdf) | |
| Thu 10/10 | Resource Disaggregation | [InfiniSwap](papers/NSDI17_InfiniSwap.pdf), [LegoOS](papers/OSDI18_LegoOS.pdf) |  Assingment 2 is out |
| | **Software-Defined Networking** | | |
| Tue 10/15 | Control Plane | [Ethane](papers/SIGCOMM07_Ethane.pdf), [Onix](papers/OSDI10_Onix.pdf) | [FlowVisor](papers/OSDI10_FlowVisor.pdf) |
| Thu 10/17 | Assignment 2 | | Assingment 2 due on Monday, October 21 |
| Tue 10/22 | Wide Area Networks | [B4](papers/SIGCOMM13_B4.pdf), [Owan](papers/SIGCOMM16_Owan.pdf) | [SWAN](papers/SIGCOMM13_SWAN.pdf) |
| | **Programmable Networks** | | |
| Thu 10/24 | Caching | [SwitchKV](papers/NSDI16_SwitchKV.pdf), [NetCache](papers/SOSP17_NetCache.pdf) | Project proposal due on Monday, October 28 |
| Tue 10/29 | Consensus | [NOPaxos](papers/OSDI16_NOPaxos.pdf), [Eris](papers/SOSP17_Eris.pdf) ||
| Thu 10/31 | Coordination and Telemetry | [NetChain](papers/NSDI18_NetChain.pdf), [Sonata](papers/SIGCOMM18_Sonata.pdf) ||
| | **Networked Systems Meet AI** | | |
| Tue 11/05 | AI for Networked Systems 1 | [NeuroCuts](papers/SIGCOMM19_NeuroCuts.pdf), [Pensieve](papers/SIGCOMM17_Pensieve.pdf) |  |
| Thu 11/07 | AI for Networked Systems 2 | [Aurora](papers/ICML19_Aurora.pdf), [Decima](papers/SIGCOMM19_Decima.pdf) |  |
| Tue 11/12 | Networked Systems for AI 1 | [ByteScheduler](papers/SOSP19_ByteScheduler.pdf), [DGC](papers/ICLR18_DGC.pdf) | Relocated to Bloomberg 276 |
| Thu 11/14 | Networked Systems for AI 2 | [PipeDream](papers/SOSP19_PipeDream.pdf), [Nexus](papers/SOSP19_Nexus.pdf) | |
| | **Middleboxes** | | |
| Tue 11/19 | Frameworks | [E2](papers/SOSP15_E2.pdf), [NetBricks](papers/OSDI16_NetBricks.pdf) | [SIMPLE](papers/SIGCOMM13_SIMPLE.pdf) |
| Thu 11/21 | Load Balancers | [Ananta](papers/SIGCOMM13_Ananta.pdf), [SilkRoad](papers/SIGCOMM17_SilkRoad.pdf) | [Duet](papers/SIGCOMM14_Duet.pdf) |
| Tue 11/26 | Thanksgiving Vacation | | Gobble, gobble! |
| Thu 11/28 | Thanksgiving Vacation | | Gobble, gobble! |
| | **Project Presentations** | | |
| Tue 12/03 | Project presentations 1 | | |
| Thu 12/05 | Project presentations 2 | | Test demo with TA before Fri 12/06; Project Report due Mon 12/09 |

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

- [Assignment 1](assignments/assignment1/assignment1.md): Use iperf3 and wireshark to explore TCP.
- [Assignment 2](assignments/assignment2/assignment2.md): Use P4 and Mininet to design network features. ([Tutorial 1](slides/P4_tutorial.pdf), [Tutorial 2 (p4 cheat sheet)](https://drive.google.com/file/d/1Z8woKyElFAOP6bMd8tRa_Q4SA1cd_Uva/view))

## Course Project
- Final project
  - Topic: reproduce a paper discussed in class, or novel research with a system-building component
  - Can work alone, or in groups of two students
  - Must involve writing some software
- Can overlap with other projects, with permission
  - Undergraduate research projects
  - PhD qualifying research projects
- Deliverables
  - Two-page short proposal: Oct 28
  - Project presentation: Dec 3 and Dec 5
  - Six-page final report: Dec 9

## Policies

### Academic Integrity Policy

This course strictly enforces the university and department policies on academic integrity. The details can be found on the [department website](https://www.cs.jhu.edu/academic-integrity-code/).

### Late Policy

- 25% off for each 24 hours late, rounded up
- Only for assignments, not for paper reviews or project reports

## Grading

- Class participation: 20%
- Paper reviews: 20%
- Programming assignments: 20%
- Project report and presentation: 40%
