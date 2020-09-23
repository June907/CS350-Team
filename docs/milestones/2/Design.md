Milestone 2. Technology Proven - Design
=======================================

PROJECT INFO
------------

-   [Software Project Plan - Easel](../Index.md)

-   Other Roles - [Requirements.md](Requirements.md) ,
    [Design.md](Design.md) , [Code.md](Code.md) , [Test.md](Test.md)

-   File: 2/Design.md

-   URL:
    https://github.com/June907/CS350-Team/tree/master/docs/milestones/2/Design.md

### Milestone 2. Technology Proven

Contributor: Erik Halenkamp - Week 2 Design Specialist

Easel - Software Architecture
-----------------------------

### Design Around User Stories

User Stories

*Student *Classes: Cannot create, destroy, join, or leave. Must be
placed into by class owner (Teacher), and can only then participate. Can
view overall class grade for themself. *Assignments: Can submit/resubmit
files and view individual grades. Cannot create, destroy, or update
assignments. *Discussions: Can contribute to discussions and edit/delete
their own posts. Cannot create/edit/delete others' posts or
create/delete discussions. *Teacher *Classes: May create and delete
classes as they please and add students to them. Can view and edit
overall grades for all students. *Assignments: Can create, delete, and
edit assignments, including the file type required, and students'
individual grades. *Discussions: Can create/delete discussions and
delete all posts. Can create and edit their own posts.

### Design Architecture

-   Apps = Data + Views
-   The design for the app requires designing the data models and the
    Views that will be implemented.

(![Image of
Wireframe](https://github.com/June907/CS350-Team/tree/master/docs/milestones/2/hierarchy.png)

### Data models

Data Classes and Database Tables (Refer to Data Hierarchy for a Better
Understanding)

-   Teacher
    -   user\*
    -   name
-   Class
    -   teacher\*
-   Student
    -   user\*
    -   name
    -   classes\*\
-   Assignment
    -   class\*
    -   submissions
-   Discussion
    -   class\*
    -   posts

“\*” makes a link to another table. This is implemented by a foreign key
relationship between the two tables. This implies belonging

Example: Assignments are made as a child of a class that only students
belonging to that class can interact with

### App Views

-   Users
    -   Register Author
    -   Register Reader
    -   User Admin
-   Books
    -   Create Book
    -   List Books
    -   Edit Book
    -   Read Book
-   Chapters
    -   New Chapter
    -   Edit Chapter
    -   Read Chapter

### Phases Of Implementation

-   1 - Proof of concept
    -   Milestone 2
    -   Define the Data Models
    -   Use admin views to simulate user stories
-   2 - Prototype
    -   Milestone 3
    -   Implement Custom View for User Stories
    -   Users
        -   Register Author
        -   Register Reader
    -   Books
        -   Create Book
        -   List Books
        -   Edit Book
        -   Read Book
    -   Chapters
        -   New Chapter
        -   Edit Chapter
        -   Read Chapter
-   3 - Core features
    -   Streamline and improve UX
    -   Deal with Errors
-   4 - Functionality complete
    -   Build out logging
    -   Fix errors
    -   Performance
    -   Usability testing and improvements
-   5 - Code Complete
    -   Fix all defects
    -   Implement 100% test coverage

