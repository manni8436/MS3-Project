# MS3 Project -

![GitHub contributors](https://img.shields.io/github/contributors/manni8436/MS3-Project)
![GitHub last commit](https://img.shields.io/github/last-commit/manni8436/MS3-Project)
![GitHub language count](https://img.shields.io/github/languages/count/manni8436/MS3-Project)
![GitHub top language](https://img.shields.io/github/languages/top/manni8436/MS3-Project)

[Here is a link to the final project](https://for-the-love-of-food.herokuapp.com/)

## INITIAL DESIGN

## FINAL DESIGN

![Final project image home page]()

## :open_file_folder: CONTENTS

* [User Experience](#USER-EXPERIENCE)  
  * [User Stories](#USER-STORIES)

* [Design](#DESIGN)
  * [Color Scheme](#COLOR-SCHEME)

* [Wireframes](#WIREFRAMES)

* [Features](#FEATURES)
  * [Future Implementations](#FUTURE-IMPLEMENTATIONS)
  
* [Solved Bugs](#SOLVED-BUGS)

* [Technologies Used](#TECHNOLOGIES-USED)
  * [Languages](#LANGUAGES)
  * [Design](#DESIGN)
  * [Database](#DATABASE)

* [Deployment](#DEPLOYMENT)
  * [Initial Deployment](#INITIAL-DEPLOYMENT)
  * [How To Fork A Repository](#HOW-TO-FORK-A-REPOSITORY)
  * [How To Clone A Repository](#HOW-TO-CLONE-A-REPOSITORY)
  * [How To Make A Local Clone](#HOW-TO-MAKE-A-LOCAL-CLONE)

* [Testing](#TESTING)
  * [Code Validators](#CODE-VALIDATORS)

* [Content](#CONTENT)
  * [Images](#IMAGES)
  * [Text Content](#TEXT-CONTENT)

* [Acknowledgements](#ACKNOWLEDGEMENTS)

## :busts_in_silhouette: USER EXPERIENCE

### USER STORIES

#### CLIENT GOALS

#### FIRST TIME VISITORS

#### RETURNING USER

## DESIGN

### COLOR SCHEME

## WIREFRAMES

[Here are my wireframes for desktop, mobile and tablet for this project]()

## :star2: FEATURES

### FUTURE IMPLEMENTATIONS

## :bug: SOLVED BUGS

## :gear: TECHNOLOGIES USED

### LANGUAGES

<img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain-wordmark.svg" alt="HTML logo" width="50px" height="50px" />  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg" alt="CSS logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" alt="JavaScript logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="Python logo" width="50px" height="50px" />

### PROGRAMS USED:

#### Git:
[Git](https://git-scm.com/) was used for version control by using the Gitpod terminal to add and commit to GIt and push to Github.

#### GitPod:
[GitPod](https://gitpod.io) was used as an IDE whilst coding this site.
    
#### GitHub:
[GitHub](https://github.com/) is being used to store all the code for this project after being pushed from GitPod.

#### Am i Responsive:
[Am i Responsive](http://ami.responsivedesign.is/) was used to create the image in my [Final Design](#FINAL-DESIGN) section.

#### Firefox Developer Tools:
[Firefox Developer](https://www.mozilla.org/en-GB/firefox/developer/) Tools was used for trouble shooting and trying new visual changes without it affecting the current code.

### DESIGN:

#### Font Awesome:

[Font Awesome](https://fontawesome.com/) was used for a few icons in the footer on all of this site's pages.

#### Google Fonts:

[Google Fonts](https://fonts.google.com/) was used for all the text content on the site pages.

#### Balsamiq:

[Balsamiq](https://balsamiq.com/) was used in the initial design process to make wireframes.

### DATABASE

#### MongoDB:

[MongoDB](https://www.mongodb.com/) was used to store all contents of the database and allow full CRUD functionality.

### LIBRARIES

#### Materialize:

[Materialize](https://materializecss.com/) was used to create an amazing, responsive site.

#### jQuery:

[jQuery](https://developer.mozilla.org/en-US/docs/Glossary/jQuery) was used to initialisation of Materliazie CSS.

#### Flask:

[Flask](https://palletsprojects.com/p/flask/) was used for application framework.

#### Werkzeug:

[Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/#) was used for user information protection.

#### PyMongo:

[PyMongo](https://pymongo.readthedocs.io/en/stable/) was used to be able to work with MongoDB.

#### DNSPython:

[DNSPython](https://www.dnspython.org/) was used as a toolkit to use with Python.

#### Flask-PyMongo:

[Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/) was used to connect Python/Flask app to MongoDB.

#### Jinja:

[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) was used to populate the site using the content from the site database.

## :computer: DEPLOYMENT:

#### Heroku:

[Heroku](https://www.heroku.com/) was used to deploy the live site.

### INITIAL DEPLOYMENT

This project was developed using [GitPod](https://gitpod.io) and pushed to [GitHub](https://github.com/) then was deployed using [Heroku](https://www.heroku.com/) using the following steps below:

1. Create a `requirements.txt` file using the command `pip3 freeze --local > requirements.txt` in the GitPod terminal.
2. Create a `Procfile` with the command `echo web: python app.py > Procfile`.
3. `git add .` and `git commit -m` the new requirements and Procfile files and then `git push` them to the GitHub repository.
4. Login or Sign up to [Heroku](https://www.heroku.com/).
5. Create a new app upon Login by clicking the "New" button in your dashboard. Choose a unique name and set the region to the one closest to you.
6. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
7. Search for your GitHub repository and connect.
8. In the heroku dashboard for the application, click on "settings" > "Reveal Config Vars".
9. Set the folowing config vars:

| Key | Value |
| ----------|--------- |
| PORT | 5000 |
| IP | 0.0.0.0 |
| DEBUG | False |
| MONGO_URI | USER_MONGODB_URI |
| MONGO_DBNAME | USER_MONGODB_NAME |
| Secret_Key | USER_SECRET_KEY |

### HOW TO FORK A REPOSITORY

If you need to make a copy of a repository:

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [manni8436/MS3-Project](manni8436/MS3-Project).
3. In the top right corner, click "Fork".

### HOW TO CLONE A REPOSITORY

If you need to make a clone:

1. Login in to [GitHub](www.github.com).
2. Fork the repository manni8436/MS3-Project using the steps above in [How To Fork a Repository](#HOW-TO-FORK-A-REPOSITORY).
3. Above the file list, click "Code".
4. Choose if you want to close using HTTPS, SSH or GitHub CLI, then click the copy button to the right.
5. Open Git Bash.
6. Change the directory to where you want your clone to go.
7. Type git clone and then paste the URL you copied in step 4.
8. Press Enter to create your clone.

### HOW TO MAKE A LOCAL CLONE

If you need to make a local clone:

1. Login in to [GitHub](www.github.com).
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should close the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new locaiton, where you want the cloned directory to be.
7. Type git clone and then paste the URL you copied in step 4.
8. Press Enter, and your local clone will be created.

## :test_tube: TESTING

### CODE VALIDATORS

The W3C Markup Validator and W3C CSS Validator was used to validate my project to make sure there were no errors within the site.

* W3C HTML Validator Results
  * [HMTL]()
    
* W3C CSS Validator Results
  * [CSS]()

* JSHint 
  * ![JavaScript]()

* PEP8 Online
  * ![PEP8]()

* Lighthouse:
  * [Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to ensure that the site was perfoming well, confirming to best practises, SEO and Accessibility guidelines.

### FULL TESTING

[Click Here](testing.md) to view the full testing steps that were completed on every device and browser.

### LIGHTHOUSE

### DESKTOP

#### Performance:

#### Accessibility:

#### Best Practices:

#### SEO:

## CONTENT

### IMAGES

* Images mainly provided by Wikipedia and Pinterest, but a full list have been provided below:

### TEXT CONTENT

* Text content on all Pages was copied and/or amended from the following sites:  
    
## ACKNOWLEDGEMENTS:

<!-- I would like to give a big thanks to [Chris Quinn](https://github.com/10xOXR) for all his help, effort, guidance
and patience he has provided during this project.

I would also like to thank [Abi Harrison](https://github.com/Abibubble) for all her support, advice and explaining things to me when I did not understand. -->