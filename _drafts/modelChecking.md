---
layout: post
title:  "Model Checking"
date:   2018-04-27 19:30:01 +0100
categories: introducing
---

## What Is Model Checking?

## Model Checking Tools

### SMV / NuSMV

### SPIN

SPIN stands for `Simple Promela Interpreter`

* Input language:  Promela (*Pro*cess *Me*ta *La*guage)
* Asynchronous non-deterministic autonoma
* Linear Temporal Logic (LTL) properties

### PRISM

Probablistic model checker

* Input language(s):   discrete-time Markov chains, continuous-time Markov chains, Markov decision processes and probabilistic extensions of the timed automata formalism
* Stochastic behaviours
* Probabilistic temporal logic properties

### FDR

FDR stands for Failures Divergences Refinement. CSP-Specific model checker

* Input language: CSPm (machine-readable CSP)
* CSP process algebra, and tockCSP sections. Also has some formal programming concepts thrown in.
* Really a _refinement_ checker, to the properties are specified in CSP as well
    - Also includes basic checks for deadlock, divergence, and non-determinism
  

### ProB/ProZ

Model checker for B (and Z) notations.

* Input language(s): B or Z specifications
    - Z specifications are converted into B-Machines
* State-Based systems
* Checks for deadlock...etc?

