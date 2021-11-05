![For The Love Of Food](static/docs/readme_images/ms3-responsive-image.png)


## **Contents**

* [**Testing**](#testing)
  * [**Navigation**](#navigation)
  * [**Buttons**](#buttons)
  * [**Home Page**](#home-page)
  * [**Register Page**](#register-page)
  * [**Login Page**](#login-page)
  * [**Favourites Page**](#favourites-page)
  * [**Recipes Page**](#recipes-page)
  * [**Profile Page**](#profile-page)
  * [**Full Recipes Page**](#full-recipes-page)
  
# **Testing**

### **Navigation** 
    - all pages - Logged In Users

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Home button    | To redirect to home page| Click the home button | Button navigates to home | Pass |
| Nav links | Clicking Recipes takes user to Recipes page | Click Recipes | Redirected to Recipes page | Pass |
| | Clicking Profile takes user to their profile page | Click Profile | Redirected to Profile Page | Pass |
| | Clicking Add Recipes takes user to Add Recipes page | Click Add Recipes | Redirected to Add Recipes page | Pass |
| | Clicking Edit Recipes takes user to Edit Recipes page | Click Edit Recipes | Redirected to Edit Recipes page | Pass |
| | Click Favourites takes user to Favourites | Click Favourites | Redirected to Favourites page | Pass |
| | Click Logout logs out the user | Click Logout | User logged out and redirected to login Page| Pass |

### **Navigation**
    - all pages - User not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Home button    | To redirect to home page| Click the home button | Button navigates to home | Pass |
| Nav links | Clicking Recipes takes user to Recipes page | Click Recipes | Redirected to Recipes page | Pass |
|  | Click Login redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
|  | Click Not Yet registered link redirects to Register page | Click Not Yet registered link | User redirected to Register Page | Pass |
|  | Click Register redirects to login page | Click Register | User redirected to Register Page | Pass |
|  | Click Already Registered link redirects to login page | Click Already Registered link | User redirected to login Page | Pass |

[Back to contents](#contents)

### **Buttons**
  - all pages - on desktop site

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Feedback on hover | buttons change colour when user hovers the mouse over them and Login Button on Home screen  | Hover mouse over each button | Buttons change colour when hovered over | Pass |

### **Home Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- |:----:|
| Card 'Login' button | Clicking "Login" button takes users to Login page | Click "Login" button | User redirected to Login page | Pass |
| Card 'See All Recipes' button | Clicking "See All Recipes" button takes users to Recipes page | Click "See All Recipes" button | User redirected to Recipes page | Pass |
| Quotes Carousel - on desktop | Play automatically | View carousel to make sure it moves automatically | carousel moves automatically | Pass |
|  | Stop when hovered over  | hover mouse over to see if it stops  | carousel stops on mouse hover | Pass |

[Back to contents](#contents)

### **Register Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| | Username and Password must be between 5 and 15 characters | Attempt to enter username and password with less than 5 characters | Form restricts the user from using less than 5 characters  | Pass |
| | Username and Password must be between 5 and 15 characters | Attempt to enter username and password with more than 20 characters | Form restricts the user from using more than 20 characters | Pass |
| | Register with new user and password to be logged in and redirected to Recipes page | username, password and click register | New account registered and Recipes page shown | Pass |

[Back to contents](#contents)

### **Login Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-----------------| ----------|  ---------- | :----: |
| Login functionality | Correct user/pass combination directs user to their profile page with name displayed | Login with correct username/password combination | Redirected to user profile with name displayed | Pass |
|   | Incorrect username/password combination | Error showing "incorrect username/password" | Flash message displays | Pass |
| Link to Register | Redirect to Register page | Click link to register | Redirected to Register page | Pass |

### **Favourites Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Favourites | Favourites can be viewed and removed | Click on Favourites nav link, click icon to remove from favourites | Upon clicking remove from favourites the recipe is removed from favourites | Pass |
|  | If no recipes saved as a favourite there is a prompt to add one with link to all recipes | Click on Favourites nav link, click icon to remove from favourites, see message prompt to click to look at recipes | No favourites added so message is displayed and clicking the link leads to the reviews page | Pass |

[Back to contents](#contents)

### **Recipes Page**
    - user not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Search Function | Search by Recipe name | Type any recipe name into search field and click search | Search returns recipes of choice| Pass |
| | Reset button should reset the search form | Enter text to search form then click Reset | Form resets to show all reviews | Pass |

[Back to contents](#contents)

### **Profile Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Edit | Recipes created can be edited | Click on Profile nav link, click button to edit recipes | Upon clicking the button to edit recipes the page is redirected to edit recipes page | Pass |
| Delete | Recipes created can be deleted | Click on Profile nav link, click button to Delete recipes | Upon clicking the button to Delete recipes the page will render a delete confirmation modal to delete recipes| Pass |
| If no profile page shows no recipes | If no recipes added to profile there is a prompt to add one with link to add recipes | Click on Profiles nav link, click icon to add some recipes, see message prompt to click to add recipes | No recipes added message is displayed and clicking the link leads to the add recipes page | Pass |

[Back to contents](#contents)

### **Full Recipes Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Show full recipe of recipe clicked | Full recipe to be displayed | Click on full recipe button on recipes in recipes page, | Upon clicking the button to show full recipe the page is redirected to Show full recipe page | Pass |

[Back to contents](#contents)