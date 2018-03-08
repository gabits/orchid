# Guidelines for the Codebase

This is where the main concepts for development are described. Design and implementation should be guided by those and new ideas are documented after trial as they become adopted. Currently the guidelines serve more as reminders for me when structuring the code, or once complexity strikes and development work is blocked, where there is a need to take an overview of the intended Architecture. 

**Code design also involves structuring the process of implementation** and this file should be a reminder for it.


## Architecture

In all languages and frameworks used, the code should be as self-documented as possible.
All apps and the interaction between them should be modular; all abstract concepts must be kept separate from concrete implementation.


### Tests

Development should be focused in *Test Driven Development* with the purpose of **guiding implementation**, keeping it as **DRY and simple** as possible, and to guarantee a system that is *maintanable* and *reliable*.

Unit tests and code related to specific implementation of each app should be contained within their directories. Integration and system tests should be kept external to the application.


### Comments
Those should follow each language's responsibilities; specific content for development should not be exposed to user-facing code such as static files and vice-versa.


## Python

**Documentation:** DocStrings must be present to every public method and preferably for private methods as well.

**Naming:** In order to have this system easy to develop with in the future and allow other developers to have a deeper contact with it, there must be a strong concern around naming which should be kept as specific and dry as possible.


## HTML and CSS

**Comments:** should be included mostly to organise, hierarchise and structure the code and reinforce its readability.
