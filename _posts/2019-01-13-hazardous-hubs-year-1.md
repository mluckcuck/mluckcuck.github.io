---
layout: post
title:  "Hazardous Hubs: Year 1"
date:   2019-01-13 10:30:01 +0000
categories: research
section: Blog
---

In a previous post I described [my job](/myJob) as a Research Associate; January is the anniversary of starting work on this project full-time, so this article gives a run-down of what I've been up to for the past year.

Some of the work has been academic publications, for the [RAIN](http://rainhub.org.uk/), [ORCA](https://orcahub.org/), and [FAIR-SPACE](https://www.fairspacehub.org/) hubs. I've also managed to arrange some workshops and tutorial for 2019. Previously I've talked about lots of fun outreach activities I've been involved in, and there are other work activities to mention too.

## Papers

In 2018 I managed to write up three papers, one of which was accepted, one is in review, and one was rejected (and is being hastily re-written!)

When I started on this job I hadn't worked on robotics or autonomous systems before; my [PhD work](/research/#thesis) focussed on [formal methods](https://shemesh.larc.nasa.gov/fm/fm-what.html) (mathematically-based techniques for the specification and modelling of software). My new colleague Marie and I (ok, ok, mostly Marie) thought it would be a good idea to write up the survey of robotics literature that we had started.

[Our survey]() formed around a few key questions we had about the application of formal methods used in autonomous or robotic systems. It became a pretty large paper, but it really helped; it gave us a nice grounding in what had already been done in the area. We submitted the paper to a journal, which rejected it initially for plagiarism. When we looked at the result, the majority of the passages that we'd 'plagiarised' were things like: one of our co-authors name's, the journal's own copyright notice, and various acronyms. Once I'd fixed these problems, we resubmitted it and it's still under review -- so we have our fingers crossed.

Next we (again, Marie and me) write a position paper, which drew on the work that went into the survey paper. During the survey, we found that many approaches using formal methods targetted one particular part of the robotic system. It seemed that this was because of the complexity of robotic systems and the range of different components that comprise them. From this, our position was that the formal methods community must work towards applying __integrated__ formal methods (combinations of several formal methods into one, which merges the benefits of each method) to robotic systems. This was accepted, and presented (by Marie) at the conference on [Integrated Formal Methods 2018]() where it won the Best Presentation award!

The final paper describes a framework for integrating different types of verification, both formal and non-formal. This is useful because each component of a robotic system might be verified in a different way (testing, model checking, simulation-based testing, theorem proving, etc). We don't want to prevent this, since each verification method is (hopefully) picked because it is the best method to tackle that particular component. So, we introduce a shared first-order logic specification that describes the system and acts like a logical prototype. This specification is used to guide the properties/tests, etc that are used by the verification methods. Unfortunately, this paper was rejected; we're reworking it now for submission to another venue. It did, however, form the basis of a recent [poster]() that I presented at an internal meeting for the [RAIN]() project.

## Workshop and Tutorials

Along Michael Fisher, I've been organising a series of workshops focussing on safety cases for robotics in the nuclear industry. Essentially, we (formal methods academics) know about the formal verification of robotic systems, but we're missing the information about the scenarios that the nuclear industry would use robots in. Neither do we know how such robotic systems would gain the certification to be allowed to operate on a nuclear site in the UK. So, we invite academic experts in verification of safety-critical systems, engineers from the nuclear industry, and representatives from the Office for Nuclear Regulation (ONR) to share information and discuss the various techniques that can be used for verify robotic systems. The key point of this series of workshops is to bring the expertise from each of the three sectors present; and work out the scenarios where robots can benefit the nuclear industry, techniques to verify them, and ways of providing evidence of this verification in safety cases so that the ONR will accept. One of these workshops has already happened, the second is planned for April 2019.

Me and Marie Farrell proposed an academic workshop, [Formal Methods for Autonomous Systems]() (FMAS), which was accepted at the [Formal Methods]() conference in 2019. This workshop will accept submitted papers and feature a discussion panel. We aim to bring together academics working on state-of-the-art formal methods for autonomous systems.

Me and Marie are also going a tutorial, at the University of York, based on [our survey paper](). It's part of the CyPhyAssure [spring school]() and will introduce people to the current state of formal methods being applied to robotic systems.

## Outreach

During the past year, I've managed to get to do some outreach work too -- which I really enjoy. Near the start of the year, I did a little bit of volunteering at a local [code club](), which I hope to continue with when I'm a little less busy. I've also been helping to run some workshops with Lego robots, alongside my colleague Louise Dennis. We've taken the [Lego Rovers]() activity to schools, the fantastic Speeke Hall for a [two day event](), and I've taken the activity to Sensor City for [Liverpool's Light Night festival]().

## Bits and Bobs

Finally, some smaller work-related things that I've been up to. After being volunteered, I've started running a twitter account for the Autonomy and Verification lab and (with help from Rafael Cardoso) building a new website for it.

The lab's [website]() is built using Jekyll, and currently runs from Github. The [Twitter account]() helps us to publicise our work and outreach activities -- hopefully. Neither of these things are __work__ in the strictest sense, but they've already given me useful experience in a bit of the background management of a research group and (again, hopefully) helped to point other researchers to our work.

## Other Sources

Other sources of information about our team at the University of Liverpool:

*  [Autonomy and Verification Laboratory](http://cgi.csc.liv.ac.uk/~matt/AVLab/)
*  [Centre for Autonomous Systems](https://www.liverpool.ac.uk/autonomous-systems/)
*  [Verification Research Group](https://www.liverpool.ac.uk/computer-science/research/artificial-intelligence/verification/)
*  [Robotics and Autonomous Systems Research Group](https://www.liverpool.ac.uk/computer-science/research/artificial-intelligence/robotics/)

Other sources of information about the project and Hubs:

*  [Robotics and AI in Nuclear (RAIN) Hub](http://rainhub.org.uk/)
  - [RAIN Hub on Twitter](https://twitter.com/@RAIN_hub)

*  [Offshore Robotics for Certification of Assets (ORCA) Hub](https://orcahub.org/)
  - [ORCA Hub on Twitter](https://twitter.com/ORCA_Hub)
  - [ORCA Hub on LinkedIn](https://www.linkedin.com/company/orca-hub/)

*  [Future AI and Robotics for Space (FAIR-SPACE) Hub](https://www.fairspacehub.org/)
  - [FAIR-SPACE on Twitter](https://twitter.com/fair_space_hub)
  - [FAIR-SPACE on LinkedIn](https://www.linkedin.com/company/fairspacehub/)
