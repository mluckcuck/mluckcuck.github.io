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

The process of designing and writing a program is often broken down into a basic cycle of four steps: analysis, design, coding, and testing. First, we analyse the problem we're trying to solve. Next, we design an algorithm to solve the problem. Then, we write some code that implements the algorithm we designed. Finally, we must test that our program implements the algorithm corectly (assuming that the algorithm we desgined _does_ solve the problem). If the program doesn't solve our problem -- and they often don't on the first try -- then we go around the cycle again. This creates a cycle of trial and error (know as **debugging**), often mainly error, that becomes familiar the more we program.

Even if our program does work first time (as I said, unlikely) we will still often go around the fout-step cycle a few times. There are a few reasons for this. We often break down (**decompose**) large problems into a collection of small problems and solve them individually. Equally, we might start with a small problem, solve it, and then add more detail.
Both situations require going through the steps more than once.

Another approach we often use is to focus on the general details of a problem, ignoring information that doesn't help us (**abstraction**). For an example of this we can think of a bus route map. It may show us some landmarks and larger street names, but it will ignore a lot of detail that a street map might show. This is becasue it's purpose is to show us the bus routes and enough information for us to get to a bus stop.

Finally, it's time for a tea break! In order to fulfil a national steeotpye, lets use making a nice cup of tea as an example to look at building an algorithm. Imagine we want to make some tea, a basic algorithm for that could be:

```
1. Boil water
2. Add tea to the pot
3. Add boiled water to the pot
4. Brew tea
5. Pour tea into a cup
6. Stir tea
7. Enjoy!
```
This sequential algorithm describes the basic steps to make a cup of tea, but lets add a little more detail. What if we want some sugar or milk in our tea.

```
1. Boil water
2. Add tea to the pot
3. Add boiled water to the pot
4. Brew tea
4. if sugar = true then
  * Add sugar to cup
5. Pour tea into a cup
5. if milk = true then
 * Add milk to cup
6. Stir tea
7. Enjoy!
```
This algorithm introduces variables and branching. The two `if` instructions check if a condition is true before performing an instruction. Both `sugar` and `milk` are variables, data that might change. If we step through this algorithm for one person, they might want both sugar and milk. Another person might want only milk. This algorithm can now cope with any combination of tea, sugar, and milk.


What if we were making tea for several people at once? We'd have to go through the algorithm above several times, and some of the steps we don't need to complete multiple times if we already know that we're making tea for lots of people.

```
1. Boil water
2. foreach person do
 1. Add 1 spoon of  tea to the pot
3. Add boiled water to the pot
4. Brew tea
4. foreach person do
 4. if sugar = true then
   * Add sugar to cup
 5. Pour tea into a cup
 5. if milk = true then
  * Add milk to cup
 6. Stir tea
7. Enjoy!
```

This algorithm introduces looping, allowing up to repeat certain instructions several times. There are a few different ways to organise a loop, here I've chose a loop that repeats a fixed number of times (whatever the value of the variabl `person` happesn to be). This means we can cater for as many tea drinkers as we like -- as long as the tea pot is big enough!

This example shows us the ideas of starting small and then adding detail, which allows us to test the basic idea before start complicating things with branches and loops. It also shows us how we can use variables, equences of instructions, branches, and loops to build our algorithm. Finally, it shows us how useful abstracting away from certain details can be. Things like boiling and brewing can be ignored for designing our algorithm, but implemented when we need them (like if we were going to build a machine to make our tea).

My final thing to say about programming is about failing. I've menetioned a few times that a program rarely works the first time, so we spend a lot of time fixing problems in our programs. This is related to the idea that computers are stupid; they will do whatever we tell them to do, even if it makes no sesne. THis can be tricky at first, but it gets easier with practice. The key thing here is to not be scared of trying, somtimes the program works and sometimes if doesn't. If it doesn't work, then we'll just fix it. Programming is the process of giving a computer instructions, which in the end comes down to a cycle of trying, failing, and fixing. 
