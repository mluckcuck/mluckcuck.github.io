---
layout: post
title:  "Model Checking Cheat Sheet"
date:   2018-05-07 17:10:01 +0000
categories: [modelChecking]
section: Blog
---

This is a quick cheat sheet for the various model checkers that I come into contact with. It is by no means exhaustive and might be added to later. I regularly found myself looking up this information to remind myself which model-checkers do what and using which languages to describe their models and specify their properties. Writing it down in one place seemed like a good idea.

## What is Model Checking?

Model checking is a technique for verifying is a system is a _model_ for a formula; that is, the system has whatever property the formula describes. Model-Checking tools verify that a system exhibits a property by exhaustively exploring that system. This means that model-checking generally requires finite-state systems and large numbers of states can make the problem intractable. However, automatic verification without having to write proofs can be very beneficial. Model-Checking is, relatively, quick; it can expose concurrency bugs, which are difficult to find by testing; and they produce a counterexample, a chain of behaviour that leads to a state that **doesn't** exhibit the property, which is invaluable for debugging.

## Model-Checking Tools

This table shows a quick summary of the model-checking tools, the languages used to describe the models, and the languages used to specify their properties.

| Tool        | Model Language   | Property Language  |
| :------------- |:-------------:|: -----:|
| [NuSMV](http://nusmv.fbk.eu/) | Binary Decision Diagrams |  LTL or CTL |
| [SPIN](http://spinroot.com) | Promela  | LTL |
| [PRISM](http://www.prismmodelchecker.org/) | Markov chains or probabilistic timed automata | Custom language subsuming various probabilistic temporal logics|
| [UPPAAL](http://www.uppaal.org/) | Timed automata | variants of TCTL and MITL |
| [FDR](https://www.cs.ox.ac.uk/projects/fdr/) | CSPm | CSPm |
| [ProB/ProZ](https://www3.hhu.de/stups/prob/index.php/The_ProB_Animator_and_Model_Checker) | B or Z | LTL |
| [Java Pathfinder](https://github.com/javapathfinder/jpf-core/wiki) | Java | Java |


### NuSMV

[NuSMV](http://nusmv.fbk.eu/) is a reimplementation of SMV model checker using temporal logics.

* Model Language: Binary Decision Diagrams
* Property Language(S): Linear-Time Temporal Logic or Computation Tree Logic
* NuSMV2 adds SAT-based model checking
* Text-based interface
    - Interactive, and;
    - Batch

### SPIN

[SPIN](http://spinroot.com) stands for "Simple Promela Interpreter", using temporal logics.

* Model language: Promela (*Pro* cess *Me* ta *La* guage)
    - Asynchronous non-deterministic automata
    - Loosely based on Dijkstra's guarded command language
    - Borrows I/O operations from CSP
* Property Language:  Linear Temporal Logic (LTL)
* Designed for multi-threaded software
* Dynamic number of processes

### PRISM

[PRISM](http://www.prismmodelchecker.org/) is a probabilistic (and temporal logic) model checker.

* Model language(s):  PRISM modelling language, which captures:
    - Discrete-time Markov chains,
    - Continuous-time Markov chains,
    - Markov decision processes, and,
    - Probabilistic extensions of the timed automata formalism
* Property Language: PRISM's property specification language
    - Subsumes several Probabilistic temporal logics: including PCTL, CSL, probabilistic LTL and PCTL*
    - textual language, based on guarded commands
* Used for checking stochastic and temporal behaviour


### UPPAAL

[UPPAAL](http://www.uppaal.org/)  is a tool for Real-Time Systems model checking using temporal logic.

* Model Language: networks of Timed Automata
* Property Language:
    - A simplified form of Timed TCTL (for standard model checking queries – i.e. reachability, invariance, inevitability and leads-to )
    - A weighted extension of Metric Interval Temporal Logic (for Statistical Model Checking)


### FDR

[FDR](https://www.cs.ox.ac.uk/projects/fdr/) stands for Failures Divergences Refinement. it is the model checker for CSP.

* Model language: CSPm (machine-readable CSP)
* CSP process algebra, and tockCSP sections. Also has some formal programming concepts thrown in.
* Really a _refinement_ checker, to the properties are specified in CSP as well
    - Also includes basic checks for deadlock, divergence, and non-determinism
* Also includes Probe
    - CSPm animator
    - Used to be separate, but now nicely integrated


### ProB/ProZ

[ProB/ProZ](https://www3.hhu.de/stups/prob/index.php/The_ProB_Animator_and_Model_Checker) is a model checker for B (and Z) notations.

* Model language(s): B or Z specifications; also, Event-B, TLA+, CSPm, Promela
    - Z specifications are converted into B-Machines
* Essentially for State-Based systems
    - Has been extended for others
* Property Language:  Linear-Time Temporal Logic
* Checks
    - Invariants
    - Deadlocks
    - Properties in Linear-Time Temporal Logic
* Also has an animator

### Java Pathfinder

[Java Pathfinder](https://github.com/javapathfinder/jpf-core/wiki) (JPF) is a program model checker for Java programs.
It has a specialised Java Virtual Machine that executes all combinations of threads and paths through a Java program.

* Model Language: Java
* Property Language: Java
    - Set of defaults: deadlocks and unhandled exceptions
    - Allows writing "little plugins" as Java listeners to monitor JPF execution
* Not lightweight because it runs on the program
