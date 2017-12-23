---
layout: post
title:  "My Code Club Year"
date:   2017-12-23 15:06:19 +0100
categories: [codeClub]
---

As the year comes to an end, I'd like to say that I've had a lot of fun volunteering with one of the many Code Clubs here in York. I've managed to help run three clubs this year. My first was an intermediate club (which I wrote about [back in August](/codeclub/2017/08/01/codeClub.html)). Then I ran both a beginner's and intermediate's club (alternating each week). All three of these were hosted by Alex at the [York Explore Library](https://www.exploreyork.org.uk) <a href="https://twitter.com/YorkLibrariesUK">
  <i class="fa fa-twitter-square fa-1x"></i> https://twitter.com/YorkLibrariesUK
</a> in the middle of York.

For the two most recent clubs, we had 2 little programmers in the beginners club and 4 in the intermediate. Both me and Alex were a little disappointed with the turnout (though very pleased with the little programmers we did get in the club). My two observations regarding the turnout are that, potentially, having the club on a Saturday in the middle of York (which _sounds_) very convenient, might not have been that useful (especially near Christmas time!); and that most of the little programmers had done quite a bit of Scratch programming at school, so maybe the beginner projects were a little too beginner for them.

Anyway, speaking of the Code Club's scratch projects...

### New Code Club Website

After attending a Code Club Meetup (organised by Anna Pearson <a href="https://twitter.com/codeclubyandh">
  <i class="fa fa-twitter-square fa-1x"></i> https://twitter.com/codeclubyandh
</a>) and being shown the [new website for Code Club's projects](https://www.projects.raspberrypi.org/en/codeclub) I started using it during both of the clubs I was running.

I've found that the new layout, where a project's major steps have a page each, to be really helpful for keeping our little programmers a little more focussed. The layout makes it easier to keep track of progress, and I can imagine it would be a lot easier to use on a mobile device than the previous layout (though I've not tried this myself, so it's just a guess). One minor improvement would be to make it more obvious if the project has a resources pack to remix or not. I've found that a lot of the little programmers have steamed past the second page (where the link may or may not be) and then gotten stuck trying to find the right sprite. But, it's a very minor issue that's usually easily solved, definitely not a show stopper.


## Impossible Games

Something that has remained constant across the three clubs I've run so far is that the little programmers the  _really_ enjoy making the games **impossible**! A few simple examples include:

* Lots of enemies or super-fast enemies,
    - Sometimes this happens by accident, because the script is missing a `wait` block, and it looks funny so they keep it like that,
    - Other times, it happens when they start tweaking the numbers, curious to see what will happen;
* Loosing <s>millions</s> far too many lives when hit by an enemy
    - Sometimes this happens because the 'hit' script is triggered multiple times (because the player character and the enemy are still touching),
    - Other times, it can be more curious tweaking of the numbers in the `change score by` block.

Another common theme has been impossibly dangerous enemies. For example, one little programmer designed a storm cloud that appeared every `x` seconds and darts across the screen, killing whatever it touches. (Oh yes, did I mention that it is un-killable? Because, of course it is!)

Finally, my personal favourite, was a version of the [Catch the Dots](https://projects.raspberrypi.org/en/projects/catch-the-dots) project. The object of the game is to rotate a wheel to match up the red, blue, and yellow sections of the wheel with the red, blue, or yellow dots travelling towards it. Clearly, this is a game where _colour_ is important. This particular version of the game included an entirely black wheel and three sets dots in a matching shade of _noir_. I, lovingly, called this version 'Goth Mode'.

I have no idea why the little programmers so often delight in making games impossible to play. Perhaps it's enjoyment of their new-found control over the computer, which is usually just a black box. The ability to give a computer instructions that it will follow is what I first enjoyed about programming.

Sometimes, the little programmer's instinct to make impossible games can be harnessed and redirected into making a game with progressive difficulty, to make it more challenging for the player. This takes some work and concentration (not to mention more than a little decentring) so it's not always possible or appropriate for little programmers of all ages, but if it's possible then it can be very worthwhile. It challenges the little programmer to think about how to engage the player of their game, work hard at sensibly altering their own code (without an explicit set of instructions or requirements), and can get a little more out of the project (which is especially useful for more advanced little programmers).
