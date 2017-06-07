---
layout: page
title: Research
permalink: /research/
---


Thesis
------

My research interests include formal modelling, model checking, safety-critical systems, and programming. My PhD relates to formalising [Safety-Critical Java (SCJ)](https://www.jcp.org/en/jsr/detail?id=302) using the state-rich process algebra [_Circus_](https://www.cs.york.ac.uk/circus/), which combines elements of Z and CSP. I was supervised jointly by Professors Ana Cavalcanti and Andy Wellings at the University of York.

SCJ adopts a new programming paradigm for applications that must be certified. SCJ programs have a specific concurrent design and use region-based memory management (instead of garbage collection); specialised virtual machines are available to execute SCJ programs. It is organised into three compliance levels, of ascending complexity. My PhD focuses on the most complex compliance level, the programs of which are highly concurrent, potentially multi-processor, and make use of suspension and a variety of release patterns. My PhD provides the most complex compliance level of SCJ with its first semantics, enables further integration with other [_Circus_](https://www.cs.york.ac.uk/circus/) semantics for SCJ, and provides automatic translation from SCJ to our model.

A copy of my PhD thesis can be found on the [White Rose respository](http://etheses.whiterose.ac.uk/17307/).

Publications
------------

During my PhD, my thesis work produced the following publications.

{% comment %}
Uncomment this to generate new bibliography, then copy html in below.
{% bibliography %}
{% endcomment %}

<ol class="bibliography"><li><span id="Wellings2013">Wellings, A., Luckcuck, M., &amp; Cavalcanti, A. (2013). Safety-critical Java level 2: motivations, example applications and issues. In <i>Proceedings of the 11th International Workshop on Java Technologies for Real-time and Embedded Systems</i> (pp. 48–57). New York, NY, USA: ACM. http://doi.org/10.1145/2512989.2512991</span></li>
<li><span id="Luckcuck2015-ua">Luckcuck, M. (2015). A Formal Model for the SCJ Level 2 Paradigm. In Aichernig &amp; B. Alessandro (Eds.), <i>Doctoral Symposium of Formal Methods 2015</i> (pp. 45–48).</span></li>
<li><span id="Luckcuck2016-hp">Luckcuck, M., Wellings, A., &amp; Cavalcanti, A. (2017). Safety-Critical Java: level 2 in practice. <i>Concurrency and Computation: Practice and Experience</i>, <i>29</i>(6), e3951–n/a. http://doi.org/10.1002/cpe.3951</span></li>
<li><span id="Luckcuck2016-om">Luckcuck, M., Cavalcanti, A., &amp; Wellings, A. (2016). A Formal Model of the Safety-Critical Java Level 2 Paradigm. In <i>Proceedings of the 12th International Conference on Integrated Formal Methods - Volume 9681</i> (pp. 226–241). New York, NY, USA: Springer-Verlag New York, Inc. http://doi.org/10.1007/978-3-319-33693-0_15</span></li></ol>
