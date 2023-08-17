1. Project Overview
The task was given to create a website, this website had client specific requirements it had MVP and Wishlist. The MVP was to create a website with functions that included cart checkout payment proccing logic, CREATE READ UPDATE DELETE function on cart. Wish list included features that client wanted but were not essential. My project did not include any item from the Wishlist. 

The project consists of using the following:
Kanban (via Jira) for project management and agile framework
Git as the version control system
GitHub for source code management
HTML, CSS, JavaScript and Bootstrap for front-end development
Python as the back-end programming language
Flask as the API development platform
MySQL/SQLite as the database management system originally MySQL was used but SQLite was used later till end of project for ease of use.

2. How I used Agile Methodology
In the morning of each day a standup was done, in which task to be done was talked about, blockers preventing from tasks and solutions on how to remove said blockers were thought up off. A retrospective meeting was done at the end of every sprint, for me a sprint was finishing a feature.
From kanban board when a story was moved to done it was the end of that story sprint.

3. How I used my Kanban board
Epics, User Stories, Tasks and Acceptance Criteria
Initially there were 9 user stories created one for each of the html page and then some were created for the logic or functioning of the page. Each user story consisted of having description, a long with the as user I want so that statements, it had acceptance criteria and also included child issues which was the main issue further broken down.
Risk Assessment
This displays some of the risks that I may have encountered during the project, including the steps to mitigate any negative impacts. Based on this risk assessment, I was able to make changed to my code to decrease the possibility of the risks happening.

ERD Diagram: ![image](https://github.com/akber360/shop/assets/139133081/876ecd48-bd19-43c6-8ae6-1eb398894232)

DB relationship explained

Relationships
Customer to Order: One-to-Many

A customer can place many orders.
An order is placed by exactly one customer

Order to OrderDetail: One-to-Many
An order can consist of multiple order details
An order detail refers to one order.

Product to OrderDetail: One-to-Many
A product can be part of multiple order details.
An order detail refers to one product.
Evolution of Ideas
Originally I wanted to create a website for icream, but it had a lot of flavours and not many categories so I went for EARTH WIND FIRE AIR categories. 

Summary of Kanban board
![image](https://github.com/akber360/shop/assets/139133081/7a833774-6196-4f0f-abae-d17a6e922ce2)
this is what the kanban looked like during the phases as you can see I have a To do in progress and done sections this is where stories would move as they progressed along.
![image](https://github.com/akber360/shop/assets/139133081/03dbd68c-0ea1-4417-895c-b6355ba74ba8)
Here is an example of how a user story would look. consisintg of child cases and user story statmenet 

Git Branching
![image](https://github.com/akber360/shop/assets/139133081/a010a6eb-a93b-43f9-a258-3cba96a6e91c)

using git as source control mangagment, I used the branch features, where each branch would be a feature that I would be working on e.g. Database
payment add-to-cart. after the feature was developed it would be pushed and main would be merging and pulling it in. so at the end of the project main had all the uptodate code.
![image](https://github.com/akber360/shop/assets/139133081/64b14cf6-02dd-470d-8511-4d72032e3c3a)
Exmaple of branch merging.
![image](https://github.com/akber360/shop/assets/139133081/ae04730a-6a1e-4e5a-b9e1-e1f1ee3a8c01)

py-test
![image](https://github.com/akber360/shop/assets/139133081/5d73c9cf-c57b-4bcf-8627-ff46e85fbae1)

I created simple assestion test. and setup the three states create which loads up the app setup which loads the database with dummy data and teardown which removes all dummy data so that when the tests are ran there is no old data running to cause conflict
There was three test to see if code would =200 and =302 and if product id=1.


Jenkins
Jenkins was setup and running taking the github repo and building from their via the shell commands that were given. the app.py file was running and jenkins was running a server. 
![image](https://github.com/akber360/shop/assets/139133081/5236da7b-a38e-46d9-abfe-373c312d141c)
![image](https://github.com/akber360/shop/assets/139133081/9c0816a2-3235-4f1b-aeaf-029961c1be70)
![image](https://github.com/akber360/shop/assets/139133081/8fd22452-68ff-4781-97d2-ffee145a14ec)

Future Steps: further analysis, what would i do next if i continued with this project id add this feature create new database relationship etc.

Licensing: vscode sqlite jenkins, Jira Kanban

Contributors: w3schools, Qa community, bootstrap, stack overflow ,EARL’s Git repo all flask excercises

Acknowledgements: all QA trainers and Earl was super helpful in answering my questions.

risk assesment
![image](https://github.com/akber360/shop/assets/139133081/24b8b668-c047-4045-bf16-ca100dc1668a)

The following photos are the development lifecycle, showing my planning process, webpage logic, database design idea.
![image9](https://github.com/akber360/shop/assets/139133081/e6877e61-0bb5-4d00-ba8a-bacc6fe11245)
laid out all the html pages I would require

![image8](https://github.com/akber360/shop/assets/139133081/82f09b1b-3a27-474e-8b40-9367b67459b0)
first mock of homepage and listing acceptance criteria on what is needs to looklike and be able to do.
![image6](https://github.com/akber360/shop/assets/139133081/879bb989-d740-4b19-89c6-2967a7819fce)
Further creating user stories for the homepage

![image7](https://github.com/akber360/shop/assets/139133081/75945311-5ef1-4a6a-b9b3-45300181855a)
Here I made HTML route, showing how from home page user can naviagate to many places but highlighting the process from cart to checkout to payment page.


![image5](https://github.com/akber360/shop/assets/139133081/03d9d198-f079-4970-b576-72f8bf4d3d73)

Navbar requiremnts 

![image4](https://github.com/akber360/shop/assets/139133081/dcc600f4-9d9e-4642-be72-5caf9512da39)
init .py file requirements

![image3](https://github.com/akber360/shop/assets/139133081/5a741683-3c86-4d4d-bf95-8ed0db0c4975)
Databse design inc ERD mock + payment page requiremtns.
![image0](https://github.com/akber360/shop/assets/139133081/cca4ca91-546a-43ad-af4b-311790d430c2)
payment page requiremnts.

![image2](https://github.com/akber360/shop/assets/139133081/6e603b11-c742-4ba1-8f98-dc65520fce8c)
Jenkins setup instrcutions 

![image1](https://github.com/akber360/shop/assets/139133081/35a70201-dc2e-4024-a802-83ddc6764f6e)
All cart redquirments as well as project task outline to be completed by monday. and outlining wednesday tasks.




