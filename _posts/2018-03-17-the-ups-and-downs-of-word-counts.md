---
layout: post
title:  "The Ups and Downs of Word Counts"
date:   2018-03-17 19:30:01 +0100
categories: writing
image : /files/images/thesis.png
section: Blog
---

Whether you're writing fact or fiction, your word count will experience ups and downs, fits and starts. It's very easy to imagine the process of writing as a nice smooth path from an empty document to the finished article; with each word count being a triumphant increase over the last word count. (OK, so maybe not everyone checks their word count as often as I do.) However, this is not true.

As a recovering PhD student, I've seen the problems with this mindset first hand. I hadn't been told that the word count should just increase as you write, it was simply a an assumption in the back of my head. After ~~completing~~ abandoning my thesis, I knew that the word count had fluctuated. To visualise this fluctuation, I wrote a small program to graph the word counts.

Skipping over the technical details; the system I use to store backups of and track changes to what I'm working on lets me access snapshot of the document. The program steps back through these snapshots, storing a word count of each version of the document. The tool is available [here](https://github.com/mluckcuck/GitCounting), though it is still in (slow) development and is presented, very much __as is__.

With that out of the way, lets look at some of the word count graphs one-by-one.

## An Extended Abstract

First, a four page extended abstract "A Formal Model for the SCJ Level 2 Paradigm"
![Word Counts for A Formal Model for the SCJ Level 2 Paradigm ]({{ site.url }}/files/images/DSFM-ExtendedAbstract.png "Word Counts for A Formal Model for the SCJ Level 2 Paradigm")

At the beginning of writing this abstract I've clearly dumped a lot of material into the document and then edited the text a lot and 'lost' ~250 words. Then, over a few months, the word count has bounced up and down, before finally 'plummeting' to ~1200 words. After this, comes several months of minor tweaking, with a relatively stable word count.

I remember part of the problem when writing this abstract was trying to say what I wanted within only four pages. Here, there was more to say than I had space for, so I had to do a lot of editing to get the word count (or, page count) down.

Especially in this instance, the 'loss' of words was definitely part of the process and was needed to get the final article.

## A Long-Slog Journal Article

Next, a journal article that took a long time to finish and get published: ["Safety-Critical Java: level 2 in practice"](https://doi.org/10.1002/cpe.3951). I wrote this paper before I started tracking the changes to my documents properly, so this file is from later in the process and therefore has already been worked on. This means that the jumps on this graph look huge, but the range of this graph is only around 600 words. Still, lets look at the ups and downs.

![Word Counts for Safety-Critical Java: Level 2 in Practice]({{ site.url }}/files/images/CPE-SCJL2.png "Word Counts for Safety-Critical Java: Level 2 in Practice")

This journal paper started life as a workshop paper (for JTRES2013) so I had decent word count to begin with. At the beginning of the period this graph covers I've clearly made some additions to a section and then made some minor edits that don't alter the word count very much.

Then there is a jump from ~10950 words to ~11450 words, before I edit that down by ~100 words. Then, over the next 9 months the word count pings up and down by ~100 words. I think this is a section where I'm addressing changes requested by the reviewers and editor.

The word count has a final peak (obviously I'd had a good idea) followed by some editing down to, what becomes, the final word count. As I mentioned earlier, this graph covers the final part of writing this paper, so most of the ups and downs are from editing changes.

## The Rumble in Reykjavik

Finally, my favourite paper ["A Formal Model of the Safety-Critical Java Level 2 Paradigm"](https://doi.org/10.1007/978-3-319-33693-0_15). This was the first paper that felt like _mine_ and it took me back to Iceland, a trip for which I was very grateful. Anyway, lets look at the graph.

![Word Counts for A Formal Model of the Safety-Critical Java Level 2 Paradigm]({{ site.url }}/files/images/iFM-Modelling.png "Word Counts for A Formal Model of the Safety-Critical Java Level 2 Paradigm")

Looking back at this one, I'm not entirely sure what's happened. I've clearly dumped a **large** amount of material into the file (I have a feeling it might have been a draft of my thesis...) and then thought better of it, which explains the first peak. The second...might be an honest mistake, I doubt I've managed to write ~47,000 words that needed _that_ much editing out!

The interesting collection of word counts appear between August and November 2015. There are a lot of point closely bunched together (clearly, I was being very productive!), which makes things a little hard to see. However, there are two clear ups and two clear downs, before the word count stabilises again.

After a final big edit in, what looks like, January, the word count remains relatively stable. There are a few dips here and there, but I've obviously got the sections written and I'm editing. Again, this paper shows peaks and troughs as the structure of sections changes and the material I've drafted gets edited down and focussed. This process helps the reader to understand what you __mean__ rather than what you __wrote__ in the first draft.

Thesis
------

Now, we come to the **main event**, my thesis ["Safety-Critical Java Level 2: Applications, Modelling, and Verification"](http://etheses.whiterose.ac.uk/17743/). Obviously this took a lot more work over a longer period, so I'm going to look at this in a little more detail.

![Word Counts for My Thesis]({{ site.url }}/files/images/thesis.png "Word Counts for My Thesis")

The first thing to note is that I didn't even start writing my thesis document until I was about **two years** into my PhD (about halfway through my time as a PhD student, as it turned out). Once I did start the document, the word count remains very close to zero for about a year. (I **was** writing things for my thesis, but into separate files in the Thesis folder, accumulating words to edit in later.) What I made sure I did in that first year was have a document that conformed to the university's submission guidelines (not that it took me a year to do, but I was working on other things too). That way, I knew that I wouldn't be tempted to start fiddling around with those settings later, as a distraction (cunning!)

The first real activity comes around February 2016, where I __think__ I've just dumped a load of text from papers and those other files I mentioned into the document. (I'm detecting a pattern here.) This second picture shows that section of the graph in more detail.

![Detail Graph of my Thesis Word Counts]({{ site.url }}/files/images/thesis2.png "Word Counts for My Thesis")

Here we can see that the very next word count drops by maybe a 1000 words, then rallies by about 500, and then drops lower. The word count then rises in large, long steps. Again, I think this fits my writing pattern of dumping in material or writing a large part of a section, and then editing it down to focus what I've said. As I mentioned earlier, this is a useful process that helps make sure that your writing says what you **mean**.

The next picture shows, again, more detail. This graph spans the space of about four months.

![Detail Graph of my Thesis Word Counts]({{ site.url }}/files/images/thesis3.png "Word Counts for My Thesis")

Here, we can see some fairly smooth rises and a few plateaus. But there is a small drop around the 20th of August and an even more severe drop near the beginning of next month. While these can look drastic (and probably felt devastating at the time) the process of editing and cutting words is essential. I may well have written several paragraphs of absolute rubbish and decided to remove them (as well as some crafty, skilful editing too, obviously!)

The final picture shows the process of writing up my corrections (the changes requested by my examiners). Because my thesis is basically done by this point, the word count drops during editing aren't as large.

![Detail Graph of my Thesis Word Counts]({{ site.url }}/files/images/thesis4.png "Word Counts for My Thesis")

Since my corrections mostly included adding extra explanations to my thesis, the progress here is generally upwards. But there are still the usual peaks and troughs of editing and backtracking. Eventually, after much frantic work, the word count stabilises again.

Summary
-------

A word count is a one-dimensional metric, which doesn't really reflect the quality of what you've written. I know that my writing pattern is to write a chunk and then edit it. Therefore, while the trend of my word counts (as can be seen in the graphs) is generally upward, there are ups and downs. That being said, seeing your word count drop can feel devastating and demoralising.

The editing process is **necessary** because writing perfectly first time is almost impossible. A drop in your word count can be because of removing typos, useless words or paragraphs, or restructuring the material for the benefit of your reader. Essentially, it is often a sign of you improving the __quality__ of what you've written.

Finally, the idea that word counts always go up or that a drop in your word count is a bad thing is pervasive and almost comes from nowhere. I know how essential editing is, especially to my writing, and yet seeing a lower word count than when I started is still demoralising at times. I try to remind myself that the document I'm writing is __evolving__ and so navigating out of dead-ends and backtracking is fine. Ultimately, if I'm improving the quality of what I've written, it's more helpful to my readers.
