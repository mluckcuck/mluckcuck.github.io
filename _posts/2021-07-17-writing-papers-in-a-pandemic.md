---
layout: post
title:  "Writing Papers in a Pandemic"
date:   2021-07-17 17:15:19 +0000
categories: [academia, research, mental-health]

section: Blog
---

Like a lot of a friends in academia, I feel like I've been struggling to get things written and published during the past 18 months. I know, I know... _pandemic_ but there still feels like a lot of pressure, even more so with time-limited contracts. I've only got so many months, so not getting things published feels like wasting time. (I know, I know... _pandemic_!)

During my PhD I worked a lot from home, so I've felt that not being able to go into the office during the UK's lockdowns (and now my theoretical office being across the Irish Sea) hasn't been all the different. However, given how long this has been going on for, now I'm beginning to notice the toll its taking.

I've come to realise that the loss of an office (not counting my spare-room-study) has had two negative impacts.
1. As a lot of people have said, not getting to have quick conversations with colleagues about work, or get around a whiteboard/computer screen has really slowed things down. Yes, I've been able to have chats more easily with people that are in various different cities/countries, but actually doing work with people is (theoretically) work with has been very slow.
2. For me, having an office was a physical reminder that I work as an academic -- the same reason I got university business cards when i started my first post-doc job. I feel like this might sound obvious or pathetically materialistic, but I realised that having an office door with my name on it (obviously a shared office, but still) that I went in to and did...academicy things was important to me. A lot of the time Research Associates aren't treated as academics within a lot of UK universities, we're 'just' researchers. But aside from that, I found it helpful to have something tangible that I could point at to convince myself that the struggle through my PhD was worth it.

Even without an office or 3D colleagues, I thought I was making a semi-decent attempt at finishing two single-author papers and I was finally looking forward to getting them published. One was for a conference, this was rejected; the other was for a journal, and this received 'Major Revisions'. The reviews were fairly helpful (and for the journal paper, they were actually extremely nice and constructive) but I still had the usual knee-jerk reaction of 'they've clearly just misunderstood what I wrote'...until I actually re-read the papers and re-examined some of the work. Then I could see how bad they were, see the impact of trying to work during all of..._this_.


## Paper 1: The Programming Error

The first paper, the one rejected from a conference, was describing a software tool that I'd been writing for a while and a formal model that I'd built during the previous project. It began as a bit of a side project, but was also trying to collaborate with other members of the project. This was the second go at sending it to a conference, and the second rejection.

In response to the reviews -- one, long and detailed review in particular -- I decided to re-do some of the timed runs of the software tool for a different analysis of the length of time it took to complete its run. The tool had two options, which triggered two different ways of working, so both of these were part of the comparison.

I set about adding a little to the software tool, to automate the data collection so that I could complete the paper in time. (Previously, the data collection was done by me manually running the program several times and collecting the information from the logs!) I was quite pleased with the changes I'd made. It made it easier for me to check how long the tool took to run on different sets of inputs, or after changes; and it would make things easier to replicate -- should anyone ever care enough to do so.

There was one curious thing about the results, not just for this third version of the paper, but in the original version of the paper too: the option that I expected to result in the tool taking longer to run was actually taking much much less time. Curious. I had a few theories as to why, but no time to investigate further. A few reviewers mentioned how strange this was, and queried why.

By chance, I was scrolling through part of the program to check something when I found the answer to why that option was running so much faster. The program wasn't actually doing what I thought it was. The program got halfway through and then skipped what it should be doing. Why? Because I had commented a line out (meaning that the line still exists in the program but is ignored). Evidently I had been testing something out and forgotten to uncomment the line.

I still feel stupid for doing this, even though the paper wasn't accepted anywhere. It's such a simple error that I feel like I should have caught it.

## Paper 2: The Garbled Text

The second paper is a 'chatty paper', by which I mean it's a position paper. It discusses ideas and techniques, but it's not presenting new work. I feel like this is helpful in general, but that my field doesn't often do chatty papers. Plus, I don't usually think that anyone want to read what I have to say about...well, anything -- this blog included!

Anyway, I had the chance to send a paper to a journal _special issue_ so I thought it would be useful to a) present some ideas that consolidated existing work 'in the literature', and b) to get a single-author journal paper published, just to show (myself and others) that I could.

Again, this paper had one very helpful, detailed review that provided so many pointers to areas of the paper that didn't make sense and needed re-writing. But eve so, there were parts of the review that indicated passages or paragraphs that 'didn't make sense' and I'm thinking 'how have you misread this, then?' Then I look at the indicated lines and find that no, actually, the sentence is utter rubbish, the paragraph is nonsense.

What made it worse, when re-writing the paper, is that there were times where I genuinely couldn't work out what I had originally meant. Sometimes I can see what I'd meant to say, or I can see that this was two (or more) sentences that I've smushed together for space. With some of these, I had to take the sentence out and start again, or say something different.

Now, this isn't a new thing. I'm sure most people have re-read things they've written and found themselves puzzled about what they had intended to write. This happens to me a lot, whether through being tired or because of dyslexia getting in the way. But usually **I notice**. This time, no. This time, I thought it was an OK paper.

It seems that the hard work of re-writing the paper (and sometimes re-examining what I even _meant_) was worth it. The revisions were accepted, and the reviewer comments on the updates were very complimentary. It's a shame that I'll never get to tell them how happy it made me to get reviews that made it clear that the hard work I'd put in was visible to the reviewer. So often reviews are either neutral or negative in tone.
