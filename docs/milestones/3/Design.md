# Milestone 3. Core Features Implemented - Design


## PROJECT INFO

* [Software Project Plan - Easel](../Index.md)

* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)



* File: Milestone-3/Design.md

* URL:https://github.com/June907/CS350-Team/new/master/docs/milestones/3/Design.md


### Milestone 3. Core Features Implemented



Role: Designer - Design

Goal: Component Design - API

* Prototype - development spike of core functionality
* Implement data models
* Implement views
* Implement URL routes



## Easel - Component Design - API



### Prototype - development spike of core functionality
  * One core set of features that the team decided to do for this project are:
    * Users can register for an account.
    * Home page dashboard will show relevant information.
    * Users can edit their account such as changing the username/password.
    * Users can sign into their account.


### Implement data models
* Data models are included for Courses, Assignments, and Submissions

 ### Courses
 * Title
 * Instructor
 
 ### Assignments
 * Title
 * Due Date
 * Points Possible
 * Course
 
 ### Submissions
 * Title
 * Assignment
 * Student
 * Time
 * File
 * Points Received
  
  Data model can be found at: https://github.com/June907/CS350-Team/blob/master/project/project/models.py
    


### Implement views
* So far, views have been implemented for the home and about pages.  
* The views file can be found at: https://github.com/June907/CS350-Team/blob/master/project/project/views.py
* Views for the course list and assigment list still need to be implemented. 
* As of right now, the team has one tests.py file which is mainly responsible for testing the connection to the API. 


### Implement URL routes
* URL routes have been initialized for the home, about, and register pages.
* More URL routes will be initialized for the courses, and assignments by the next milestone. 

### Document Engineering Practices
* As a team, we all work best when we are talking to eachother and sharing out screens. This allows for those of us who are not doing to acutal
code to take notes and observe what is happening. 
* We work best as a team when we communicate what we're doing with each other. We have daily meetings to allow everyone to explain to the rest of the team what they've been working on and for us to plan our next steps.
* Rules for TDD: 
* 1. Work together
* 2. Code in small chunks
* 3. Test code constantly
* 4. When a bug is encountered don't move on until it is fixed
* 5. Document issues
