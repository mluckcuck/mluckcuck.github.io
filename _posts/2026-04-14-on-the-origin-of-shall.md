---
layout: post
title:  "On the Origin of Shall"
date:   2026-04-14 10:33:19 +0000
categories: [academia]
section: Blog

---

#### "Shall": The Pivot Point of Structured Requirements

Now firmly ensconced at the University of Nottingham, I co-teach the _Software Specification_ module which teaches students about software requirements and why we bother developing them. One of the key points of the module (and where my teaching is focused) is that writing requirements in unstructured natural language (e.g. English) is a really bad idea, so we introduce them to structured ways of writing requirements instead. 

Structured requirements (at least the formats I've seen) often use the keyword "shall" to separate the requirement's trigger from its response: when the trigger happens the system should behave as the response describes. This is true in the [Easy Approach to Requirements Syntax (EARS)](https://alistairmavin.com/ears/) and the newer [Formal Requirements Elicitation Tool (FRET)](https://github.com/NASA-SW-VnV/fret) (which is what I teach on the _Software Specification_ module). Using "shall" like this is also mention in Ian Sommerville's [Software Engineering textbook](https://software-engineering-book.com/) (in a list of recommendations for adding structure to natural-language requirements) "Mandatory requirements are requirements that the system must support and are usually written using 'shall'" (Chap. 4, p. 122, 10th Edition). 

It makes sense to use "shall" for mandatory requirements (Sommerville suggests using "should" for optional requirements) but why "shall"? In my first year of teaching on the _Software Specification_ module, a student asked Julie (the module leader) why we use "shall", why not "will" or "must"? A chance purchase at a second-hand bookshop may have given me the answer.

I was at [Kedleston Hall](https://www.nationaltrust.org.uk/visit/peak-district-derbyshire/kedleston-hall) for a walk and (of course) popped into the second hand bookshop. One of the books that I bought was The Plain English Guide (First Edition, 1995). (The newest edition of this book, Fifth, has a new title [Oxford Guide to Plain English](https://global.oup.com/academic/product/oxford-guide-to-plain-english-9780198844617).) 
![Front Cover of The Plain English Guide]({{ site.url }}/file/images/plainEnglish.png)
In explaining why _not_ to use the word "shall" it explains the grammatical rule for when it should be used, which I think is why "shall" is used in requirements.

## The Origin of Shall(?)

![From The Plain English Guide "The old rule was that when writing of future events you would say 'I _shall_; you will; he/she/it will; we _shall_; you (plural) will; they will' but that when writing of promises, obligations or commands, the _wills_ and _shalls_ would change places."]({{ site.url }}/file/images/plainEnglish2.png)

The Plain English Guide explains (on page 36) the rule of when to use shall and when to use will: "The old rule was that when writing of future events you would say 'I _shall_; you will; he/she/it will; we _shall_; you (plural) will; they will' but that when writing of promises, obligations or commands, the _wills_ and _shalls_ would change places." That is, when the future event is a promise or obligation, the text should say "you shall..." or "it shall...". The book continues, saying "the Old English root of 'shall' is 'sceal', meaning 'I must' or 'I owe'. 

Given that a requirement is a future obligation or promise of a system (which should really be referred to as 'it'), I think this makes a lot of sense. We are obliging the system (via its developers) to perform some behaviour; another way to look at it is that we are promising that the system will behave like this. In either case, it is the system that is involved in the future behaviour so the rule says _shall_. 

I think that another useful reason to use "shall" in requirements is that it sounds so old fashioned now, so it sticks out. People are less likely to casually use the word "shall" in other bits of the requirement, which helps preserve it as the pivot point of the requirement.



