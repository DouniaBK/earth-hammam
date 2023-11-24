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

### Colour Schemes:
///////////////image of the color pallet
 Earth Hammam project is inspired by the rose-hued landscape and architecture of North Africa. The color of limestone, wet sand, olive tree leaves, and desert sand make the tones of the site, installing a sense of peace, relaxation and luxury and ensuring a calm user experience.


# Features

## Page Elements:
The site contains various pages to introduce the user to the services and approaches Earth Hammam offers. The following pages are accessible from the extendable navbar on top:

### Navigation:
The navbar is centered above the main content of the site where the user can navigate to the Hammam, tickets, treatments,  products or the booking page. The navbar collapses for small and medium screens allowing better user experience and optics.
### Logo: 
Simple clean logo featuring the name of the establishment written in uppercase and bold, placed in the top left corner of the site including the only link that redirects to the welcome page.
### Footer:
The footer includes multiple Social media links for the user to find out more about the establishment. These will open in a new tab. Furthermore, it includes a subscription section allowing the users to receive the newsletter. Underneath the Unsubscribe link, redirect the returning to an unsubscribe page, where the user is prompted to enter their email address and press unsubscribe if they no longer want to receive the newsletter.
### Toast Messages:


### Welcome page:

A simple and clean welcome page with the Earth Hammam Logo, welcomes the user into the serene world of wellness by Earth Hammam, with an elegant image of a woman being pampered with a massage and a title inviting the customer to "Treat the body and ease the soul" and button leading the user to discover Earth Hammam Marrakech. The button leads to the Hammam section of the site where the overall facility is described.

### Hammam:

    1. The first section features the Earth Hammam facility including a brief description of what Earth Hammam stands for, a carousel with images of everything the facility offers such as a hammam, pool, soak tub, aromatherapy treatments and massage rooms. 

    2. The next section features exclusive offers at Earth Hammam, such as the treatments, the restaurants and the Earth Hammam signature products with links to draw the user to shop as well as to facilitate navigation.

    3. The Testimonials section is displayed as a powerful marketing tool to build trust and inspire professionalism. The testimonials section features only three testimonials to foster esthetic balance and harmony. The admin can update, delete, publish or choose to keep some testimonials saved as drafts for later. This site section is minimal, responsive and centered containing the author of the testimonial and the body of the testimonial. The establishment is then in control of the image they want to portray to clients.


### Earth Hammam Store Categories:

Earth Hammam has three categories of items sold online, Entrance tickets, Treatments Gift Cards and Signature Products. Each category has a page accessible from the navbar and referenced in the hammam page as well. Each category page features items contained in a card with an image, a title, a description, a price and an add-to-bag button. When the user clicks on the add-to-bag button, a default quantity of one is added to the bag. The client can then adjust the quantity on the bag page. The items sold by Earth Hammam type of establishments are very limited in comparison to a large store, and thus the items sold are displayed on one page shortening the buying process for the client, instead of adding a product-detail type page where the client clicks on the product leading to a page with just information about that particular product and only then adds it to the bag. The items have enough information in the description for the client to add them to their cart with fewer clicks.

Once the shopper adds the items to their shopping bag, they can proceed with the payment by filing out proper information, approving and then they will receive a confirmation of their order.

The admin, when logged in as a superuser, will have an extra section to manage Merchandising appearing under the add-to-bag button.
///////////////////////////////add Update store Merchandise image///////////////////
This section allows the admin to delete the item or editing it. If the admin chooses to edit the item, they will be redirected to the Merchandising page, with the item they want to edit information already prefilled, once they undergo the necessary changes, a submit button will then update the information of the item in the proper category. Furthermore, the admin can also simply add another item including an image from the merchandising drop-down menu.

The design of the category pages has a balanced serene and minimalistic aesthetic with an earthy color palette that aims at not overwhelming the shopper with too much information. The design is balanced between a promise of luxury, pampering and relaxation.

The Categories of Items are:

    1. Tickets: The shopper can buy the entrance tickets at the store. featuring two types of tickets, the day ticket and the year ticket allowing visitors to buy their tickets ahead of their visit.
    
    2. Treatments: The shopper can choose to buy the treatments as a gift card, gift it or redeem it for themselves. The gift card is valid for five years giving the shopper enough time to book an appointment using the booking system accessible from the navbar. The business model is to entice the shopper to buy the treatment packages with ease through gift card format appealing to not only individuals but also the corporate industry as an incentive. Whether the gift card has been used or not, Earth Hammam benefits from it. After purchase the shopper will then receive an order confirmation email as well as an elegant e-Gift Card.
 
    3. Products: The shopper often buys spa products at the facility after having experienced the spa and thus the products sold by Earth Hammam target clients that want to take the unique Earth Hammam products to recreate that experience at home.

### Booking:

![Booking](static/images/booking-screenshot.png)

This page is accessible from the navbar once registered or logged in. This section allows the user to select a service and then book one of the Treatments offered with a handy calendar that shows which days and times are still available and the slots that are not available are grayed out. Once the user selects an appropriate time and a service and submits it that appointment then appears in their personal list of booked treatments which in turn can be cancelled. The design of the booking system is coherent with the serene, minimal and earth tones of the site for seamless user experience.

### Accounts:


///////////////////////////////////////////////////add image of login
 1. **User Account**: the user can log in, log out and access their profile through the right end section of the navbar, login and drop-down menu list profile and logout. The authentification system has been done with the django-allauth package.

- Register: New users are prompted to register in order to continue their purchase or book an appointment by filling out a registration form, confirming their account with a confirmation email and then logging in.
- Log in: The flow is standard, provide a username or email and a password, check the *Remember Me* box if the user wants to stay logged in and a *forgot Password* link to reset their password redirecting to *Password Reset* page, login button to access their account
- My Profile: Allows them to see their profile information, update it and delete their account giving the user CRUD functionality for better usability and the right to privacy. This section also has all their order history.
- Logout: Allows the user to log out by clicking logging out.

 2. **Superuser/Admin Account**: this account is meant for the admin for site management such as merchandising, retailing, client assistance and personal management. The admin managing the site of Earth Hammam has access to a frontend and backend admin page allowing them to perform the following daily tasks:

- Manage Merchandise: the admin can add, edit and delete items sold on the site.
- Newsletter: The admin can send newsletters with a handy email function thanks to a package called "Django-TinyMCE", which allows the admin to format the newsletter content as they wish. 
- Testimonials: The admin can manage testimonials from the backend, publishing, deleting and updating testimonials
- Booked Appointments: The admin can view and edit all the appointments made by the clients, assisting them in managing personal as well as helping clients if assistance is needed
- Orders: The admin is able to see all the orders made by the clients thus they can complete the shipment procedure.
- Manage subscribers: the admin can view and manage subscribers to the newsletter allowing them to manage all marketing aspects as well as further market estimations.




### Error Pages:
* 400 Error page appears when the server can not or will not process the request due to something that is perceived to be a client error 
* 403 Error page appears when the user does not have the necessary permissions to access the wanted page
* 404 Error page appears when the server can not find the page requested
* 500 Error page appears when the server encounters a problem, and can not complete a request



## Features Not Yet Implemented

- Post Content:
The admin ability to post articles, meditation guides, journals and workbooks. 

- Book Retreat Stay:
Allowing the user to book a stay or a retreat for multiple days with the booking system will be incorporated in the future.

# User Stories:


///////////////////////////////





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