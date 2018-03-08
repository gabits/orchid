# Guidelines for the Codebase

## Architecture
In all languages and frameworks used, the code should be as self-documented as possible.
All apps and the interaction between them should be modular.

### Tests
Development should be focused in Test Driven Development with the purpose of guiding implementation, keeping it as DRY and simple as possible, and to guarantee a system that is maintanable and reliable.
Unit tests and code related to specific implementation of each app should be contained within their directories. Integration and system tests should be external to the application and not .

### Comments
Those should follow each language's responsibilities; specific content for development should not be exposed to user-facing code such as static files and vice-versa.


## HTML and CSS
Comments: should be included mostly to organise, hierarchise and structure the code and reinforce its readability.
