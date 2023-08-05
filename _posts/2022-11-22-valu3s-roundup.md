---
layout: post
title:  "VALU3S Round Up"
date:   2022-11-22 17:15:19 +0000
categories: [academia]
image:  /files/logos/values-logo.png
section: Blog
---

As another post-doc job I wanted to summarise what I've been doing during this project. I did this [before]( /hubs-roundup) and I've found it very useful, I think it's helpful because it reminds me that I've not just been twiddling my thumbs and getting paid to do nothing.

For this post-doc contract I was working on the [VALU3S project](https://valu3s.eu) (or "Verification and Validation of Automated Systems’ Safety and Security" for long) which was a large EU project with a lot of universities and industrial partners in the consortium. I was working on [Use Case 5](https://repo.valu3s.eu/use-cases/aircraft-engine-controller), which was the software controller for a civilian aircraft engine. (I usually add the word "civilian", because this project is about as close as I want to come to military funding.) Our team was me, Rosemary Monahan, Marie Farrell, and 
Oisín Sheridan. 

When people ask where to start with formalising a system, I had often suggested starting with the requirements; in this project I got to take my own advice. When I started the job there was only a set of requirements, test cases, and system descriptions &ndash; a Simulink diagram would come later. So that we could make some progress, we wrote up the requirements for the [Formal Requirements Elicitation Tool (FRET)](https://github.com/NASA-SW-VnV/fret) and our work on the project centred around the interaction between these requirements and our formal modelling and verification approaches.


## FRET Requirements and Verification Methodology

Part of the work I was involved in on this project used FRET, describing the experience of translating the requirements into FRET's input language (FRETISH) and how to combine this with other formal methods.

### Papers

_"A Methodology for Developing a Verifiable Aircraft Engine Controller from Formal Requirements"_
 - IEEE Aerospace Conference: [https://ieeexplore.ieee.org/abstract/document/9843589](https://ieeexplore.ieee.org/abstract/document/9843589)
 - arXiv: [https://arxiv.org/abs/2110.09277](https://arxiv.org/abs/2110.09277)

This paper outlines our high-level methodology for using FRET and other formal methods together during the project.

The idea here was that FRET allows the user to translate requirements into contracts for Simulink diagrams or runtime monitors, and we wanted to be able to use other formalisms to model the requirements. I suppose this is another in a line of papers that I (and Marie Farrell) have written that has an _integrated_ flavour (in the sense of the integrated Formal Methods conference).  


_"FRETting about Requirements: Formalised Requirements for an Aircraft Engine Controller"_
  - REFSQ 2022: [https://link.springer.com/chapter/10.1007/978-3-030-98464-9_9](https://link.springer.com/chapter/10.1007/978-3-030-98464-9_9)
   - arXiv: [https://arxiv.org/abs/2112.04251](https://arxiv.org/abs/2112.04251)

This paper was a detailed experience report of using FRET to capture the controller's requirements, describing the requirement set, approach, and our interactions with the industrial partner. We had strayed into **Requirements Engineering** properly with this paper, and followed the authors of FRET in publishing at [Requirements Engineering: Foundation for Software Quality](https://2022.refsq.org/) (REFSQ 2022). 

As I talked about [before](/mini-mega-march#an-in-person-conference), REFSQ was my first in-person conference after _**The Event**_ and they were a very friendly community. The paper was well received, and there is some crossover with the Formal Methods community, which was helpful. 

This paper is partly exposing the research collaboration, and partly publishing the requirements set for our Use Case. We were also quite pleased that it was (as far as we knew) the first publication about FRET that wasn't written by the FRET team. 

### In FRETISH Style 

While writing up both of these papers, I made a simple LaTeX style file for typesetting the colour-coding used by FRET. It's been really useful during the project. If you would like to use or contribute to the style file, then you can find `fretish.sty` here: [https://github.com/valu3s-mu/fret-utils/blob/master/fretish.sty](https://github.com/valu3s-mu/fret-utils/blob/master/fretish.sty)


## FRET Refactoring

While working on the REFSQ paper ([https://link.springer.com/chapter/10.1007/978-3-030-98464-9_9](https://link.springer.com/chapter/10.1007/978-3-030-98464-9_9)) we found that there was a lot of repetition in the requirements. As we were developing the requriements, we were drafting up a version and then having a meeting with the industrial partner to check that our translation matched their intention. This, inevitably, meant that we had to update things as we found mistakes that we had made. The problem was that because the same behaviour was copied into multiple requirements, we had to do a lot of updates for just one change. 

This reminded me of the Software Engineering process of [refactoring](https://www.refactoring.com/), which I had first heard about during a module I took during the final year of my undergraduate degree. (As an aside, I was quite pleased about this because my undergraduate degree was not very 'academic' and had assumed that everyone would graduate and go work in tech companies or be a programmer.) 

Essentially, the point of _refactoring_ software is to improve its internal structure while leaving its external behaviour unchanged. With software, you might use the Extract Method refactoring to extract repeated bits of code into a reusable method &ndash; defining the behaviour in one location. Since FRET only has requirements, I set about performing a manual refactoring on the requirements, which I called **Extract Requirement**.  Reassuringly, I also found an existing approach that applied this to text requirements in the literature, this meant it wasn't an _entirely_ crazy idea. I wrote a slightly mess technical note describing the manual refactoring steps, which you can find [here](/files/FRET-Requirements-Refactoring.pdf).

The extra useful bit about refactoring FRETISH requirements is that we can formally compare the behaviour before and after refactoring to prove that the behaviour hasn't changed. This is achievable because FRET translates each requirement into metric temporal logic. The final step in every software refactoring is _test_, which is difficult/impossible with textual requirements; but with a representation of the requirement in formal logic, we can use existing tools to compare them.

### Paper(s)

_"Towards Refactoring FRETish Requirements"_
   - NFM 2022: [https://link.springer.com/chapter/10.1007/978-3-031-06773-0_14](https://link.springer.com/chapter/10.1007/978-3-031-06773-0_14)
   - arXiv: [https://arxiv.org/abs/2201.04531](https://arxiv.org/abs/2201.04531)

This paper was written while I was also writing up a longer paper about the manual refactoring approach, with the idea that it would eventually become automated but I wanted to test the theory of the process first. This paper in NASA Formal Methods (NFM) describes the high level idea of refactoring for requirements in FRET and discusses the repetition within our requirements set to give motivation. I was mostly focussed on the other paper; this paper got accepted and the other paper didn't.

The _on going work_ is to publish a journal paper about the refactoring process, which I have automated in a fork of FRET that I called MU-FRET ([https://github.com/valu3s-mu/mu-fret](https://github.com/valu3s-mu/mu-fret)). In Mu-FRET, the user can extract parts of a requirement to a new requirement, leaving behind a reference to 'call' the extract behaviour in the new requirement. It then checks, using [NuSMV]() that the temporal logic for the requirement before and after factoring is the same. The tool (finally) works quite nicely, and I am leading the write up of the paper for publication. (The name Mu-FRET was to reference Maynooth University, where I was working at the time; and also that mu (&#956;) is the prefix for a one millionth of something, as a sort of joke that I was only adding a tiny bit of functionality. As it turns out, it took me a lot longer than I though/hoped!)



## Formal Methods for Aerospace Systems Survey Paper

When I started this new post-doc project, Marie and I bravely/foolishly started another survey paper. This one was about the Formal Methods used in the literature to specify or verify aerospace systems. We tried to learn some lessons from our previous paper, and recruit extra help, so the team is me, Rosemary, Marie, Oisín, and Conor Reynolds. 

However, I may have overcomplicated things by insisting that we use more than just Google Scholar; so we included results from Scholar, [Microsoft Academic Search](www.academic.microsoft.com), [Bielefeld Academic Search Engine](https://www.base-search.net/), and The (COnnecting REpositories) [(CORE)](https://core.ac.uk/) system. This, combined with the variety of search terms we used, means that we are still reviewing the literature generated by the search. 

...watch this (aero)space.



## Non-VALU3S Work

There was also a strand of work that was entirely unconnected to the VALU3S project, and that was co-supervising a PhD project that I had proposed.

The project was on a list of final-year/masters projects that we showed to an incoming PhD student, [Dara MacConville
](https://orcid.org/0000-0002-2510-9446). The PhD programme that Dara is on required a short project and an industry placement in the frist year, so the list of projects we already had was the obvious starting point. I was pleased when he picked one of my project ideas. He has done a fantastic job, writing a paper and building a toolchain, with a journal paper on the way. The work is interesting, and it's personally very reassuring that the initial idea wasn't terrible.

_"Modelling the Turtle Python library in CSP"_
   - Paper: [http://dx.doi.org/10.4204/EPTCS.362.4](http://dx.doi.org/10.4204/EPTCS.362.4)
   - Zenodo Repository: [https://zenodo.org/record/6671802](https://zenodo.org/record/6671802)

This is the initial paper about the project, which was to investigate how suitable the process algebra CSP would be for specifying mobile robot behaviour. The basic idea was to start with the Turtle library in Python, which provides a simple set of 'up', 'down', 'left', 'right' commands; and then handles the graphics part of showing an agent (a small turtle, by default) on screen and making it follow the commands. This would let us focus on the instructions and the state of the agent, while ignoring simulation, sensors, etc etc. 

In this paper, we describe the approach and the model of the Turtle API. This model captures the Turtle's possible behaviours, which is combined with the user's instructions to form a specification of the behaviour. The user's instructions are checked against a description of the 'environment' (a simple grid world with a goal and optional obstacles). Dara wrote a toolchain to support this process, which accepts the description of the environment and the CSP plan of what the turtle should do, it performs the checks and (if the plan is valid for the environment) synthesises Python code to run the Turtle commands that the user specified. You should be able to try it out for yourself from the [Zenodo Repository](https://zenodo.org/record/6671802).

~~We are writing up a journal paper that describes the toolchain in more detail, which will be available soon.~~

We wrote a journal a journal paper that describes the toolchain in more detail: _"CSP2Turtle: Verified Turtle Robot Plans"_ 
 - MDPI Robotics: [https://doi.org/10.3390/robotics12020062](https://doi.org/10.3390/robotics12020062) (Open Access)

