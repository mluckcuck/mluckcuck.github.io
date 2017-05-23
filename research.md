---
layout: page
title: Research
permalink: /research/
---

My research interests include formal modelling, model checking, safety-critical systems, and programming. My PhD relates to formalising [Safety-Critical Java (SCJ)](https://www.jcp.org/en/jsr/detail?id=302) using the state-rich process algebra [_Circus_](https://www.cs.york.ac.uk/circus/), which combines elements of Z and CSP. I was supervised jointly by Professors Ana Cavalcanti and Andy Wellings at the University of York.

SCJ adopts a new programming paradigm for applications that must be certified. SCJ programs have a specific concurrent design and use region-based memory management (instead of garbage collection); specialised virtual machines are available to execute SCJ programs. It is organised into three compliance levels, of ascending complexity. My PhD focuses on the most complex compliance level, the programs of which are highly concurrent, potentially multi-processor, and make use of suspension and a variety of release patterns. My PhD provides the most complex compliance level of SCJ with its first semantics, enables further integration with other [_Circus_](https://www.cs.york.ac.uk/circus/) semantics for SCJ, and provides automatic translation from SCJ to our model.

During my PhD, my thesis work produced the following publications.

#{% bibliography %}
