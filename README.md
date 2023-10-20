
# BuzzEireBrazil

![Alt text](documentation/home_lg_screen.PNG)

```
Welcome to BuzzEireBrazil!
```

This blog was created to Brazilians living in Ireland, offering a platform for them to promote their businesses or professional services. Additionally, users can seek recommendations and assistance from others within the Brazilian community in Ireland. The primary objective of this project is to connect Brazilians living in Ireland with job opportunities and business prospects.

## Goals
* Facilitate connections and networking among Brazilians in Ireland, specifically focusing on job and business opportunities.
* Create a user-friendly and inclusive platform where users can easily share and discover professional services.
* Foster a supportive community environment for Brazilians living in Ireland.

# User Experience

* User experience is a central focus of this project. We aim to provide an intuitive and visually appealing interface that enhances user engagement.
* The website has been designed with the user in mind to ensure seamless navigation and accessibility.

## Agile
Agile methodologies have been employed to manage and prioritize project tasks using GitHub Project Boards. Here's how we approached it:

1. **Theme Identification:** Initially, we created a spreadsheet to collect details categorized by themes, which helped us define epics. These themes include Account Management, Profile, Post Pool, Navigation, and Admin.

2. **Issue Template:** To expedite the addition of User Stories to the project, we developed an issue template.

3. **Repository Settings:** In the repository settings, we set up templates for features. The Issue Template provides developers with the necessary information to address MVP (Minimum Viable Product) points.

4. **Deployment process:** The project was developed using python and Django and was deployed using Debug = `False` 

## User Stories in Agile
We've organized the project into the following milestones:

![Agile Methodology](documentation/agile_issues.PNG)

 1. Start and deploying

2. Setup & Basic Blog Functionality: This phase involves establishing the fundamental blog features, such as user registration and post creation.

    - USER STORY: Navigate Through Pages

    - USER STORY: Browse Blog Entries

    - USER STORY: Access a Post
  
3. User Engagement & Interactivity: Here, we focus on enhancing user engagement through features like comments, likes, and sharing.
    - USER STORY: Profile Creation

    - USER STORY: Participate in Post Discussion

    - USER STORY: Engage with Content

4. Admin Management & Content Creation: In this phase, we develop admin management tools and refine content creation features.
    - USER STORY: Content Administration

    - USER STORY: Draft Posts `(NOT IMPLEMENTED)`

    - USER STORY: Moderate Comment Section
    
    - USER STORY: Search for Posts `(NOT IMPLEMENTED)`

    - USER STORY: Allows to preview before posting `(NOT IMPLEMENTED)`


5. Advanced User Features & Enhancements: This milestone concentrates on advanced user features and improvements to existing functionalities.

     - USER STORY: Search for Posts `(NOT IMPLEMENTED)`

     - USER STORY: Notification Preferences `(NOT IMPLEMENTED)`

     - USER STORY: Review Comment Section 

6. Testing & Quality Assurance: The final milestone emphasizes rigorous testing and quality assurance to ensure a stable and reliable platform.

    - Manual Testing Framework

    - Automated Unit Testing

    - UI/UX Testing

    - Performance Testing



# Design
## Color Scheme
The color scheme was chosen to reflect the Irish flag and evoke a sense of Ireland:

![Alt text](documentation/colors.PNG)


## Mobile-Friendly Design

For mobile users, the website is optimized with a responsive design. The navigation menu is toggled to accommodate smaller screens, making it convenient for users on mobile devices.

Authentication: Users who are not logged in can still browse and view posts. However, to participate by commenting or making suggestions, they must first log in. If a user doesn't have an account, they can easily sign up to become a part of the community.

![Login request](documentation/login-request.PNG)

## Typography
We've selected the `"Secular One"` font for the website. 

## Icons
Font Awesome icons have been used throughout the site, including for the buttons and social media links.

# Features
## Pages and elements

1 - **Home Page**
The heart of the website, the home page, serves as a central hub where users can access a variety of key features. Here's what you'll find on the home page. The logo is also clickable.

2 - **List of Posts:** Users can view a comprehensive list of posts submitted by members of the Brazilian community in Ireland. These posts showcase various businesses, services, or job opportunities.


![home page for large screens](documentation/lg-screen.PNG) ![home page for large screens2](documentation/lg_screen_2.PNG)


3 - **Main Sponsors:** 
Prominent on every page, the "Main Sponsors" section highlights four businesses that have chosen to promote their services on the platform. This section offers visibility and recognition to these sponsors.

 * 3.1 ![main sponsors](documentation/main_sponsors-view.PNG)

 Clicking in the contact us button you will be redirect for a form to be filled in order to check how to become a sponsor.

 * 3.2 ![sponsors form](documentation/Contact_us.PNG)

 After submitting the form you will get a message thanking you for your interest in become a sponsor
 
 * 3.3 ![submitted form](documentation/Contact_us_submitted.PNG)

4 - **List of Suggestions:** 
Users can discover and submit requests for assistance or recommendations. This section encourages community members to help one another by connecting individuals seeking specific services with those who can provide them.

![suggestions view](documentation/suggestion-view-if-logged.PNG)

5 - **Post Details Page**
When a user clicks on a post from the list, they are directed to the "Post Details" page. Here, they can delve deeper into the specifics of a particular business or service. This page includes:

![Post details](documentation/post_details-view.PNG)

6 - **Comments and Feedback:** Users can engage in discussions and provide feedback regarding the business or service. This interactive feature fosters communication and helps community members make informed decisions.

![comments and feedback](documentation/comments_and_feedback.PNG)

7 - **Navigation**
The navigation bar, situated at the top of the website, provides easy access to essential features and functions. Users can find the following items in the navigation:

![Nav bar for small devices](documentation/nav_bar-sm.PNG) ![Nav bar for large devices](documentation/nav_bar-lg.PNG)


8 - **Login/Logout:** Users can log in to their accounts or log out as needed. This functionality is crucial for accessing certain actions on the website.


9 - **Sign-In/Sign-on Page:**
The Sign-In page serves as the entry point for registered users to access their accounts. Key features of this page include:
 
 * 9.1 ![Sign up large devices](documentation/sign_up-view-lg-screen.PNG)
 General view for large device

 * 9.2 ![Sign up view](documentation/sign_in-view.PNG) 
![Sign up view](documentation/sign_up-view.PNG)

Full Page view 

* 9.3 ![sign_up-view-sm](documentation/sign_up-view-sm.png) 
![sign_in-view-sm](documentation/sign_in-view-sm.png)

* 10 **Clickable Logo:** Clicking on the logo serves as an alternative way to return to the home page, ensuring intuitive navigation.

![Alt text](documentation/logo-image.PNG)

* 11 **Footer**: footer is quite clean. It brings few elements. The information about the me and LinkedIn and GitHub link pages

![Alt text](documentation/footer.PNG)

## Future implementation 

 1. List of Posts Sorted by Categories:
In upcoming versions, we will introduce a feature to categorize posts. This will make it easier for users to find content that interests them. Posts will be tagged with relevant categories, and users can filter posts by selecting a category from the navigation menu.

2. Search Bar on the Top of Post List:
To enhance user experience, we'll add a search bar at the top of the post list. Users can simply enter keywords or phrases related to their interests, and the system will display matching posts in real-time.

 3. Reply for Suggestions in Suggestion Section:
We are committed to fostering engagement within the community. In the next release, users will be able to reply to suggestions, providing feedback or offering assistance. This will create a more interactive and supportive environment.

 4. Reply for Comments in Post Details:
To encourage discussions, we will implement a comment reply feature. Users can respond to specific comments within a post's comment section, facilitating meaningful conversations.

 5. Rate with Star for Services in Post Details:
We aim to improve the way users evaluate services. Users will have the option to rate services with a star-based system, offering valuable feedback to service providers and helping other users make informed decisions.

 6. Feed with Updates in Another Page Like a Journal:
In future updates, we will introduce a dedicated page for updates and announcements. Users can access this journal-like feed to stay informed about the latest community news, events, and changes to the platform.

 7. Notification Preferences for User:
Personalization is key. Users will be able to customize their notification preferences. They can choose to receive updates related to specific categories, new posts, comments on their content, and more.

 8. Reset Password:
Password management is crucial. Users will have the option to reset their passwords securely through a password reset feature. This ensures account security and accessibility.

 9. Draft Post for Keeping Posts Saved:
We understand that not every post is meant for immediate publishing. Users can save drafts of their posts and return to them later for editing and publishing. This feature will ensure that no creative idea is lost.

## Accessibility


Our commitment to accessibility is evident in every line of code. We've gone the extra mile to make our website as user-friendly as possible for everyone. Here's how we've achieved this:

- Semantic HTML: We've meticulously crafted our web pages using semantic HTML tags. This means that not only is our code clean and organized, but it also ensures that screen readers and assistive technologies can understand and navigate the content effortlessly.

- Descriptive Alt Attributes: Images on our site are more than just visuals; they're informative. We've provided detailed and meaningful alt attributes for every image. This empowers screen readers to convey the content accurately to users who rely on them.

- Icons with Text Descriptions: Icons can be confusing for some users. To make sure everyone understands their meaning, we've included text descriptions alongside icons where needed. This ensures that all users, regardless of their abilities, can interact with our site effectively.

- Color Contrast: We understand the importance of legibility. To that end, we've maintained a high level of color contrast throughout our site. This not only makes text and content easier to read but also ensures that our site is inclusive and accessible to all.

At BuzzEireBrazil, accessibility isn't an afterthought; it's an integral part of our development process. We believe that everyone should have a seamless and enjoyable experience on our platform, regardless of their abilities or assistive technologies.


Creating a Blog Application with Django
🚀

Welcome to BuzzEireBrazil! In this section, we will guide you through the process of creating a robust blog application using Django. Learn how to build, customize, and launch your own blogging platform.

Installation Steps
🔧

Let's begin by setting up your development environment. Follow these simple steps to install Django and get ready to embark on your blogging journey.

Main Documentation
📘

In the main documentation, you'll find comprehensive guidance on building a blog application with Django, including detailed steps for:

Installing Django: Get started by setting up the Django framework.
Writing Your First Django App, Part 1: Dive into the fundamentals of building your first Django application.
Technologies Used
🛠️ This project has been developed using a variety of technologies, ensuring a robust and dynamic platform for our users. Here's a breakdown:

# technologies Used
## Languages
- HTML: The foundation of our website, responsible for structuring the main site content. We have 13 HTML files in the project so far.
- CSS: Provides the styling and layout to create an attractive and user-friendly interface.
- JavaScript: Adds interactive elements and enhances user engagement.
- Python 3.8.11: The backbone of our back-end functionality, powering the server and business logic.

## Databases Used
- ElephantSQL (Postgres database): Our reliable data storage solution. 
- Cloudinary: An online static file storage service for managing media assets.

## Frameworks Used
- Django: A high-level Python web framework that streamlines development.
- Bootstrap (Version 5.2.3): A CSS framework that accelerates front-end design.
- Crispy Forms: Enhances form rendering for a more user-friendly experience.

## Development Tools
- Pip: A vital tool for installing Python packages.
- Jinja: Our templating engine, facilitating dynamic content rendering.
- Balsamiq: Used for wireframing to plan out the site's layout and structure.

## Version Control
- Git: The backbone of our version control system.
- GitHub: Our repository for saving and managing project files.

## Development Environment
- Gitpod: A cloud-based integrated development environment (IDE) for seamless development.

## Hosting and Deployment
Heroku: Hosting platform for the deployed back-end site.

## Typography and Styling
- Google Fonts: Imported fonts to enhance site aesthetics.

## Testing and Debugging
- Google Chrome Dev Tools: Essential for troubleshooting, testing, and ensuring responsiveness and styling.
- Am I Responsive?: Used to display website images on various devices.

# Deployment & Local Development
## Fork the Repository

1. Log in or Sign up: Go to GitHub and log in with your account. If you don't have an account, sign up.
2. Navigate to the Repository: Go to the repository for your project (replace your-repo-name with the actual repository name). <br>
Click here [BuzzEireBrazil](https://github.com/zanettiprado/buzzeirebrazil)
```
https://github.com/zanettiprado/buzzeirebrazil
```

3 - Fork the Repository: Click the "Fork" button in the top right corner of the repository page. This will create a copy of the repository under your GitHub account.

## Clone the Repository
1. Log in to GitHub: If you're not already logged in, log in to GitHub.

2. Navigate to the Repository: Go to the repository for your project (replace your-repo-name with the actual repository name).<br>
Click here [BuzzEireBrazil](https://github.com/zanettiprado/buzzeirebrazil)
```
https://github.com/zanettiprado/buzzeirebrazil
```
3. Clone the Repository: Click on the "Code" button on the repository page. Select your preferred method for cloning: HTTPS, SSH, or GitHub CLI. Copy the provided link.

4. Open Terminal: Open your terminal (command prompt or Git Bash on Windows, Terminal on macOS, or any terminal emulator on Linux).

5. Change Directory: Use the cd command to navigate to the location where you want to store the cloned repository.

```
cd /path/to/your/directory
```
6. Clone the Repository: In your terminal, run the following command, pasting the link you copied from step 3:

## Install Project Dependencies
1. Navigate to Project Directory: Ensure you are in the project directory where the `requirements.txt` file is located.

2. Install Dependencies: In your terminal, run the following command to install the required packages:

```
pip install -r requirements.txt
```

## ElephantSQL Database
In this project, we use ElephantSQL to store our data in a special database called PostgreSQL. To get your own database, follow these steps:

1. Sign up using your GitHub account.
2. Click on "Create New Instance" to make a new database.
3. Give it a name (usually the project's name, like "tribe").
4. Choose the "Tiny Turtle (Free)" plan.
5. You can ignore the "Tags" part.
6. Pick a Region and Data Center that's closest to where you are.
7. Once it's created, click on the new database's name to see the database URL and Password. You'll need these later.

## Cloudinary API
We use the Cloudinary API in our project to keep our pictures and videos online because Heroku, where we host our project, doesn't save this kind of data. Here's how to get your own Cloudinary API key:

1. Create an account and log in to Cloudinary.
2. When they ask what you're interested in, pick "Programmable Media" because it's about images and videos.
3. If you want, change your cloud name to something you can remember easily.
4. On your Cloudinary Dashboard, you'll find your API Environment Variable. It looks like a long code.
5. Make sure to remove the "CLOUDINARY_URL=" part from the code because that part is your key.

## Heroku Account and dployment
<details>
<summary>How to use HEROKU to deploy the project step by step</summary>

<br>

1. Set Up Your Heroku Account

If you don't have a Heroku account, sign up for one at https://www.heroku.com/. It's free to get started.

2. Install Heroku CLI

Download and install the Heroku Command Line Interface (CLI) for your operating system. You can find installation instructions here: https://devcenter.heroku.com/articles/heroku-cli

3. Log In to Heroku

Open your terminal or command prompt and log in to Heroku by running:
```
heroku login
```
Follow the prompts to enter your Heroku credentials.

4. Initialize a Git Repository

If your project isn't already in a Git repository, you'll need to initialize one. Navigate to your project's root directory in the terminal and run:

```
git init
git add .
git commit -m "Initial commit"
```
5. Create a requirements.txt File

If you don't already have a requirements.txt file, create one. This file lists all the Python packages required for your project. You can generate it by running:
```
pip freeze > requirements.txt
```
6. Create a Procfile

Create a file named Procfile (without any file extension) in your project's root directory. This file tells Heroku how to run your application. Inside the Procfile, add:

```
web: python your_app_name/manage.py runserver 0.0.0.0:$PORT
```
7. Install Gunicorn

Gunicorn is a WSGI HTTP server for Python applications. Install it by running:
```
pip install gunicorn
```

8. Add Heroku Buildpacks
Heroku uses buildpacks to determine how to build and run your application. You'll need to add Python and Node.js buildpacks if your project uses JavaScript or CSS. Run the following commands to add buildpacks:
```
heroku buildpacks:add heroku/python
```
9. Set Environment Variables

Set the environment variables in Heroku that you mentioned earlier. You can do this by running:
```
heroku config:set CLOUDINARY_URL=your_cloudinary_api_key
heroku config:set DATABASE_URL=your_database_url
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set SECRET_KEY=your_secret_key 
```

Replace your_cloudinary_api_key, your_database_url, and your_secret_key with your actual keys and URLs.

10. Deploy to Heroku

Now it's time to deploy your project to Heroku. Run:
``` 
git push heroku master
```

This command will push your code to Heroku's servers and trigger the deployment process.

11. Run Migrations

After deploying, run the following command to apply database migrations:
``` 
heroku run python manage.py migrate 
```

12. Open Your App

Your app should be deployed and live on Heroku now! You can open it in your browser using
``` 
heroku open
```

</details>


