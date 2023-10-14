---
layout: page
title: Research
permalink: /research/
section: Research

---

My research interests lie in the intersection of formal software verification and safety-critical software, with a particular focus on applying formal methods to autonomous robotic systems. I am keen to do research work that also provides practical benefits, producing usable tools that support verification, development, and future research projects.

### Academic Profiles

My publication and/or reviewing records are available on the following sites.

Profiles:  <a href="https://orcid.org/{{ site.orcid_username }}"><img alt="ORCID logo" src="/files/logos/orcid_32x32.png" width="32" height="32"/></a>
  <a href="https://www.researchgate.net/profile/{{ site.researchgate_username }}"><img alt="researchgate logo" src="/files/logos/RG_square_green.png" width="32" height="32" /></a>
 <a href="https://scholar.google.co.uk/citations?user={{site.scholar_username}}"><img alt="google scholar Logo" src="/files/logos/gscholar32x32.png" width="32" height="32" /></a>
 <a href="http://dblp.uni-trier.de/pers/hd/l/{{site.dblp_username}}"><img alt="DBLP Logo" src="/files/logos/dblp2.png" width="32" height="32" /></a>


## Automated Aircraft Control Systems

My second pot-doc job was as Post-Doctoral Researcher at [Maynooth University](https://www.maynoothuniversity.ie/computer-science), Ireland. I was part of a team researching formal verification techniques for automated aircraft engine control systems, as part of the the [Verification and Validation of Automated Systems' Safety and Security (VALU3S)](https://valu3s.eu/) project. Having long told people that a good place to start with formal specification of a system is by looking at its requirements, my work on this project gave me a fantastic opportunity to do just that. A longer round-up of my work on this project can be found in a [blog post](/valu3s-roundup) I wrote.

Much of my work during this job centred on the _requirements_ for the civilian aircraft engine controller that our industrial partner had given us. We captured the requirements in [FRET](https://github.com/NASA-SW-VnV/fret) (the Formal Requirements Elicitation Tool, written by a verification team at NASA) and did a lot of collaborative with the industrial partner to make sure that our formalisation of their requirements meant what they had intended the requirements to say. In this sense, I took a step into Requirements Engineering for the first time.

Seeing that the requirements contained a lot of repetitions, I was reminded of a module on Refactoring (improving the structure of a program without changing its behaviour) that I took during my undergraduate degree. I began investigating the idea of being able to reorganise the requirements in structured way to make them easier to maintain. This idea was eventually implemented in a fork of FRET that I called [Mu-FRET](https://github.com/valu3s-mu/mu-fret), which added one refactoring. More are being added by [Oisín Sheridan](https://orcid.org/0000-0002-8613-2500).

## Autonomous Robots in Hazardous Environments

My first post-doc job was a a Research Assistant in the Department of Computer Science at the University of Liverpool (and later, the University of Manchester), working on one of the [Robotics and AI Hubs](https://www.epsrc.ac.uk/funding/calls/raihubs/). I wrote [blog post](/hubs-roundup) that gives a detailed round-up of my work during this job.

Most of my work in this job was for the [Robotics and AI in Nuclear (RAIN)](http://rainhub.org.uk/) Hub. Other colleagues were involved in the the hubs for [offshore](https://orcahub.org/), and [space](http://cgi.csc.liv.ac.uk/~michael/FAIR-SPACE-Hub/), so some of my collaborative work crossed over to those domains too. These environments are remote and hazardous to humans, so robotic systems deployed there require a high level of autonomy and rigorous verification.

My work on this project began with an extensive survey paper, and then focussed on linking heterogeneous verification approaches applied across an autonomous software system, and runtime verification of an autonomous system's behaviour. I also lead a collaboration with the UK's Office for Nuclear Regulation on developing guidance for developers of autonomous systems that ensures their systems are amenable to robust verification and can provide useful assurance evidence.

During this job I also helped setup the [research group (now network) website](https://autonomy-and-verification.github.io/) alongside [Rafael Cardoso](https://orcid.org/0000-0001-6666-6954), and was 'volunteered' to setup and run a <a href="https://twitter.com/AandVNetwork"><i class="fab fa-twitter"></i>Twitter account</a> for the group (now network). Most of the activities we did for these projects got tweeted about, and can be found under <a href="https://twitter.com/search?f=tweets&amp;q=HazardousHubs"> <i class="fab fa-twitter"></i> #HazardousHubs</a>.


## PhD Thesis

My research interests include formal modelling, model checking, safety-critical systems, and programming. My PhD relates to formalising [Safety-Critical Java (SCJ)](https://www.jcp.org/en/jsr/detail?id=302) using the state-rich process algebra [_Circus_](https://www.cs.york.ac.uk/circus/), which combines elements of Z and CSP. I was supervised jointly by Professors Ana Cavalcanti and Andy Wellings at the University of York.

SCJ adopts a new programming paradigm for applications that must be certified. SCJ programs have a specific concurrent design and use region-based memory management (instead of garbage collection); specialised virtual machines are available to execute SCJ programs. It is organised into three compliance levels, of ascending complexity. My PhD focuses on the most complex compliance level, the programs of which are highly concurrent, potentially multi-processor, and make use of suspension and a variety of release patterns. My PhD provides the most complex compliance level of SCJ with its first semantics, enables further integration with other [_Circus_](https://www.cs.york.ac.uk/circus/) semantics for SCJ, and provides automatic translation from SCJ to our model.

A copy of my PhD thesis can be found on the [White Rose repository](http://etheses.whiterose.ac.uk/17743/). The slides for my Thesis Seminar, which is a presentation of my entire thesis work given just before the final hand in, can be <a href="/files/presentations/MLuckcuck_thesisSeminar.pdf" download >downloaded here</a>

## Publications and Presentations

You can find external lists of my publications on my [dblp](http://dblp.uni-trier.de/pers/hd/l/{{site.dblp_username}}) page or my [google scholar](https://scholar.google.co.uk/citations?user={{site.scholar_username}}) page. My thesis work produced the list of publications below, which also shows links to the papers and slide (where available).

{% comment %}
Uncomment this to generate new bibliography, then copy html in below. Careful of [slide] links
{% bibliography --file msl.bib%}
{% endcomment %}

<ul class="bibliography">
<li><span id="Farrell2018">Farrell, M., Luckcuck, M., and Fisher, M. (2018). Robotics and Integrated Formal Methods: Necessity meets Opportunity. In <i>Integrated Formal Methods</i>  IFM 2018. Lecture Notes in Computer Science, vol 11023. <a href="https://doi.org/10.1007/978-3-319-98938-9_10"> https://doi.org/10.1007/978-3-319-98938-9_10 </a> <br>
Download: <a href="https://arxiv.org/pdf/1805.11996" download ><button type="button" > Paper </button></a> <a href="/files/presentations/RAS-iFM.pdf" download ><button type="button" > Slides </button></a> <a href="/files/bib/Farrell2018.bib" download ><button type="button" > Bibtex </button></a>
</span></li>

<li><span id="Luckcuck2016">Luckcuck, M., Cavalcanti, A., and Wellings, A. (2016). A Formal Model of the Safety-Critical Java Level 2 Paradigm. In <i>Proceedings of the 12th International Conference on Integrated Formal Methods - Volume 9681</i> (pp. 226–241). New York, NY, USA: Springer-Verlag New York, Inc. <a href="https://doi.org/10.1007/978-3-319-33693-0_15">http://doi.org/10.1007/978-3-319-33693-0_15</a>  <br>
Download: <a href="https://arxiv.org/pdf/1805.10711" download ><button type="button" > Paper </button></a> <a href="/files/presentations/ifm2016_formalModelForTheScjL2Paradigm.pdf" download ><button type="button" > Slides </button></a> <a href="/files/bib/Luckcuck2016_ifm.bib" download ><button type="button" > Bibtex </button></a></span></li>

<li><span id="Luckcuck2017">Luckcuck, M., Wellings, A., and Cavalcanti, A. (2017). Safety-Critical Java: level 2 in practice. <i>Concurrency and Computation: Practice and Experience</i>, <a href="https://doi.org/10.1002/cpe.3951">http://doi.org/10.1002/cpe.3951</a> <br>
Download: <a href="https://arxiv.org/pdf/1805.10710" download ><button type="button" > Paper </button></a> <a href="/files/bib/Luckcuck2016_CPE.bib" download ><button type="button" > Bibtex </button></a> </span></li>

<li><span id="Luckcuck2015">Luckcuck, M. (2015). A Formal Model for the SCJ Level 2 Paradigm. In Aichernig and B. Alessandro (Eds.), <i>Doctoral Symposium of Formal Methods 2015</i> (pp. 45–48).<br>
Download: <a href="/files/presentations/dsfm2015_formalModelForSCJL2.pdf" download ><button type="button" > Slides </button></a>
<a href="/files/bib/Luckcuck2015.bib" download > <button type="button" > Bibtex </button></a></span></li>

<li><span id="Wellings2013">Wellings, A., Luckcuck, M., and Cavalcanti, A. (2013). Safety-critical Java level 2: motivations, example applications and issues. In <i>Proceedings of the 11th International Workshop on Java Technologies for Real-time and Embedded Systems</i> (pp. 48–57). New York, NY, USA: ACM. <a href="https://doi.org/10.1145/2512989.2512991">https://doi.org/10.1145/2512989.2512991</a> <br>
Download: <a href="/files/presentations/jtres2013_usesofscjlevel2.pdf" download > <button type="button" >Slides</button></a> <a href="/files/bib/Wellings2013.bib" download ><button type="button" >Bibtex</button> </a> </span></li>

</ul>



## Other Presentations

+ [Certifiable Java for Embedded Systems (CJ4ES)](http://cj4es.imm.dtu.dk/) <br>
Download: <a href="/files/presentations/CJ4ES_modellingSscjL2InCircus.pdf" download > <button type="button" > Slides </button> </a>
+ Efficient Model Checking in FDR <br>
Download: <a href="/files/presentations/efficientModelChecking.pdf" download > <button type="button" > Slides </button> </a>
+ Using _Circus_ to Verify Safety-Critical Java Level 2 Programs <br>
Download: <a href="/files/presentations/verificationGroup.pdf" download > <button type="button" > Slides </button> </a>
