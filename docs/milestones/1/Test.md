# Milestone 1. Project Plan Complete - Test


## PROJECT INFO


* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)



* File: Milestone-1/Test.md

* URL: https://github.com/June907/CS350-Team/tree/master/Milestone1/Test.md

* Git Repo: https://github.com/June907/CS350-Team


### Milestone 1. Project Plan Complete

Role: QA Engineer - Test

Goal: Test Plan

* Outline of testing methods
* Setup structure for testing
* Log issues
* Document how to log issues



## Easel - Test Plan

Our test plan is broken down into five levels of increasing detail outlined below. 

About one quarter of our total engineering time will be spent on testing. We anticipate the entire project to take roughly 1000 hours, 250 of those hours will be spent on testing. 


### Testing Levels 


#### Level 1 - Test Plan

* Outline the major types of testing 
    * Manual Acceptance Testing - A person uses the application and observes what happens.  The test script describes scenarios that the tester must go through.
    * Django unit test - Automatic tests that may start with a blank database.  These tests can be very fine grained or run the entire system.
    * Hammer test - These tests execute automatic scenarios that exercise the entire system.
    * Quick test - The test is only used during development to iterate on a single function.
    * Page test - This test runs on “requests” Python package and gets web pages from a live server it is used to see if pages on the internet are changing.
    * Selenium Page test - Firefox and Chrome are used to obtain pages and look for specific HTML elements.
    
Easel testing

* Due to limited time frame of this project testing will be focused on essential testing methods. 
* Essential testing will include
    * Manual Acceptance Testing
    * Quick Tests in development
    * Page Tests (using "requests" Python package on PyTest)
    

#### Level 2 - Test Area

* These are the main areas of the app where testing will be focused
* Product subsystems
    * Views
    * Database
    * Gradebook view
    * User accounts
    * Reports
    * Diagnostics

#### Level 3 - User Story Test

* Each Test Area is decomposed into a number of User Stories.  
* Each User Story is defined as a User Experience (UX) that is documented in the requirements
* A User Story Test outlines how the UX scenario will be exercised and verified
* Examples:  Student Register UX,  Change Grade UX, Register Student Grade UX

#### Level 4 - Test Script

* Each User Story  is decomposed into a number of User Scenarios.  
* A Test Script outlines how the User Scenario will be exercised and verified.
* Examples:  Student Register UX
    * Student can register
    * Student can login
    * Student can logout
    * Only students can see grades

#### Level 5 - Test Case

* Each User Scenarios  is decomposed into a number of specific features that the app implements.  
* A Test Case outlines specific behavior to be exercised and what the expected results are.
* Examples:  Students can register
    * Successful registration
    * Error for bad email, name, or already enrolled
    * Student can login after registering
    * Errors prevent student from being enrolled


## Hierarchy of Test Details

### Complete Test Plan

This hierarchy can be documented to highlight the key artifacts.

* Level 1 - Test Plan (1)
* Level 2 - Test Areas (7-10)
* Level 3 - User Story Tests (50-100)
* Level 4 - Test Scripts (200-400)
* Level 5 - Test Cases (1000-2000)

### Essential Test Plan

As stated above testing will be limited to the essential testing at first. Time permitting we will ad more testing into our overall project plan.

Easel Testing Hierarchy

This hierarchy can be documented to highlight the key artifacts.

* Level 1 - Test Plan (1)
* Level 2 - Test Areas (4)
* Level 3 - User Story Tests (16)
* Level 4 - Test Scripts (64)
* Level 5 - Test Cases (256)

Over the course of the project we plan to spend about 250 hours testing and can focus on the 250 Essential Test Cases.  This makes testing totally predictable and manageable.  If there is enough time we can do more but we are guaranteed to get the most important stuff tested.


## User Register - Test Script

Manual Testing - live user clicking buttons

Test Cases - Student Register

* Scenario 1 - Guest Access
    * Guests can see system view with Welcome
    * Not logged in displayed
    * Menu has links to Register, Sign in

* Scenario 2 - Register New Student
    * Student can register
    * Error for used email
    * New users are created
    * Dropping a Student removes the user record
    * Existing user records are used

* Scenario 3 - Student Access
    * Student can log in successfully
    * Student can see course view with Student Settings and Welcome
    * Login displayed
    * Logout menu item
    * Menu has links to Courses, Calender, Inbox
    * Dropped Students can not log in

* Scenario 4 - Teacher Access
    * Teacher can modify grades
    * Teacher can update assignments


### Setup structure for testing

We will start by doing manual testing only. For the first two milestones will not need to have any automated testing setup. 

The above test scripts cover the scope and high level direction that the testing will 
take.  An example Level 4 - Test Script has been included to illustrate the kind of 
Test Scripts that will be developed later on in the project.


### Log issues

The Github issues tracking system will be used to track all known items and remaining
work.

The Product Backlog will be an Issue in the BookBuilder project.  It will track the 
priorities for the current Sprint.  The functionality that is expected for the next
milestone will be documented in the Product Backlog.

At the end of the Milestone all work listed in the Product Backlog must be complete.
Any unresolved issues must be logged within the Github issues list.
