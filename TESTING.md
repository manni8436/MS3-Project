![For The Love Of Food](static/docs/readme_images/ms3-responsive-image.png)


## **Contents**

* [**Testing**](#testing)
  * [**Navigation**](#navigation)
  * [**Buttons**](#buttons)
  * [**Welcome Page**](#welcome-page)
  * [**Register Page**](#register-page)
  * [**Log In Page**](#log-in-page)
  * [**Profile Page**](#profile-page)
  * [**All Reviews Page**](#all-reviews-page)
  * [**Book Review Page**](#book-review-page)
  * [**Add Review Page**](#add-review-page)
  * [**Edit/Delete Review Page**](#edit-delete-review-page)
  * [**User Stories Testing**](#user-stories-testing)
  
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
| | Click Log Out logs out the user | Click Log Out | User logged out and redirected to login Page| Pass |


### **Navigation**
    - all pages - User not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Home button    | To redirect to home page| Click the home button | Button navigates to home | Pass |
| Nav links | Clicking Recipes takes user to Recipes page | Click Recipes | Redirected to Recipes page | Pass |
|  | Click Log In redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
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

### **Register Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| | Username and Password must be between 5 and 15 characters | Attempt to enter username and password with less than 5 characters | Pass |
| | Username and Password must be between 5 and 15 characters | Attempt to enter username and password with more than 20 characters | Form restricts the user from using more than 20 characters | Pass |
| | Register with new user and password to be logged in and redirected to Profile page | username, password and click register | New account registered and Recipes page shown | Pass |

[Back to contents](#contents)

### **Log In Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-----------------| ----------|  ---------- | :----: |
| Log in functionality | Correct user/pass combination directs user to their profile page with name displayed | Log in with correct username/password combination | Redirected to user profile with name displayed | Pass |
|   | Incorrect username/password combination | Error showing "incorrect username/password" | Flash message displays | Pass |
| Link to Register | Redirect to Register page | Click link to register | Redirected to Register page | Pass |

### **Profile Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Favourites | Favourites can be viewed and removed | Scroll down to Favourites section, click icon to remove from favourites | Upon clicking favourites the book review is removed from favourites for that [user](static/images/testing/favourite.png) | Pass |
|  | If no reviews saved as a favourite there is a prompt to add one with link to all reviews | Scroll to Favourites section, see message prompt to click to look at reviews | No favourites added so message is displayed and clicking the link leads to the reviews page | Pass |

[Back to contents](#contents)

### **Favourites Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Favourites | Favourites can be viewed and removed | Scroll down to Favourites section, click icon to remove from favourites | Upon clicking remove favourites is removed from favourites | Pass |

[Back to contents](#contents)

### **All Recipes Page**
    - user not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Search Function | Search by Recipe name | Type any recipe name into search field and click search | Search returns recipes of choice| Pass |
| | Reset button should reset the search form | Enter text to search form then click Reset | Form resets to show all reviews | Pass |

[Back to contents](#contents)

### **Edit/Delete Recipe Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----: |
| Edit functionality | Only admin or reviewer can edit reviews | Log in as admin, navigate to a book review page, click edit, edit review, click submit, view book review to check edit successful | Edit successful for admin user | Pass |
| | Only admin or reviewer can edit reviews | Log in as standard user, create review, edit review, click submit, view book review to check edit successful | Edit successful for reviewer | Pass | 
| | | Log in as different standard user, attempt to edit Recipe | Edit/Delete button not available | Pass |
| Review info prepopulated on edit | Recipeshould be prepopulated on editing a Recipe | Pass | 
| Delete functionality | Only Recipe creater can delete Recipe | Log in as admin, navigate to a Recipe review page, click delete, modal launch to confirm, click confirm | Delete successful for admin | Pass |
| | | Log in as standard user, create Recipe, click delete | Delete successful | Pass | 
| | | Log in as different standard user, attempt to edit Recipe | Edit button not available | Pass |
| | | Log in as different standard user, attempt to delete Recipe | Delete button not available | Pass |
