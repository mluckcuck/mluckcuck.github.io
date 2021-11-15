---
layout: post
title:  "Hazardous Hubs: Year 1"
date:   2019-01-13 10:30:01 +0000
categories: research
permalink: /hubs
section: Blog
---

In a previous post I described [my job](/myJob) as a Research Associate; January is the anniversary of starting work on this project full-time, so this article gives a run-down of what I've been up to for the past year.

Some of the work has been academic publications, for the [RAIN](http://rainhub.org.uk/), [ORCA](https://orcahub.org/), and [FAIR-SPACE](https://www.fairspacehub.org/) hubs. I've also managed to arrange some workshops and tutorial for 2019. Previously I've talked about lots of fun outreach activities I've been involved in, and there are other work activities to mention too.

## Papers

In 2018 I managed to write up three papers, one of which was accepted, one is in review, and one was rejected (and is being hastily re-written!)

When I started on this job I hadn't worked with robotics or autonomous systems before; my [PhD work](/research/#thesis) focussed on [formal methods](https://shemesh.larc.nasa.gov/fm/fm-what.html) (mathematically-based techniques for the specification and modelling of software) applied to safety-critical systems. There is obviously an overlap between 'safety-critical' and 'robotic' systems (a pretty big overlap) but I still had new things to learn. Since this meant a **lot** of reading, my new colleague Marie and I (ok, ok, mostly Marie) thought it would be a good idea to write a survey of robotics literature, as a useful output to all this reading.

[Our survey](https://arxiv.org/abs/1807.00048) formed around a few key questions we had about the application of formal methods used in autonomous or robotic systems. It became a pretty large paper, but it really helped; it gave us a nice grounding in what had already been done in the area. We submitted the paper to a journal, which rejected it initially for plagiarism. When we looked at the result, the majority of the passages that we'd 'plagiarised' were things like: one of our co-authors name's, the journal's own copyright notice, and various acronyms. Once I'd fixed these problems, we resubmitted it and it's still under review -- so we have our fingers crossed.

Next we (again, Marie and me) wrote a position paper, which drew on the work that went into the survey. During the survey, we found that many approaches using formal methods targetted one particular part of the robotic system. It seemed that this was because of the complexity of robotic systems, and the range of different components that they are built from. From this, our position was that the formal methods community must work towards applying __integrated__ formal methods (combinations of several formal methods into one, which merges the benefits of each method) to robotic systems. This was accepted at the conference on [Integrated Formal Methods 2018](https://ifm2018.cs.nuim.ie/). I talked about my visit to this conference in [a previous post]({{site.url}}/research/2018/09/09/mosey-to-maynooth.html), but the summary is that Marie presented our paper and won the **Best Presentation award!**

The final paper describes a framework for integrating different types of verification, both formal and non-formal. This is useful because each component of a robotic system might be verified in a different way (testing, model checking, simulation-based testing, theorem proving, etc). We don't want to prevent this, since each verification method is (hopefully) picked because it is the best method to tackle that particular component. So, we introduce a shared first-order logic specification that describes the system and acts like a logical prototype. This specification is used to guide the properties/tests, etc that are used by the verification methods. Unfortunately, this paper was rejected; we're reworking it now for submission to another venue. It did, however, form the basis of a recent [poster (pdf 645kb)]({{site.url}}/files/poster/RAIN-Poster.pdf) that I presented at an internal meeting for the [RAIN](http://rainhub.org.uk/) project.

## Workshop and Tutorials

Along with Michael Fisher, I've been organising a [series of workshops](https://autonomy-and-verification-uol.github.io/events/fnrc) focussing on how to certify robotics in the nuclear industry. The workshops bring together:
* Academics, with experience in systems verification and certification;
* Nuclear Industry Practitioners, who know tasks the robots will be doing; and,
* Representatives from the [Office for Nuclear Regulation](http://www.onr.org.uk/) (ONR), who regulate the nuclear industry in the UK.

The key point is to combine the expertise from each of these three sectors. We need to find:
* Scenarios where robots can benefit the nuclear industry,
* Techniques to verify these systems, and;
* Methods of presenting this verification to the ONR so that they can certify the system.

The first of these workshops has already happened and the second is planned for April 2019.

Me and Marie Farrell proposed an academic workshop, [Formal Methods for Autonomous Systems](https://autonomy-and-verification-uol.github.io/events/fmas) (FMAS), which was accepted at the [Formal Methods](http://formalmethods2019.inesctec.pt/) conference in 2019. This workshop will accept submitted papers and feature a discussion panel. We aim to bring together academics working on state-of-the-art formal methods for autonomous systems.

Me and Marie are also going a tutorial, at the University of York, based on our, aforementioned, [survey paper](https://arxiv.org/abs/1807.00048). It's part of the CyPhyAssure [spring school](https://www.cs.york.ac.uk/circus/CyPhyAssure/school/) and will introduce people to the current state of formal methods being applied to robotic systems.

## Outreach

During the past year, I've managed to get to do some outreach work too -- which I really enjoy. Near the start of the year, I did a little bit of volunteering at a local [Code Club](https://codeclub.org/en/), which I hope to continue with when I'm a little less busy. I've also been helping to run some workshops with Lego robots, alongside my colleague [Louise Dennis](http://cgi.csc.liv.ac.uk/~lad/). We've taken the [Lego Rovers](http://legorovers.csc.liv.ac.uk/) activity to schools, the fantastic [Speeke Hall](https://www.nationaltrust.org.uk/speke-hall-garden-and-estate) for a two day event (which I talked about [before]({{ site.url }}/outreach/2018/09/04/twinSpekes.html)), and I've taken the activity to Sensor City for [Liverpool's Light Night festival]({{ site.url }}/outreach/2018/05/09/Light-Night.html).

## Bits and Bobs

Finally, some smaller work-related things that I've been up to. After being volunteered, I've started running a twitter account for the Autonomy and Verification lab and (with help from my colleague [Rafael Cardoso](https://rafaelcaue.github.io/)) building a new website for it.

The lab's [website](https://autonomy-and-verification-uol.github.io/) is built using [Jekyll](https://jekyllrb.com/), and currently runs from Github. The [Twitter account](https://twitter.com/LivUni_AVLab) helps us to publicise our work and outreach activities -- hopefully. Neither of these things are __work__ in the strictest sense, but they've already given me useful experience in a bit of the background management of a research group and (again, hopefully) helped to point other researchers to our work.
