---
layout: page
title: Research
permalink: /research/
section: Research

---

### Academic Profiles

My publication and/or reviewing records are available on the following sites.

Profiles:  <a href="https://orcid.org/{{ site.orcid_username }}"><img alt="ORCID logo" src="/files/logos/orcid_32x32.png" width="32" height="32"/></a>
  <a href="https://www.researchgate.net/profile/{{ site.researchgate_username }}"><img alt="researchgate logo" src="/files/logos/RG_square_green.png" width="32" height="32" /></a>
 <a href="https://scholar.google.co.uk/citations?user={{site.scholar_username}}"><img alt="google scholar Logo" src="/files/logos/gscholar32x32.png" width="32" height="32" /></a>
 <a href="https://publons.com/a/{{ site.publons_username }}"><img alt="Publons Logo" src="/files/logos/blue_white_shadow.png" width="32" height="32" /></a>
 <a href="http://dblp.uni-trier.de/pers/hd/l/{{site.dblp_username}}"><img alt="DBLP Logo" src="/files/logos/dblp2.png" width="32" height="32" /></a>


## Autonomous Robots in Hazardous Environments

I'm Research Assistant in the [Department of Computer Science](https://www.liverpool.ac.uk/computer-science/) at the University of Liverpool, where I'm working on the Autonomous Robots in Hazardous Environments project -- details of the EPSRC grant can be found [here](https://www.epsrc.ac.uk/funding/calls/raihubs/). I am working on three separate, but related, hubs. Each hub focusses on a different hazardous environment: [nuclear](http://rainhub.org.uk/), [offshore](https://orcahub.org/), and [space](http://cgi.csc.liv.ac.uk/~michael/FAIR-SPACE-Hub/).
Such environments are remote and hazardous to humans, so robotic systems deployed there require a high level of autonomy and rigorous verification.

My post-doctoral research on this project involves the verification of autonomous robotic systems in the previously mentioned hazardous environments. I am looking at a range of techniques, including process algebraic models and temporal logic.


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
