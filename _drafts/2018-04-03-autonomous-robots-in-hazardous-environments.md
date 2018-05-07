---
layout: post
title:  "Autonomous Robots in Hazardous Environments"
date:   2018-05-03 19:30:01 +0000
categories: research
section: Blog
---

I work as a Research Assistant in the [Department of Computer Science](https://www.liverpool.ac.uk/computer-science/) at the University of Liverpool. I'm working on the Autonomous Robots in Hazardous Environments project -- details of the EPSRC grant can be found [here](https://www.epsrc.ac.uk/funding/calls/raihubs/).

The project combines three separate, but related, 'hubs'. Each hub focusses on autonomous robots in a different hazardous environment: [nuclear](http://rainhub.org.uk/), [offshore](https://orcahub.org/), and [space](http://cgi.csc.liv.ac.uk/~michael/FAIR-SPACE-Hub/). Each of these environments is dangerous, so we'd like to improve the robotics used in these environments to reduce the risk to the people who work there. This involves robots that can be __autonomous__ and proved to be __safe__.

In this little article, I'm going to answer the following questions:
* What are __autonomous__ robots?
* Why would we want to use them in these 'hazardous environments'?
* How do we prove that they're __safe__?

## Autonomous Robots

In essence, an __autonomous__ robot is one that can make decisions for itself. We're talking more like C-3PO than a robot arm on a production-line. Things like robot arms are sometimes remote controlled (tele-operated), and simply perform the behaviour they're told to; sometimes they operat on their own, but follow a script that tells them what to do. As I'll talk about in the next section, neither of these are good options for the hazardous environments that we're looking at.

//how?



The robots we're going to use need autonomy to be able to naviagte their particular hazardous environment, which might change quickly or not be fully mapped beforehand.
They also need to be autonomous so that they can do their job, which might involve

 Robotcs in the nuclear industry



The benefits of using autonomous robotics in this environment are an increased working efficiency and lower risk to humans.


Like the material in the RAIN hub, the offshore assests that are being assessed will not appear the same as when they were installed, so complex decisions need to be made about the level of repair of assets in and on the water.

Each of these application areas displays similar characteristics. A high level of autonomy is required to plan and execute the required task. Further, teleoperation is either error-prone or infeasible.

## Hazardous Environments

As I mentioned at the begining, the project I work on covers three hazardous environments. For our work with the nuclear industry, we're looking at robots that handle nuclear waste material for safe desposal; the offshore robotics are used to check if structures that are in the ocean (things like wind turbines) need repairing, and; the robots designed for space are likely to be exploring the Moon or Mars. Each of these environments has its own challenges.

For the nuclear industry, the main problem is large amounts of radiation. Even with large amounts of protective equipment, humans can only spend a relatively short time working around that much radiation. Remote controlled (tele-operated) robot arms are often used to keep humans away from the radiation, but the job can be repetative, so the oporator can eventualy make mistakes.

Sending teams of robots out to sea brings a different set of challenges. These robots might be in, on, or above the water; but either way, they'll have to cope with changing sea state and wind conditions. The dangers faced by humans performing this job are the main reason for developing robots that can do it. Tele-oporation could be possible, but the rapid changes in wind and sea might be too fast for a human to react in time.

Robots are already helping us to explore [Mars](https://mars.nasa.gov/mer/home/) and this seems to be a good idea for exploring space. Since humans need air to breath, space isn't a great place to try and work. When we go into space we need a lot of protective equipment to stay ~safe~ alive. Another problem is the communications delay between earth and the robot, which makes tele-oporation difficult or impossible. The delay between Earth and the Moon is about 1.3 seconds, but the delay between here and Mars is about 3 minutes! If we can tell that our robot is going to fall down a hole and it doesn't stop until 3 minutes __after__ we've told it to, our robot's going in the hole!


## Verififyig Safety

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