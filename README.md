# Attentive

The cute smart assistant framework that lives on your desk. Like a rubber ducky, but way better.

## Project Pitch

N.B. This pitch targets software developers, but the product will be generalized to address the needs of common folk soon.

### Problem Statement

The rubber ducky hasn't been iterated upon for 56 years.
Rubber ducky debugging has long been regarded as the golden standard for eliminating undetectable stupidity from code.
First proposed in *The Pragmatic Programmer* in 1964, the rubber ducky has since proven itself in the workplace as an intimate programming companion.

Many software developers, however, find it difficult, or even ridiculous, to use their imagination to begin a conversation with a rubber toy when trying to squash debilitating bugs in their code.
Rubber duckies don't appear to be listening to you, they provide no auditory or visual feedback, and they are only as effective as the user's imagination can carry them.

When developers can't, or refuse to, use a rubber ducky for debugging undetectable bugs, they turn to their colleagues to fulfill the role of the inanimate rubber toy.

#### Supporting problem

Software developers tend to overwork themselves and hate planning, estimating, remembering, and making non-code-related choices while they're trying write code.
Current solutions for project management in software development are geared toward team productivity and lack intimate personal management features that devs so dearly need.
Unfortunately there is a lapse in time management and organization solutions for the individual engineer; and personal tools that do exist, generally, don't integrate nicely with the engineer's work domain.

The workplace can become a stressful environment when you're required to be an expert in your field and be your own secretary too.

### Hypothesis

If we can make the rubber ducky more helpful and require less imagination to use, the proven rubber ducky debugging technique will become more accessible to the majority of developers.
This, should in turn, improve productivity in teams. Only one engineer will be needed to detect obfuscated stupidity in their code.

#### Supporting hypotheses

- If Attentive is cute and can alter its appearance to look more attentive when you talk to it, devs will use it more.

- If Attentive is easy and intuitive to communicate with, like a well trained dog, it won't feel awkward talking to it for help.

- If Attentive happens to also be a tool the developer uses to manage their day, a rapport will form by the time bugs are in need of squashing. This rapport will conveniently define Attentive as a helpful *thing* in the mind of the dev.

- If developers can have a small private stand-up meeting with Attentive every day, they'll be able to be honest with themselves about tasks and deadlines without the stress of their entire team being there.

- If Attentive can follow along within your development environment, and prompt you for explanations, it'll only feel natural to enlighten the toy with your stupidity.

### User Population

We will focus on software developers who don't already use a rubber ducky as a debugging tool, and work with a few employees at Genetec Inc. to get feedback.

### Prototype

#### Loveability

In the aim to improve overall mental health and facilitate talking to an inanimate object, the Attentive platform will be embodied by a plush toy dog. It will be outfitted with a raspberry pi, servo motors, and a camera.

For human facial detection and orientation estimation, the Google Cloud Vision API will be used.

#### Communication

There will be a Microsoft Teams integration for talking to your little buddy when you're away from your desk and for reliable notification features.

#### Implementation & Integrations

Business logic will be implemented in Google Functions with the help of the Cloud IoT Core and Pub/Sub so as to provide a scalable and modular backend.

Software development environment integration will be with Visual Studio Code.

Productivity software integrations will aim to include Microsoft Teams, Outlook, and Jira (if time permits).

## Next Steps







<!-- Secretaries are specialists in managing an individual as part of a larger team and can offload plenty of work, but they're not available 24/7, won't normally tend to your mental health, and they're expensive.


- Rubber duckies are hard to talk to

Everyone has their reasons for diving into a project or codebase and only surfacing for food and coffee.
For me, it's to escape all my other responsibilities that I need to track.
Planning, estimating, remembering, and making choices are all things I'm horrible at. 
Thankfully humans have invented to-do lists and calendars. -->

<!-- Often during work, people are met with moments of uncertainty during which they distract themselves with something like a coffee or snack. Once back at their desks they're met with the same problem from which they originally got distracted. -->

<!-- Surgeons often have to look away for guidance to a navigation system outside
the sterile area in the operating room. This can be detrimental to the task at hand and lead
to errors or extra time in surgery. -->

<!-- ### Hypothesis: -->
<!-- Auditory displays use sound to give users information. We believe that we can
use sound cues to help guide a surgeon to a given target much more accurately and
quickly. -->

<!-- ### User population:  -->
<!-- We will focus on neurosurgeons, and work with a few surgeons at the
Montreal Neuro to get feedback. -->

<!-- ### Prototype: -->
<!-- As we will build on an existing open-source framework (IBIS), we believe, that
we should have no problem to develop a plug-in that allows for data sonification of distance
information to a target. We will interface the IBIS system with an external audio synthesizer,
and developed an IBIS audio plugin capable of transmitting open sound control (OSC)
messages from IBIS to the pure data audio programming environment. -->



<!--### Rubber Ducky Plugin --- for stupidity in code
"I'm running my code, but it keeps crashing when it tries to instantiate this here object. I'll go find my friend and explain to him every line of code until I realize the stupid mistake I made. I'll then proceed to thank him and tell him to get out of my cubicle so I can get back to work."

### Productivity Plugin --- for ADHD at work 
"I come in to work on Monday, and login to my computer. Presented with my desktop background and a few (okay, a lot of) icons, I hit WINDOWS + L and get a coffee. Maybe a coffee will help me decide what to start with today."

### Motivation Plugin --- for depression at home
"I wake up in the morning, but I really don't want to get out of bed. There are too many people I have to talk to. There's no point anyways, what difference will it make if I wake up today." -->


