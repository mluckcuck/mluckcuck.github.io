---
layout: post
title:  "CSP Workflow"
date:   2020-06-28 11:18:00 +0000
categories: [research]
permalink: /csp-workflow
section: Blog
---

I often work with the formal language Communicating Sequential Processes ([CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes)) and its associated model checker [FDR](https://en.wikipedia.org/wiki/FDR_(software). (A [previous post](/model-checking-cheatsheet) gives a quick description of what model checking is.)

I'm used to the broad workflow involved with modelling and model checking (I've been doing it since the start of my PHD) so I know that I need to build a model, which should have some properties, then check that the model has these properties. Sometimes it's the other way around, and the properties (often being more abstract) come first, and the model implements the properties. But I find that modelling and them checking the model better suits my brain.

During work on a [recent paper](/varanus) (and after reading some papers that talked about Specification/Model Debugging) I started thinking about how I go about this process. Debugging is something that feels much more closely linked to 'proper' software, but since I've always approached formal methods in a more software-development style, it made sense that a formal model should also need to be debugged.

The following was originally written as I was trying to check that my [CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes) model obeyed some properties. Both the model and the properties were derived from a natural-language document (i.e. a report written in English) which often leads to a tricky modelling process, because of the vagaries of natural language.


## Model Debugging

Usually, when I check an assertion on my model it fails. It's like running a newly written program; it rarely works first time. Either the property specification is wrong, or the model is wrong.

When an assertion check fails, FDR produces a counterexample -- the trace of event that leads to a failure, and an example of why the check failed -- which is a great place to start debugging. Sometimes I can use the counterexample to step my way trough the model and find the source of the problem. But often, the model has gotten to be too big for that, it requires simultaneously stepping though multiple files and keeping track of how they all interact. That quickly becomes too much for my brain to keep track of, avoiding having to do this is the point of using a model checker!

My next source of information is the acceptance and refusals of the different processes in the model. Again, this is information in the debugging window for the failing assertion. Unfortunately, I usually find that the acceptance and refusal sets are far too big to easily look through by eye. What I need to know is: which processes aren't accepting the next event, but should; or which processes are refusing the next event, but shouldn't. FDR doesn't let me easily get at this information. It would be great even if it could just highlight processes that are refusing the event that the property specification wants to do next. Alas, no.

To side-step this problem, I use my text editor to help reduce the number of processes I have to look closely at. I use [Atom](https://en.wikipedia.org/wiki/Atom_(text_editor)) to write CSP. Among other useful features, it lets me search the directory that contains my CSP files. So, I search for the event that the specification wants to do next. This usually brings up lots of files -- obviously including both the file where the channels are defined and the file where the property specifications live! So I collapse them all and go one-by-one through each file that is actually a process.

For each process that I find that _can_ engage in the blocked event, I swap back to the FDR debug window and see if that process is accepting the event. (We could check the refusals, but usually the set of acceptances is smaller.) If a process is accepting to do the event, we don't need to look at the file and we can move on to the next potential source of the blockage.

When we find a process that _can_ perform the blocked event but isn't accepting it, we can investigate further. Note that it might be a good idea to check all the files before moving on, just in case more than one processes is refusing this event.

Once we've found the offending file(s), we can open them up to take a closer look. Helpfully, if Atom is still in 'search mode', it highlights the event we're looking for. This is where we need to step through the failing trace in this process to see what state it's in at the time of the failure.

First, I usually eyeball it, stepping through the process by eye to follow how it reacts to the events in the trace. Sometimes this will quickly lead you to an event that doesn't look right. You can then compare this to other processes and try to work out if something needs changing.

If eyeballing the process(es) doesn't help, then we can use FDR's Probe tool to do some of the work for us. Probe loads a given process and lets you step through the possible events. You get a list of events that the process can do, when you select an event you get the next list of possible events. Using this, we can step through the events that the model checker is able to perform when it's checking the assertion. This is sometimes a quicker (and definitely less error-prone) way of working out what state the offending process is in at the point of failure.

Whichever method is used, hopefully you eventually find the potential source of the failure, the event that is blocking the cogs of the process from turning freely. This is where we need to start making some changes and testing them out. Delete (or maybe comment out) the potentially problematic event(s), save, reload the process in FDR and check the assertion again -- crossed fingers may or may not be helpful.

If this solves the problem, that's great! But don't forget to recheck all the other assertions (i.e. regression testing) to make sure that you've not solved one problem but caused another.

If (as I find is so often the case) this edit hasn't solved the problem, then we need to keep digging around. Perhaps the edit we made was wrong? Or, perhaps the edit was the right step towards solving the problem, but there are other edits that are needed? At this point we need to go back to examining the process, either by eye or using FDR -- probably both.

Eventually, this little loop of edits and rechecking should get you to the point where your assertion check passes. This warrants a small celebration. But, and I'm going to say this again, before you continue you need to **recheck all the other assertions**. This regression test is key to make sure your whole model still works. Often this change to make one thing work might deadlock another part of the process. The restarts our edit and recheck loop, just with a slightly different failure.

When you have finally edited the model in the right way, and all your assertions pass, you can take a moment to celebrate (personally, I usually punch the air and spin around in my chair) and then ask: what's next?


### Workflow

In summary, the debugging workflow I use is:

1. Search CSP model for the specification's next event, using your text editor's search feature;
2. Check each process that can do the event against its acceptances in the FDR debug window;
3. Examine the file(s) of processes that can perform the blocked event but are refusing to;
4. Alter process and recheck;
5. If the check still fails, go back to step 3.; if the check passes, we're done.
