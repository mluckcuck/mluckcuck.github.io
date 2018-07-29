---
layout: post
title:  "Autonomous Robots in Hazardous Environments"
date:   2018-05-03 19:30:01 +0000
categories: research
section: Blog
---

I work as a Research Associate in the [Department of Computer Science](https://www.liverpool.ac.uk/computer-science/) at the University of Liverpool. I'm working on the Autonomous Robots in Hazardous Environments project [here](https://www.epsrc.ac.uk/funding/calls/raihubs/).

The team at Liverpool is involved in three related, 'hubs'. Each hub focusses on autonomous robots in a different hazardous environment: [nuclear](http://rainhub.org.uk/), [offshore](https://orcahub.org/), and [space](http://cgi.csc.liv.ac.uk/~michael/FAIR-SPACE-Hub/). Each of these environments can be dull, dirty, dangerous, or distant.

* Dull jobs lead to mistakes;
* dangerous and dirty jobs are harmful;
* and distant jobs make usual remote controlled robots tricky or impossible.

These hubs are focussed on reducing the risks to people working in and increase the capability of the robots being used in these environments. The reduction of risk means we need to be mindful of making the robots __safe__, and increasing their capabilities often leads us towards making them more __autonomous__

In this article, I'm going to answer the following questions:
* What are __autonomous__ robots?
* Why would we want to use them in these 'hazardous environments'?
* What do we mean by __safe__?

## Autonomous Robots

Some robots are romote controlled, some follow a pre-written program, neither of these are good options for the hazardous environments that we're looking at. When the robot's environment might change, or the robot itself might change, the assumptions made when writing the program might not be true anymore. To deal with this, we need to introduce some style of autonomy. Essentially, an __autonomous__ robot is one that can make decisions for itself; think R2-D2, rather than a production-line robot.

A useful example here is the [Curiosity rover](https://mars.nasa.gov/msl/) that is exploring Mars, which can be driven remotely from Earth or [navigate autonomously](https://www.jpl.nasa.gov/news/news.php?release=2013-259). Examples of changes to this environment might be finding a large crater or an impassible obstacle, which means that the navigation system will need to adapat the route. A more ambitious challenge (that the rover can't yet handle) is that it might need to change itself to adapt to damage or to some change in its environment.

Because the Curiosity rover is on Mars, radio signals sent to and from the robot are delayed by an average of about [14 minutes](http://blogs.esa.int/mex/2012/08/05/time-delay-between-mars-and-earth/). This means that if a robot on Mars detects a large crater that it will fall down, and sends that information back to Earth, it will be 14 minutes before we know about it. If we tell the robot to stop or turn to avoid this deadly crater, that signal will also take 14 minutes to get to Mars. By this time it's likely that our robot is now uspide down, wheels spinning, and possibly damaged beyond repair (I don't think that breakdown recovery covers Mars).

An autonomous robot is basically one that can sense its surroundings, 'think' about that information, and then act on the information. This loop of behaviours enables robots to adapt to changes in a way that is smarter than a program that tries to dictate the robot's response to every possibility. The biggest challenge that this approach helps us deal with is a changing, unknown, and dangerous environment.


## Hazardous Environments

As I mentioned at the begining, the project I work on covers three hazardous environments. For our work with the nuclear industry, we're looking at robots that handle nuclear waste material for safe desposal; the offshore robotics are used to check if structures that are in the ocean (things like wind turbines) need repairing, and; the robots designed for space are likely to be exploring the Moon or Mars. Each of these environments has its own challenges.

For robots in the nuclear industry, the obvious problem is radiation. Even with large amounts of protective equipment, humans can only spend a relatively short time working around that much radiation. Remote controlled robot arms are often used but the view that the operators get is restricted by the radiation shielding. The jobs that the robot arms need to do are repetative and difficult. All in all, remote control is not a good option.

Sending teams of robots out to sea brings a different set of challenges. These robots might be in, on, or above the water; but either way, they'll have to cope with changing sea state and wind conditions. The dangers faced by humans doing this job are the main reason for using robots instead. Remote could be possible, but the rapid changes in wind and sea state might be too fast for a human to react in time.

An example I've already used is robots helping us to explore [Mars](https://mars.nasa.gov/msl/). Since humans need air to breath, space isn't a great place for us to work. When we go into space we need a lot of protective equipment to stay ~safe~ alive. One problem I've already mentioned is the time delay for radio signals from the Earth to Mars, which makes remote control very tricky. Another challenge is that a lot of detail about what we'd like to explore in space is unknown (that's why we want to explore it!) so we can't rely on a good map of the area.

Each of these three environments is hazardous, both to humans and to the robots. Humans already are (or have been) doing these jobs, working in dangerous places and putting a lot of effort into staying safe. Robots can help us to avoid some of the most dangerous situations and enable us to focus on doing the jobs better. Robots will also face danger in these environments, which is another priority for autonomy. Autonomous robots must also be safe, both with respect to themselves and to humans around them.


## Safe Robotics

[//]: # (Too Big)


* Safety Properties
    - Taken from the design or regulators
    - shown by verification techniques: testing, simulation, formal methods
* Testing
    - runs a program and checks that its output matches the expected output
    - only one run of the program
* Simulation
    - simulates the physical environment of the system and run the program
    - checks that the behaviour is as expected
    - again, one runs
* Formal methods
    - unambiguous language, mathematically described
    - logical methods to check the whole program
    - Often more abstract, so have to check assumptions/abstractions to link back to program


Because the robots we're looking at are going to operate in dangerous places, away from human control, we want to make sure that they behave as designed. We need to make sure that the program controlling the robot acts safely; for example, this can mean not damaging things around it or not damaging itself. Essentially this is involves compring the program to the design. I'm going to describe three ways of doing this with robots: testing, simulation, and formal methods.

Testing a robot can mean running just the program, or a __field__ test where the physical robot is used. Both involve comparing the behaviour of the program or the robot with the expected behaviour. Becasue this is done with the actual program or robot, the link between the results of testing and the final system are pretty close. However, testing can take a lot of time. Each test is only one possible behaviour of the system. Also, field tests could potentially damage the robot or things around it.

Running the program but simulating the robot and its physical environment avoids the potential damage of field tests, and enable you to test the robot ins situations that are difficult to get at physically. The idea here is the same as with testing: run the program and compare its behaviour to the expected behaviour. But it has the same problem as testing: each simulation run is one path through the program, so it can be time-consuming. Another problem is how realistic the simulation is and if you have to alter the program to use it in the simulation, then the link between the results of simulation and the bahviour of the final system might be a little less convincing.

Finally, Formal Methods use unambiguously defined languages and logical methods to check the whole program, not just one run. However, this requires some extra work up front. This often can't be done on the program (though there are exceptions to this) and requires a more abstract model of the system, which is then checked for the expected behaviour. The link between this abstract model and the final system is a key weak point of this approach; the model can be safe but the final system might not represent the model well enough.

Testing and simulation are used a lot when verifying robots, but Formal Methods also have some applications here. My work is about using Formal Methods, but not to the exclusion of other techniques. A holistic approach will be the most practical and be the most conviincg to the public and the regulators.
