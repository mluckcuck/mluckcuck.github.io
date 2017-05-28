---
layout: post
title:  "Introduction to Programming"
date:   2017-05-28 11:48:19 +0100
categories: programming
---

There is a lot that I could say about programming, but this is intended as a brief introduction so I've kept to the basics. This post will cover what programming is, discuss programming languages and the process of programming, and provide a small example of a basic program. I should also say that this is based on a talk I put together for a recent interview, the slides for which can be found [here](/files/presentations/IntroductionToProgramming.pdf).

The first thing I always ask when introducting someone to programming is "Have you done any programming before?" Most people say no, becasue they think they haven't. Perhaps you're saying the same thing to yourself now. But consider setting up a timed recording on a VCR -- or something like a Sky+ or TiVo box, for a more modern example -- or setting a washing machine's programme. These are, in essence, programming. You are interacting with the computer embdedded in that device to give it instructions. You push some buttons and tell it to _record every eipsode of Game of Thrones_ or _wash these clothes at 30&deg;C and spin them at 1200_. Even though what you're able to tell the computer is relatively restricted, you are programming.

At its most basic, we can say that programming is the process of giving instructions to a computer. More concretely, programming is the process of **desiging** and **writing** instructions for a computer.

The first thing to say about computers, when considering how to design and write programs for them, is that computers are **stupid**. We often talk about computers being _smart_ or that they are _thinking_ about something. It can often seem this way, but the bottom line is that computesr are good with numbers and repatition, but all-in-all are rather dumb. So, we have to tell them _exactly_ what to do. This means that we need to be able to give precise instructions using a language that the copmuter can 'understand' (and I'll return to the issue of a computer understanding the language in a moment).

A program may solve one or many problems, perhaps it's a big problem that is broken down into several smaller problems to make it easier to solve. The sequence of instructions we design to solve a particular problem is called an algorithm. For a few everyday examples of algorithms, that are nothing to do with programming, we can think of a recipe or a set of directions. In each case there is a problem to solve (_how do I bake a cake?_ or _how do I get to the train station?_) and a sequence of instructions to solve it.

For computer programming, we need to be able to write our instructions in a language that the computer 'understands' (don't worry, I've not forgotten that I said I'd explain this in more detail, the explanation is on it's way) and this is where programming languages come in. Programming languages (examples inclide: C, Scratch, C++, Java, Python, Javascript, and PHP) provide us with a set of instructions that we can use to tell the computer what to do. These instructions can include things like variables, which are data that might change during our program; expressions, which are statements that have a value; and control structures, which allow us to repeat instructions or to choose which instructions to perform. Like a natural language, these instructions are combined according grammar rules to make a valid program.

Earlier, I mentioned that programming languages are something that a computer can 'understand' (yes, I'm finally going to explain). In reality, computers can only understand binary instructions (1s and 0s), which represent the presence of ansence of an eletrical current. Modern programming languages are designed to be human-readable (in that they use words like `print` and `input`) and are automatically translated into a form that the computer can understand (machine-readable). 
