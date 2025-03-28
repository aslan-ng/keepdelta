---
title: 'KeepDelta: A Python Library for Human-Readable Data Differencing'

tags:
  - python
  - simulation
  - sensing
  - data structures
  - delta encoding
  - delta compression
  - data differencing
  - differential compression
  - change tracking
  - human-readable

authors:
  - name: Aslan Noorghasemi 
    orcid: 0009-0004-3387-4502
    affiliation: '1'
    corresponding: true
  - name: Christopher McComb
    orcid: 0000-0002-5024-7701
    affiliation: '1'
    corresponding: false
  
affiliations:
  - index: 1
    name: Carnegie Mellon University, Pittsburgh, PA, USA
    ror: 05x2bcf33

date: 1 January 2025
bibliography: paper.bib
---


# Summary

Efficiently managing evolving data is crucial in applications like computational simulations and sensing, where dynamic data tracking and processing are essential. In simulations, traditional methods of storing complete snapshots (full-state encoding) at each step can be highly storage intensive; in contrast, recalculating states from scratch is computationally expensive. Similarly, in sensing, continuously transmitting full data snapshots is inefficient, leading to increased bandwidth consumption and latency.
_KeepDelta_ addresses this challenge by providing a lightweight Python library that captures and applies only the changes (deltas) between successive states of complex, nested Python data structures. Designed for clarity and ease of use, KeepDelta produces human-readable outputs, facilitating debugging and analysis in research applications.


# Statement of need

High-frequency data sampling is fundamental in both scientific simulations and real-world sensing applications, where large volumes of evolving data must be efficiently managed. Both domains, whether generating synthetic data through computational models or collecting real-time measurements from physical sensors, face a common challenge: storing, transmitting, and processing dynamic data without excessive redundancy.

First and foremost, KeepDelta applies to simulation. Simulation is a widely used methodology across all applied science disciplines, offering a flexible, powerful, and intuitive tool for designing processes or systems and maximizing their efficiency [@SimulationExperiments]. Specifically, computational simulations are invaluable tools for studying complex systems and their behaviors [@ComplexSystemsSimulation]. These studies often take the form of computer experiments, where data is generated through pseudo-random sampling from known probability distributions. This approach serves as an invaluable resource for research, particularly in evaluating new methods and comparing alternative approaches [@SimulationStudies]. 

Secondly, KeepDelta also applied to sensing. Sensing technologies are employed across diverse scientific and engineering domains, enabling continuous monitoring and analysis of dynamic environments. It is common for these systems to utilize a set of sensors to capture real-time data, which is essential for studying systems behaviors, informed decision-making, and system optimization [@RemotePhysiologicalandEnvironmentalMonitoring] [@agricultureIoT].

Both simulations and sensing require mechanisms to track and store evolving states of data structures over time. In simulations, the naive approach of saving full snapshots at every timestep leads to excessive storage demands, while recalculating states from scratch is computationally expensive. Similarly, in sensing applications, continuously storing or transmitting full data snapshots is impractical, particularly in bandwidth-limited and remote environments. Instead of relying on these easy-to-implement but inefficient methods, KeepDelta introduces an optimized middle ground by saving only the _deltas_ (changes) between states, significantly reducing storage and computation overhead. This Delta Encoding technique has been successfully applied in other domains where managing evolving data efficiently is critical, such as web development [@DeltaEncodingInHTTP] and software version management [@NaiveDifferencesOfExecutableCode].

Human-readability is crucial for debugging and development in both simulation and sensing projects, and KeepDelta is tailored specifically for this purpose. It is lightweight and has no dependecies, supports native Python data structures, and generates results that are easy to interpret. This makes it an ideal tool for Python developers and researchers seeking a simple yet powerful solution for change management. By providing clear, human-readable output, KeepDelta enhances both the development process and debugging efficiency, making it easier to track and manage changes in complex projects involving both computational models and real-world sensing systems.

![Comparison of data management approaches in evolving systems. Full-state encoding incurs high storage and bandwidth costs, while delta encoding saves only changes for efficiency. Rerunning reduces storage but increases computation and is often impractical for sensing real-world data. The bottom gradients illustrate trade-offs: storage/bandwidth decrease left to right, while data loading time increases.](./assets/comparison.png)


# Comparison to Existing Tools

In the landscape of Python libraries designed for delta encoding, several notable tools have emerged, each with distinct features and applications.
xdelta3 [@xdelta3] and its predecessor, xdelta [@xdelta], are tools that perform delta encoding at the binary level. These utilities are particularly effective for binary file differencing and are widely used in version control systems and data synchronization tasks. However, both are considered outdated and are no longer actively maintained. Their operation at the binary level results in outputs that are not human-readable, and they are not tailored for Python data structures, limiting their applicability in Python-centric workflows.
deepdiff [@deepdiff] is a contemporary library that facilitates the identification of differences between complex Python data structures, including dictionaries, lists, and sets. It extends support to external libraries like NumPy [@numpy], enhancing its versatility. However, this integration can lead to outputs that are less human-readable compared to KeepDelta. Additionally, deepdiff introduces weighty dependencies that may not be necessary for all projects.
In contrast to these alternatives, KeepDelta is a lightweight Python library optimized for simulations, focusing on efficient delta management for native Python data structures. It operates directly on Python’s native data types, producing human-readable outputs that facilitate debugging and research applications. Implemented in pure Python, KeepDelta eliminates external dependencies, making it an ideal choice for Python-centric workflows, particularly in simulations and data analysis tasks.


# References