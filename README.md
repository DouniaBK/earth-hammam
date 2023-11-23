![Earth Hammam](static/images/site-screenshot.png)

Earth Hammam where you rekindle your soul, treat your body and leave your stress behind in an invigorating wellness experience. The luxury Earth Hammam facility is inspired by the North African
landscape and thus the site mirrors the esthetic and architecture of the facility. The site design is inspired by the rose-hued buildings of Marrakech
and the surrounding olive groves. Dedicated to personal wellness the site design is serene, minimalistic and timeless ensuring a calming and relaxing user experience. 
The site brings the serene Earth Hammam experience to the world, inviting visitors from around the world, to book appointments for treatments at the facility, buy their entrance tickets prior to their visit, and buy the signature Earth Hammam products inspired by the scent and atmosphere of the hammam. Furthermore, the exclusive Earth Hammam treatment packages are available to purchase as gift cards making it a perfect gift not only for tourists but also as a corporate incentive. The gift cards can be purchased online and redeemed at the facility.

# Table of Contents
## Goals
* Target Users
* Visual Design

## Features
* Page Elements
* Additional Features
* Features Not Yet Implemented
## Information Architecture
* Database Structure
* Data Models
## Technologies Used
* Languages
* Libraries
* Packages
* Platforms
* Other Tools
## Testing
* Automated Testing
* Manual Testing
* Bugs
* Accessibility
## Deployment
* Local Deployment
* Heroku Deployment
## Credit
* Code
* Content

# Business Goals
## Target Audience :
The site is designed for Earth Hammam tourists, influencers and business travelers who would like to visit the facility during their trip to Marrakech, it is designed to attract tourists, influencers and business travelers from around the world who are tempted by this luxury yet authentic experience to indulge, be pampered and promote the facility.
The treatments can be bought in the form of a gift card which makes an ideal corporate incentive targeting corporate individuals as well as influencers. The gift card option incites individuals to go to the facility and spend more benefitting the business.

## Gift Card Business Model:

The Earth Hammam profits when individuals buy their gift cards online whether for personal use or as a gift. Earth Hammam profits as well when the gift card has not been redeemed. The booking system gives the sense that the gift card can be redeemed whenever the client wants and thus encourages clients to buy gift cards online as long as they have the freedom of booking within the next five years. 

## Site Admin:
The admin managing the site of Earth Hammam has access to a frontend and backend admin page allowing them to perform the following daily tasks:
1. Manage Merchandise: the admin can add, edit and delete items sold on the site.
2. Newsletter: The admin can send newsletters with a handy email function thanks to a package called "Django-TinyMCE", which allows the admin to format the newsletter content as they wish. 
3. Testimonials: The admin can manage testimonials from the backend, publishing, deleting and updating testimonials
4. Booked Appointments: The admin can view and edit all the appointments made by the clients, assisting them in managing personal as well as helping clients if assistance is needed
5. Orders: The admin is able to see all the orders made by the clients thus they can complete the shipment procedure.
6. Manage subscribers: the admin can view and manage subscribers to the newsletter allowing them to manage all marketing aspects as well as further market estimations.


## Visual Design:
A folder with further design elements can be accessed [here](ADD LINK) as well as the [flowchart](ADD LINK).
### Site Design:

This particular site is dedicated to wellness and relaxation transporting the user to a serene space inspired by the rose-hued architecture and landscape of North Africa. The site has an earthy North African color pallet, aiming at embracing healing, rejuvenation and indulging in a promise of luxury and pampering. The site has a minimal aesthetic and color palette to avoid sensory overstimulation often and offers an intuitive workflow leading to, buying, an entrance ticket, a product or even better a treatment gift card and then if logged in, booking a session and starting a journey of mental repair and pampering. Furthermore, the site contains key information about the facility in the section dedicated to the Hammam, accessible from the navigation, such as a carousel with images inspiring luxurious wellness with unique architecture, authentic ancient healing treatments and beauty rituals. Moreover, a section describing the exclusive offers Earth Hammam provides with links leading the user to shop. Finally, a Testimonial section is added to provide a sense of trust and professionalism.

### Fonts:
The font family and style used are:

   * font-family: 'Montserrat'
   * Lead feature from Bootstrap
### Favicon:
A minimalistic favicon with the word 'Hammam" has been added giving the site a professional look. The favicon has been generated using [Hoststar](https://www.hoststar.ch/de).
# Features
## Page Elements:
The site contains various pages to introduce the user to the services and approaches Earth Hammam offers. The following pages are accessible from the extendable navbar on top:
### Home page:

The Home page welcomes the user into the serene world of wellness by Earth Hammam, with an elegant image of a woman being pampered with a massage and a title inviting the customer to "Treat the body and ease the soul" amd button leading the user to discover Earth Hammam Marrakech. The button leads to the Hammam section of the site where the overall facility is described.

### Hammam:

    1. The first section features the Earth Hammam facility including a brief description of what Earth Hammam stands for, a carousel with images of everything the facility offers such as a hammam, pool, soak tub, aromatherapy treatments and massage rooms. 

    2. The next section features exclusive offers at Earth Hammam, such as the treatments, the restaurants and the Earth Hammam signature products with links to draw the user to shop as well as to facilitate navigation.

    3. The Testimonials section is displayed as a powerful marketing tool to build trust and inspire professionalism. The testimonials section features only three testimonials to foster esthetic balance and harmony. The admin can update, delete, publish or choose to keep some testimonials saved as drafts for later. This site section is minimal, responsive and centered containing the author of the testimonial and the body of the testimonial. The establishment is then in control of the image they want to portray to clients.
    
### Tickets:
This part is featured twice on the site, once with brief information on the home page and again accessible from the navbar with more detailed information about the number of sessions, the duration, price and techniques used allowing the user to delve in and find the most suitable package. This section includes a button that will redirect the user to registering or logging in and then selecting a service and eventually booking a session at a suitable time and canceling it in case of a change of plan.

### Treatments:
This page is intended to simply give more information about the free resources available to them at the clinic and during the therapy sessions. As the goal is to inform, the esthetic is clean, minimal, light and familiar to help the user's brain focus and pay attention. 
 
### Products:




### Booking:

![Booking](static/images/booking-screenshot.png)

This page is accessible from the navbar once registered or logged in. This section allows the user to select a service and then book one of the Treatments offered with a handy calendar that shows which days and times are still available and the slots that are not available are grayed out. Once the user selects an appropriate time and a service and submits it that appointment then appears in their personal list of booked treatments which in turn can be cancelled. The design of the booking system is coherent with the serene, minimal and earth tones of the site for seamless user experience.
### Accounts:

A site user has to register to book an appointment, edit their profile, see order history and purchase items sold on the site. The user can log in, log out and access their profile through the right end section of the navbar, login and drop-down menu list profile and logout. These account features have been implemented to give the necessary information to the admin for billing purposes, client and time management. However, the account can also be deleted giving the user the right to privacy thus all CRUD functionalities have been implemented for better usability.



### Error Pages:
* 400 Error page appears when the server can not or will not process the request due to something that is perceived to be a client error 
* 403 Error page appears when the user does not have the necessary permissions to access the wanted page
* 404 Error page appears when the server can not find the page requested
* 500 Error page appears when the server encounters a problem, and can not complete a request

## Admin Page Elements
### Account management
The admin Panel contains three main sections:
### Custom User:
The patients that register are saved and displayed in the panel with the status of active or not and staff or not. The super user has then all the permissions and can also grant permissions to the users for example if another user such as an assistant can be permitted to maintain the site and manage the clients' sessions and accounts.

### User Profile
The custom user information section combined with the registration form displays the First Name, Last Name, Address, and Email address of the user that can be changed using the CRUD functionality available to the user on the home page

### Coaching Sessions Calendar and Display:
Displaying the user information, the time and date of the session chosen by the user. These sessions can be canceled by the user, from the site once logged in, if they choose to.

### Testimonials:
Displaying the name, body and status of the testimonials published will publish them on the site and draft status will save them. The testimonials are solely managed by and through the admin panel.


## Features Not Yet Implemented
### Post Content:
The admin ability to post articles, meditation guides, journals and workbooks. 

# Information Architecture
## Database:

ElephantSQL is hosted by PostgreSQL has been used as a database.

## Data Models:

* Custom User: CustomUser() has been created and migrated to create a user account to access the booking system to book a session with the coach and manage the bookings.
* Testimonials: Testimonial() has been created and migrated to publish testimonials from the admin panel as a marketing tool
* Booking: CoachingSession() has been created and migrated to book a session with the coach as well as manage booked sessions such as canceling a session.

# Technologies Used
## Languages:

* Logic:
    - Python

* Template:
    - HTML
    - CSS
    - Javascript

* Database:
    - Structured Query Language

## Libraries:
    1. dj_database_url==0.5.0 psycopg2
    2. os library
    3. Cloudinary

## Tools:
Code validation was done using the following tools:

| **Tools**     | **Language**   |**Validation Result** |
| -----         | ----------     | -----------------    |
| W3C           | HTML           | Valid                |
| CSS Portal    | CSS            | Valid                |
| esprima.org   | Javascript     | Valid                |
| PEP8          | Python         | Valid                |

Responsiveness has been tested using:

  * [BrowserStack](https://www.browserstack.com/)
  * Screenshots of responsiveness have been added to this drive [file](https://www.browserstack.com/).

# Testing
Testing was conducted automatically as well as manually. Automatic testing was used for backend functions, with an easily testable input-output relationship. Manual testing was added to account for interactive scenarios, that are not easily testable with automation. 

## Automated Testing:
### Why use Automated Unit Testing?
Automated testing was used to efficiently test the core functionality, such as database object creation as well as middleware functionality with a clear input-output relationship. These test cases can then be repeated during the development process, to ensure continuous functionality, thus eliminating human error.

### The features tested with automated unit testing are:
    Database object creation:
        - User
        - Super-user
        - Session
        - Testimonial

    Middleware:
        - Calendar date and session processing functions, which are vital for the correct visualization of the calendar

The result of the automated testing is as follows:

Debug mode is on.
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
normal@user.de | service: Freedom and Thrive
..Test super user
create_superuser
..Test normal user
.
----------------------------------------------------------------------
Ran 5 tests in 0.481s

OK
Destroying test database for alias 'default'...
##  Manual Testing:
A detailed Manual Test Protocol has been created to document the steps taken for testing including responsiveness, Please, see the document for further details. The Manual Test Protocol is accessible through this [drive link](https://drive.google.com/drive/folders/1L4WP4BcJh_ixJev1f9W-9LHCpFTmigTt?usp=sharing)
### Why Use Manual Testing?
Manual testing was conducted for scenarios, that can not easily be tested via automation and thus involve a system-level interaction across several components. Regardless, the manual tests are written in a strictly repeatable manner, to ensure consistency across testers and time.

### The features tested manually are:

1. User registration: Test if the can user enter the required information such as name, email address, password, and address and subsequently register. Test error messages are displayed to the user. 
2. Account management: Test if the user can edit their profile information and view their newly edited saved profile. Test profile deletion and robustness to incorrect entries.
3. Accessibility: Test if the website's features and functions are accessible to users with disabilities, such as screen readers or keyboard-only users.
4. Booking process: Test booking page navigation and session booking, as well as session cancelation.

## Accessibility

![Site Performance Score](static/images/lighthouse-performance-test.png)
  * The overall performance of the site has been tested on desktop and mobile using Lighthouse and the site has passed the accessibility test
## Bugs:
1) Issue:       The user was able to book a session in the past.
   Resolution:  The user is now prevented from booking past sessions, by disabling the possible user interaction for the present day and all previous days.

2) Issue:       Regardless of the error, the user always received the same "Passwords do not match" error when making a mistake in the registration form.
   Resolution:  A custom routine was added to the user registration routines to extract the exact error from the available information.

3) Issue:       Although for the current week, no "Previous week" button is shown, the user was able to manipulate the URL parameters manually to change the calendar to any previous week.
   Resolution:  Negative URL parameters for the week offset are now blocked.

## Deployment

* Local Deployment

    1. Install Django and supporting libraries mentioned above, create a requirements file, a project and an app, and save, migrate and run the server using the command "python3 manage.py runserver".

* Heroku Deployment:

    1. Create an external database: Create an ElephantSQL account and instance then set up the plan and the instance as instructed and finally add the ElephantSQL database URL to Heroku.
    2. Create the Heroku app: Create the app, add the Config Vars then attach the database.
    3. Prepare the environment and settings.py file: Create a new env.py file, import the Os library, set environment variables including the secret key, add the links to the DATATBASE_URL variable on Heroku and finally add Heroku Hostname to ALLOWED_HOSTS and deploy through Heroku.

## Credit
* The code has been created following the Django and Bootstrap official documentation as well as the courses provided by the Code Institute. 
* Testing code used in test_create_user() and test_create_superuser() have been done following the guide "Create a Custom User Model in Django" by Michael Herman published in [testdriven. io](https://testdriven.io/blog/django-custom-user-model/ 
    #settings).
* The RegisterUserForm() has been adapted from courses taken on [Codemy.com](https://codemy.com/).

## Content

The content of the Website has been used and developed with the consent of a certified Life Coach whose name has been changed for privacy reasons. The content can be seen [here](https://drive.google.com/drive/folders/1_awslZHQsQfMlFC5cb1gW_YfR_6Asccn?usp=sharing).




notes from rory:
mention cloudinary doubled all the images
css file in its own css
break down the long lines
add comments for every function
database browsers download database schema