# EN.601.714: Advanced Computer Networks

## Logistics

- Instructor: [Xin Jin](http://www.cs.jhu.edu/~xinjin/)
- Teaching assistants: [Kaiyue (Karin) Wu](http://www.cnds.jhu.edu/~wooloo/)
- Lecture time: Tuesday and Thursday, 1:30-2:45pm
- Location: Malone 228
- Office hours: Tuesday 2:45-4pm, Malone 207/233
- Credits: 3 credits
- Area for MSE and PhD requirements: Systems
- Homework submission: [Gradescope](https://www.gradescope.com/), join the course with entry code MZRZK4

## Course Description

This is a graduate-level course on computer networks. It provides a comprehensive overview on advanced topics in network protocols and networked systems. The course will cover both classic papers on Internet protocols and recent research results. It will examine a wide range of topics, e.g., routing, congestion control, network architectures, datacenter networks, network virtualization, software-defined networking, and programmable networks, with an emphasis on core networking concepts and principles. The course will include lectures, paper discussions, programming assignments and a research project.

## Prerequisites

One undergraduate course in computer networks (e.g., EN.601.414/614 Computer Network Fundamentals or the equivalent), or permission of the instructor. The course assignments and projects assume students to be comfortable with programming.

## Announcements

- Monday, September 4: Sign up for paper presentations [here](https://docs.google.com/spreadsheets/d/1DwZDxOBwvyADt4WEDsYZKJS4s6wEcVM4_Pf29147_SE/edit?usp=sharing) before September 7


## Course Syllabus

| Date    | Topics  | Readings | Notes   |
| :------ | :------ | :------  | :------ |
| | **Classics** | | |
| Tue 09/05 | Course Overview | [How to Read](papers/CCR07_HowToRead.pdf), [You and Your Research](papers/Bell86_YouAndYourResearch.pdf) | |
| Thu 09/07 | End Host | [Packet Switching](papers/TOC74_CerfKahn.pdf), [E2E Argument](papers/TOCS84_EndToEnd.pdf) | |
| Tue 09/12 | Control Plane | [Design Philosophy](papers/SIGCOMM88_DesignPhilosophy.pdf), [E2E Routing Behavior](papers/TON97_E2ERouting.pdf) | |
| Thu 09/14 | Data Plane | [Click](papers/TOCS00_Click.pdf), [P4](papers/CCR14_P4.pdf) | [50Gbps Router](papers/TON98_50GbpsRouter.pdf), [RMT](papers/SIGCOMM13_RMT.pdf) |
| Tue 09/19 | No class, but work on assignment 1 and forming groups | | Assignment 1 due Mon 09/25 |
| Thu 09/21 | Overlay Networks | [Chord](papers/SIGCOMM01_Chord.pdf), [CAN](papers/SIGCOMM01_CAN.pdf)  | [Pastry](papers/Middleware01_Pastry.pdf), [Tapestry](papers/JSAC04_Tapestry.pdf) |
| | **Datacenter Networking** | | |
| Tue 09/26 | Datacenter Architectures | [VL2](papers/SIGCOMM09_VL2.pdf), [Jupiter Rising](papers/SIGCOMM15_Jupiter.pdf) | [PortLand](papers/SIGCOMM09_PortLand.pdf) |
| Thu 09/29 | Optical Datacenters | [Helios](papers/SIGCOMM10_Helios.pdf), [ProjecToR](papers/SIGCOMM16_ProjecToR.pdf) | [FireFly](papers/SIGCOMM14_FireFly.pdf) |
| Tue 10/03 | Resource Allocation | [DRF](papers/NSDI11_DRF.pdf), [Carbyne](papers/OSDI16_Carbyne.pdf) | [Varys](papers/SIGCOMM14_Varys.pdf) |
| Thu 10/05 | Congestion Control | [DCTCP](papers/SIGCOMM10_DCTCP.pdf), [pFabric](papers/SIGCOMM13_pFabric.pdf) | [PDQ](papers/SIGCOMM12_PDQ.pdf) |
| | **RDMA** | | |
| Tue 10/10 | RDMA 1 | [DCQCN](papers/SIGCOMM15_DCQCN.pdf), [RoCEv2](papers/SIGCOMM16_RoCEv2.pdf) | |
| Thu 10/12 | RDMA 2 | [Design Guidelines](papers/ATC16_RDMA.pdf), [Infiniswap](papers/NSDI17_Infiniswap.pdf) |  |
| | **Software-Defined Networking** | | |
| Tue 10/17 | SDN Control Plane | [Ethane](papers/SIGCOMM07_Ethane.pdf), [Onix](papers/OSDI10_Onix.pdf) | [FlowVisor](papers/OSDI10_FlowVisor.pdf) |
| Thu 10/19 | Wide Area Networks | [B4](papers/SIGCOMM13_B4.pdf), [Owan](papers/SIGCOMM16_Owan.pdf) | [SWAN](papers/SIGCOMM13_SWAN.pdf) |
| Tue 10/24 | Traffic Engineering | [BwE](papers/SIGCOMM15_BwE.pdf), [FFC](papers/SIGCOMM14_FFC.pdf) | [Footprint](papers/NSDI16_Footprint.pdf); Project Proposal due Mon 10/23 |
| | **Network Verification** | | |
| Thu 10/26 | No class, but work on assignment 2 | | Assignment 2 due Mon 10/30 |
| Tue 10/31 | Data Plane Verification | [HSA](papers/NSDI12_HSA.pdf), [Delta-net](papers/NSDI17_DeltaNet.pdf) | [NetPlumber](papers/NSDI13_NetPlumber.pdf), [VeriFlow](papers/NSDI13_VeriFlow.pdf), [Mutable](papers/NSDI17_Mutable.pdf) |
| Thu 11/02 | Control Plane Verification | [BatFish](papers/NSDI15_Batfish.pdf ), [Minesweeper](papers/SIGCOMM17_Minesweeper.pdf) | [Propane](papers/SIGCOMM16_Propane.pdf) |
| | **Network Measurement** | | |
| Tue 11/07 | Network Telemetry | [EverFlow](papers/SIGCOMM15_EverFlow.pdf), [Pingmesh](papers/SIGCOMM15_Pingmesh.pdf) | [NetSight](papers/NSDI14_NetSight.pdf) |
| Thu 11/09 | Sketch | [UnivMon](papers/SIGCOMM16_UnivMon.pdf), [SketchVisor](papers/SIGCOMM17_SketchVisor.pdf) | [OpenSketch](papers/NSDI13_OpenSketch.pdf) |
| | **Middleboxes** | | |
| Tue 11/14 | Frameworks | [E2](papers/SOSP15_E2.pdf), [NetBricks](papers/OSDI16_NetBricks.pdf) | [SIMPLE](papers/SIGCOMM13_SIMPLE.pdf) |
| Thu 11/16 | Load Balancers | [Ananta](papers/SIGCOMM13_Ananta.pdf), [SilkRoad](papers/SIGCOMM17_SilkRoad.pdf) | [Duet](papers/SIGCOMM14_Duet.pdf) |
| Tue 11/21 | Thanksgiving Vacation | | Gobble, gobble! |
| Thu 11/23 | Thanksgiving Vacation | | Gobble, gobble! |
| | **Networking Meets Big Data** | | |
| Tue 11/28 | Distributed Storage | [IOFlow](papers/SOSP13_IOFlow.pdf), [NetCache](http://p4.org/wp-content/uploads/2017/06/p4-ws-2017-netcache.pdf) | [SwitchKV](papers/NSDI16_SwitchKV.pdf )  |
| Thu 11/30 | Wide Area Analytics | [JetStream](papers/NSDI14_JetStream.pdf), [Clarinet](papers/OSDI16_Clarinet.pdf) | [Iridium](papers/SIGCOMM15_Iridium.pdf) |
| Tue 12/5 | Performance Modeling | [CherryPick](papers/NSDI17_CherryPick.pdf), [PARIS](papers/SOCC17_PARIS.pdf) | [Ernest](papers/NSDI16_Ernest.pdf) |
| | **Project Presentations** | | |
| Thu 12/7 | Talks by project groups | | Project Report due Mon 12/11 |

## Paper Reviews and Presentations

- Each student reviews 1 paper/class; submit reviews before the class
- Each student presents 2 papers; sign up here

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
- [Assignment 2](assignments/assignment2.md): TBD.

## Course Project
- Final project: Novel research with a system-building component
  - Open-ended research problem: Come up with your own, or talk to me
  - Can work alone or in small teams, i.e., 1-5 people
  - Must involve writing some software
- Can overlap with other projects, with permission
  - Undergraduate research projects
  - PhD qualifying research projects
- Deliverables
  - Two-page short proposal: Oct 23
  - Project presentation: Dec 7 (last class)
  - Six-page final report: Dec 11

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

