# Milestone 4. Functionality Complete - Test


## PROJECT INFO

* Software Project Plan - Easel

* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)



* File: docs/milestones/4/Test.md

* URL: https://github.com/Twitter-Clone/twitter-clone-documentation/blob/master/milestone-4/Test.md

* Documents: Documents/Twitter-Clone

* Git Repo: Twitter-Clone




### Milestone 4. Functionality Complete



Role: QA Engineer - Test

Goal: Continuous integration

* Build and test with every push
* Implement Travis (CI tool)



## Twitter-Clone - Continuous integration

### Build and test with every push
* For milestone 4, we were able to test that our views were working. 
* Views that we were able to get working were user_list, user_detail, and tweet_list.
* views.py can be found at: https://github.com/Twitter-Clone/twitter-clone-api/blob/master/tcapi/views.py
* We implemented tests that cover the different views.
* One major issue that we faced was getting all of our settings configured. We had issues with the API not working correctly, so manual testing was definately used here.


### Implement Test Coverage
* For test coverage, we have a CI/CD pipeline that was created using Github Actions. 
* The CI/CD pipleine has two jobs which are located in two of our repositories. 
* The first job is for building the docker container. This would include updating it when changes have been made. 
* The second job is responsible for making sure that we are writing clean Python code that follow basic Pep8 standards. 
* Django testing is done mainly through so called 'second job'.
* Github Action for Docker container: https://github.com/Twitter-Clone/twitter-clone-api/actions
* Github Actions for clean python code: https://github.com/Twitter-Clone/twitter-clone-frontend/actions