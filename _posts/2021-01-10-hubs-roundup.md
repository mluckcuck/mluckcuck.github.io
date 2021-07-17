---
layout: post
title:  "Hubs Round-Up"
date:   2021-02-06 14:06:19 +0000
categories: [academia, job-hunt, mental-health]

section: Blog
---

As I mentioned in my [last post](/post-doc-job-hop) I've been job hunting, and this month sees me starting a new job. Obviously, I'm still working from home, so nothing much has changed.

As part of leaving my current job, I've been preparing a list of where any resources (program code, verification models, etc) are located (since most of my work is stored/archived online somewhere). For this job, I've been working on the Robotics and AI Hubs that I've talked about [before](/hubs) mainly the [RAIN](http://rainhub.org.uk/) Hub.

As usual, I don't feel like I've done enough work over the past three years. I was hoping that in 2020 I could catch up and get some more things done, wrap up some of the loose ends; but the COVID-19 pandemic put paid to that. I suppose this post is mainly for my own benefit, to gather together the list of what I did for this job. I hope that having it collected in one place will help me to: a) see that I _was_ in fact productive, and b) tease out some common threads in the research I did.

One thing that is clear, is that much (if not all) of the work I've done over the last three years has been possible because of the friendships I've made and collaborations I've had with other people. Academic work is inherently collaborative.

## Survey Paper

Some of the early work I did on the [hubs](/hubs#papers) was a survey paper. This was joint work, mainly with [Marie Farrell](https://orcid.org/0000-0001-7708-3877), and I think we managed to get quite a lot out of the (admittedly large) effort we put into it.

The survey paper itself "Formal Specification and Verification of Autonomous Robotic Systems: A Survey" contains the main results, where we classified the papers we found by: the verification challenge being tackled, the type of formal method being used, and the _approach_ (model checking, theorem proving, run-time verification, etc). I wanted the ": A Survey" at the end of the name so that it wasn't yet another survey paper called "A Survey of...", though at least with that, it would have been at the top of an alphabetical list!

From the initial survey work, we also produced "A Summary of Formal Specification and Verification of Autonomous Robotic Systems", which summarised the survey; and "Robotics and Integrated Formal Methods: Necessity meets Opportunity", which is a position paper talking about why verifying robotic systems often needs the _integration_ of multiple formal methods.

These three papers are:

* "Formal Specification and Verification of Autonomous Robotic Systems: A Survey"
  - Available on [arxiv](https://arxiv.org/abs/1807.00048) and [ACM](https://dl.acm.org/doi/10.1145/3342355)

* "A Summary of Formal Specification and Verification of Autonomous Robotic Systems"
  - Available on [arxiv](https://arxiv.org/abs/1911.11597) and [Springer](https://link.springer.com/chapter/10.1007%2F978-3-030-34968-4_33)

* "Robotics and Integrated Formal Methods: Necessity meets Opportunity"
  - Available on [arxiv](https://arxiv.org/abs/1805.11996) and [Springer](https://link.springer.com/chapter/10.1007/978-3-319-98938-9_10)

## Discussion Papers and Articles

Some of the other work I've done over the past three years has been writing more 'chatty' papers or articles, more like the position paper I mentioned above.

### British Computer Society FACS FACTS Article

I wanted to write a little article about the work me and [Marie](https://orcid.org/0000-0001-7708-3877) had been doing, talking to the respective communities of the [RAIN](http://rainhub.org.uk/) and [FAIR-SPACE](https://www.fairspacehub.org/) hubs about how safety and security regulations for autonomous robotic systems might work. I had been collaborating with the Office for Nuclear Regulation (along with Michael Fisher, and more recently Louise Dennis) and Marie had recently run a [workshop](https://cgi.csc.liv.ac.uk/~marie/scopingsecwk/) involving some of the UK's space systems industry and security researchers at the University of Warwick

We wrote up a short article for the [newsletter](https://www.bcs.org/membership/member-communities/facs-formal-aspects-of-computing-science-group/newsletters/) of the British Computer Society's Formal Aspects of Computer Science group. While this wasn't a 'publication' in the usual academic sense (it wasn't peer-reviewed and it was just for a newsletter) I think it's useful. It was good practice at a slightly different style of writing, and informed other people who are interested in formal methods about what we'd been doing.

The article "Regulating Safety and Security in Autonomous Robotic Systems" is available from:
* [BCS FACS](https://www.bcs.org/media/5204/facs-dec19.pdf), and
* [arXiv](https://arxiv.org/abs/2007.08006)

### Defending Formal Methods
#### Or "Another Tool in the Box: Why use Formal Methods for Autonomous Systems?"
#### Or "Using Formal Methods for Autonomous Systems: Five Recipes for Formal Verification"

[Previously](/mega-march#Trek-to-Trondheim) I mentioned attending the [International Workshop on Autonomous System Safety](https://www.ntnu.edu/imt/iwass) in Trondheim. Mid-way through last year, they organised a special issue of the [Journal of Risk and Reliability](https://journals.sagepub.com/home/pio). I decided to expand on the paper I'd written for the proceedings of the workshop, turning it into a larger (and I hope more useful) argument in favour of using formal methods for autonomous systems.

During my (admittedly) short time researching formal methods, it seems to me that a lot of formal methods are sold as:

"we can solve all your problems!!*

\* if you change your development process and do things our way from the start"

Now, there is a lot to be said for using a good development process from the start, but during the last three years I found that most robotic/autonomous systems we came across _already existed_. So if we were asked "what can you verify about this system?" is seemed a bit petulant to reply "here's how you can _redevelop_ your system....does that help?"

I became interested in what approaches we could use on existing systems, systems that are often not designed or developed with the consideration of formal verification. While this paper does present some recommendations for the design of a system (processes, architecture, etc), it also tries to show off techniques that could be used after a system has been built (like runtime verification) or how including formal methods in parts of the system's development can still be really useful.

I realise that this idea is not new. Some the recommendations fit well until the title of "lightweight formal methods", but (and I don't know how the phrase was first intended) to me the word "lightweight" seems a little pejorative, like they're not _really_ formal methods and can't _really_ handle the problems of real systems like **heavyweight** formal methods could. Perhaps that's just me.

Either way, I went with the idea of formal methods providing _tools_ to verify things about a system. A good tool box has tools for a variety of different things. The paper argues that formal methods are another tool to add to the collection, and describes different things they might be useful for.

I submitted the paper and it's status is "Peer review in process". I'd like to have had it published before the end of this job, but **events...**. The pre-print draft is, predictably, available online:

* "Using Formal Methods for Autonomous Systems: Five Recipes for Formal Verification"
  - [arXiv](https://arxiv.org/abs/2012.00856)



## Runtime Monitoring using CSP

Runtime Monitoring or Runtime Verification was something I'd become interested in as one of the formal verification tools that could be useful when a system already exists. With the addition to the team of [Angelo Ferrando](https://orcid.org/0000-0002-8711-4670), whose PhD is about runtime verification for multi-agent systems, I had a great chance to learn more about it. (So much of being able to develop new areas of interest in academia rests on these chance encounters with someone you happen to get along with and has the right knowledge.)

This paper is from a long-running project, where I was 1) trying to do some runtime verification using one of the project partner's robotic systems, and 2) trying to incorporate CSP, since it's the formal language I'm most comfortable with. So, for this work I wrote a runtime verification tool that uses a CSP specification as the oracle (gives the pass/fail verdict), and applied it to a pair of tele-operated mirroring arms (the operator controls one pair of arms and their movements are mirrored by the other pair).

Most of my time was spent carefully building a specification of the system's safety controls, from an English-language report of a new safety subsystem that was being designed. The amount of time this took was unsurprising since we know that [specification is the biggest bottleneck in formal methods...](https://link.springer.com/chapter/10.1007%2F978-3-319-48869-1_2). Once the model was [built and debugged](/csp-workflow), and could be verified to have the right safety properties, I was able to use it in my runtime verification tool.

I called the tool "Varanus", which is a) the genus of Monitor Lizards, and b) evidence of my poor sense of humour. I was pretty pleased with the tool (and the work itself, shockingly), but one downside was the choice of example application. The system doesn't yet have the safety subsystem that I specified, so I wasn't able to monitor the events that I needed to (because the system doesn't produce them). So I built 'scenarios', which were essentially test cases for the system, to show that the tool (and the specification/oracle) could detect problems and wouldn't react to the system behaving correctly.

This was also the first paper I've written where I've collected any substantial data. I wanted to have some numbers about how long the tool took to check the model. I felt that this was important, because the tool takes the very simple approach of calling the CSP model checker and asking it if the trace of events it has (the 'scenario') is a valid trace of the model. I wasn't sure if this would come out as an efficient way of checking, so it was useful to show the time taken to do this check.

The first conference I sent it to rejected it, mildly, but I think the reviews gave me some useful feedback. It's currently under review again and I have my fingers crossed. In the meantime, the paper is available online:

* "Monitoring Robotic Systems using CSP: From Safety Designs to Safety Monitors"
  - [arXiv](https://arxiv.org/abs/2007.03522)


## Heterogeneous Verification and First-Order Logic Framework

One long-running project within our group has been trying to build an architecture or framework to let us specify the components in a robotic system, but verify each component using different techniques. This is especially useful for robotic systems, which are built from lots of different components that often each have their own field-specific methods of testing or verifying them.

We started off with a small framework the uses First-Order logic, which we thought was simple enough to be more widely understood than if we built our own language or used something more complicated, to specify the components in a robotic system. We added a set of rules to allow us to check that these contracts 'fitted' together correctly and that they obey (for example) the safety requirements of the system.

We've found this project very difficult to get published. I think there are few problems. First, it started off a a bit of a side-project, so it's never had our full attention. Second, the field is kinda crowded with approaches like this, so we've found it hard to find the unique points about ours. Third, when we've written papers about the whole approach, we've had to: explain the approach, show how the contracts work, show how the rules work, introduce a case study and it's specifications, introduce each of the formalisms we've used to verify the components of the case study, and show how the verification links back to the contracts! It's a lot. We often had to cut content to meet the page limit, and then found that reviewers were missing some key information about part of the approach or one of the formalisms. It's been tricky.

However, we have managed to publish this work in bits. First we showed how a(n autonomous) robotic system benefits from verification in different formal methods, but how this leaves you with a problem of integration.
Then we published a paper showing the basis of our approach: the contracts and some of the rules for combining them.
These two papers are:

* "Heterogeneous Verification of an Autonomous Curiosity Rover"
	- Available on [arXiv](https://arxiv.org/abs/2007.10045), and
	- [proceedings](https://link.springer.com/chapter/10.1007%2F978-3-030-55754-6_20), and
	- the example code is on [github](https://github.com/autonomy-and-verification-uol/curiosity-NFM2020)

* "Towards Compositional Verification for Modular Robotic Systems"
	- Available on [arXiv](https://arxiv.org/abs/2012.01648), and
	- [proceedings](http://eptcs.web.cse.unsw.edu.au/paper.cgi?FMAS2020.2) (also open access)

We are currently preparing a paper that uses a more detailed, remote inspection, case study and gives a fuller account of how the use the contracts and rules. For this paper, we've added a Domain-Specific Language to help users to write the contracts, and a tool to parse contracts and translate them into runtime monitors. I've written that tool, so it has an even more nerdy name than my previous program! Hopefully that bit of the work will also be published.

## Multi-Agent Programming Competition Modelling

After [Rafael Cardoso](https://orcid.org/0000-0001-6666-6954) joined the group, in 2018, he started a team for the [Multi-Agent Programming Contest](https://multiagentcontest.org/). The research group has a lot of work using [BDI Agents](https://en.wikipedia.org/wiki/Belief%E2%80%93desire%E2%80%93intention_software_model) so I had some idea of what these systems are like, but like with Angelo and Runtime Verification, its really useful to have someone in the same office as you and at the same 'level' as you to chat to about it.

I didn't think I could bring anything to the team, so for the first year I just watched and listened to some of the conversations that went on in the office or around the whiteboard by the _secret_ kitchen. The teams can't see the matches in the competition until after they're all finished, as replays. When the replays came in, I stayed in the office to watch them (the closest I usually get to watching sport). The team won, which was exciting.

Next year, Rafael said he was going to enter the competition again, and I wanted to see if I could add some formal methods to their approach. I started modelling a complicated protocol that governed how the agents built up a shared map of their environment.

The model isn't quite finished yet (but then, the competition is still running, and there was _The Event_ to deal with) but even so, I've seen that multi-agent systems have more in common with other types of real-time systems than I had expected. These sorts of synchronisation problems are dealt with in similar ways to other real-time problems, locks and atomicity, but sometimes under different names. It was a new perspective on this type of system, that I wouldn't have gotten otherwise.

Now Rafael and I are preparing a paper about this modelling and verification of the protocol used for our entry to the competition this year. It's not yet written, but it's an interesting side-project that I hope gets published.


## Formal Methods for Autonomous Systems Workshop

Not at all a paper, but something that has been an interesting experience during this job has been starting a new workshop. Me and Marie decided that it would useful to have some more event-organising experience, plus there seemed to be a gap for a workshop about the application of formal methods to autonomous systems.

After writing the survey paper, and it's position-paper offspring, we felt like we had a good grounding in what had been done recently with formal methods and autonomous systems, but it seemed that they were still two separate communities. Our workshop "Formal Methods for Autonomous Systems" (FMAS) is trying to bridge that gap.

So far, we've had two editions of the workshop. In 2019, the first FMAS was held at the [Formal Methods conference](https://formalmethods2019.inesctec.pt/). It was a _World Congress_ year, so it was big. This felt like a huge chance for us, and I was pleased that we were allowed to run our workshop there -- plus it was in Porto! The second workshop, in 2020, was obviously a lot different. Due to _The Event_ the conference we had aimed at was not taking on workshops, so we ran it solo and online (like all the other conferences and workshops). This still went well, and it was great to see some friends and colleagues again.

As someone who struggles to juggle so many things and (often) to organise, I'm pleased to have been able to make these events work. And as someone who can remember being *terrible* at giving presentations and talking publicly, I'm proud to be able to see how much progress I've made on those things. Also, I find that running your own workshop feels very (academically) _grown up_, which is an unusual but nice feeling.

The websites and proceedings can be found online:
* FMAS 2019
	-	[website](https://autonomy-and-verification.github.io/events/fmas2019/)
	- [proceedings](https://link.springer.com/book/10.1007%2F978-3-030-54994-7)

* FMAS 2020
	- [website](https://autonomy-and-verification.github.io/events/fmas2020/)
	- [proceedings](http://eptcs.web.cse.unsw.edu.au/paper.cgi?FMAS2020)
