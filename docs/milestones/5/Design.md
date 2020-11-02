# Milestone 5 - Design

## Developer - Erik Halenkamp
## PROJECT INFO


* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)



* File: docs/milestones/5/Design.md




### Milestone 5 - Oversee Code and Test Completion



Role: Programmer - Design

Goal: Oversee Code and Test Completion

* ~~Implement all required features
* ~~Improve code structure
* Ensure test quality
* ~~Measure all remaining work

## Implement All Required Features

* All required views are implemented for both teachers and students. Notable additions for Milestone 5 are the instructor views for adding, deleting, and updating assignments.
* Grade page displays grades based on submissions already posted, though there is no way yet to submit a submission. This is not a required feature, but will be implemented soon to fix calculations.

## Improve Code Structure

* Revamped URL Path (10/23/20)
  * Each page will have varying CRUD permissions based on whether user is a student or instructor of the course in question
  * ![Revamped Student URL Path](/docs/milestones/5/studenturlrevamp.png)
  * ![Revamped Instructor URL Path](/docs/milestones/5/instructorurlrevamp.png)
* URL Path Update (11/1/20)
  * Grades are now displayed on two pages, the first of which will display a hyperlink leading to the second for students, and a list of students for the instructor. The second page houses individual student grade data
  
## Measure All Remaining Work

* To-Do
  * Assignment submission (create/update views for students)
  * Template updates to flesh out look & feel of application
  * Situational awareness, less-common views, and bugfixes
  
Overall, the website's core functionality is complete, and most remaining work will go into fleshing out the application to create a finished product.

