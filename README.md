# The Recipe Blog
The Recipe Blog is a website that I built using the Dajngo Full Stack framework for my Portfolio Porject 4. The Recipe
Blog is a site that allows users to view and share their favourite recipies and also view and share their favourite wines.
They are able to comment underneath recipes and also like them. Users need to be logged in to get the full
functionality of the site.
  
![Am i responsive image](readme-docs/images/amiresponsive.jpg)  

[Click Here To Visit Live Site](https://the-recipe-blog1.herokuapp.com/)  

## Table Of Contents:
1. [UX Design](#ux-design)
2. [Features](#features)
3. [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Acknowledgements](#acknowledgements)


## UX Design:


## Features:

### Navigation Bar
- The Navigation bar sits at the very top of each page, The logo is at the right hand side and the navigation links are on the left.
- When logged in some of the links change, like the **Login** becomes **Logout** and the **Registeration** link is removed and **Wine** linke added.
- The Navbar background is green with the Navigation links and Logo in white colored text.
- On large to xx-large screens the navigation bar is in the center of the page and is sized by the bootstrap [container-lg](https://getbootstrap.com/docs/5.0/layout/containers/) class.
- The active page(page that the user is current on) is displayed in bold text, this makes it stand out much more and is clear to the user which page they are on.
- When on medium to small screens the navigation menu changes to burger menu which show all the nav links when clicked on.(second screenshot below)
  
![Nav bar](readme-docs/images/navbar.jpg)  

**Nav bar on mobile and tablets**  

![Nav bar](readme-docs/images/navbar-smaller-devices.jpg) 


### Footer
- The footer is found at the bottom of every page and responsive for tablet and mobile too.
- It displays 4 icons for the biggest scoial media platfoms today, Twitter, Facebook, Youtube and Instagram. These are all green in color to match the sites colour scheme
- Above the icons there is a horizontal line that is centered, and it is 30% of the screen with on large devices, 50% on medium and 60% on small devices.
- When any of the icons are clicked the social media site opens on a seperate tab, this way the user still has the Fitness 365 website open so they can easily navigate back to it.
  
![Footer](readme-docs/images/footer.jpg) 
- - -  

### Home Page
- The home page has a background image of food on a table and has a light black linear gradiant to darken the image a bit and bring up the text color.
- In the center there is a H1 heading that says **The Recipe Blog** in green.
- Below the heading there is a text box that explains what the site is about, the text box has a white border around it and the backgound is abit darker, the text is then in white shich really makes it stand out.

![HomePage](readme-docs/images/home.jpg) 
- - -  

### Recipes Page
- At the top of the recipes page, right below the Nav bar there is a H1 heading that says **Recipes List** which is underlined and centered.
- Below this are the recipes cards which are displayed in the bootstrap card format and have six to a page.
- The **read more** button is greyed out when the user is logged out and is green when the user is logged in(second screeshot)
- Above the recipes on the left hand side there is a green **Add Recipe** button, this button is only displayed if the user is logged in.
- On Large screens they are three accross, on medium devices they are two accross and on small deavices it is just one.
- Below the recipe cards there will be a next and back button depending on how many recipes have been added.  

![Recipes](readme-docs/images/recipes.jpg)


**Recipes page when user is logged in** 
![Recipes](readme-docs/images/recipes-logged-in.jpg)
  
[Back to the top](#the-recipe-blog)
- - -    
  
### Recipe Details
- At the top of the of the recipe details page in the center is the photo of the recipe.
- If the user who posted the recipe is looking at it, then the delete and edit buttons are at the top right.
- Below the image and center is the title of the recipe and the author who has posted it.
- Below the image to the left you have a like button that shows how many people liked the recipe, the heart will be an empty outline with a 0 next to it if no one has liked it, and it will be filled red if liked.
- Underneath the like button you have **Description**, **Ingredients** and **Cooking Instructions** fields.
- Then there is the comment section below this, which has a H2 heading that says **Comment Section**, The comment section has a border around it, and comments have a light grey backgound colour, which makes them stand out. The authors name and date is displayed below the comment and there is an edit and delete button in the top right of the comment which is only visible to the author of the comment.
- Below this is the **Post a Comment** section which has has border around it. Inside is the **info** text area where the user can enter their comment and then below that is the green **Post** button.

![Recipe details](readme-docs/images/recipe-details.png)
- - -   

### Add Recipe Page
- When a user clicks the **Add Recipe** button on the **recipes** page they are taken to the **Add Recipe page** where they are greeted with a form to enter their recipe.
- At the top there is a H1 heading that says **Add Your Recipe below** with the form fields beneath it. I kept the form big and simple, so that it is easy for the user to use and everything is centered.
- For the **Description**, **Ingredients** and **Cooking Instructions** fields the summernote widget is used so that a user can easily format their text and style it whatever way they wish.
- Below this is a **Submit** button that is in green and once clicked the recipe will be submitted and the user returned to the recipe page where they will see their recipe as the first in the list.
- Beside the **Submit** button there is a orange **Cancel** button that once clicked will bring the user back to the recipe page.
  
![Add-recipe](readme-docs/images/add-recipe.png)
- - -

### Edit Recipe Page
- The **Edit Recipe page** is accessed when the user clicks the edit recipe pencil icon on the recipe details page.
- This is practically the same as the **Add Recipe page**. The only difference is that the form is already filled in with the details you entered before so that you can change them, and also the heading says **Edit Your Recipe**
- After editing the Recipe a success message will be displayed at the top of the screen.
- Please note that only the user who created the recipe can edit it from here.

![Edit Recipe](readme-docs/images/edit-recipe.png)

[Back to the top](#the-recipe-blog)
- - -

### Delete Recipe
- When a user clicks on the delete icon on the recipe details page a bootstrap modal pops up in the center and ask the user to confirm.
- The modal is a square box with a grey background, with a heading that says **Delete Recipe** and text centered asks **Are you sure you want to delete the recipe**.
- At the bottom right of the modal box is a red **Yes** button to confim if they want to delete it. The button is red because red is associated with danger and if clicked the recipe will be gone. Once clicked the recipe will be deleted and the user will be returned to the recipes page.
- Beside the **Yes** button there is a **Cancel** button, that when clicked will make the modal disappear, there is also an **x** in the top right of the modal that will also get right of it.
- If the user clicks anywhere else on the screen the modal will also disapear.
- Please note that only the user who created the recipe can delete it from here.
- After deleting the Recipe a success message will be displayed at the top of the screen.

![Delete Recipe](readme-docs/images/delete-recipe.jpg)
- - -

### Edit comment Page
- When the edit comment icon is clicked at the right of the comment, the user is brought to the edit comment page.
- This is just a bigger version of the **Post a Comment** section on the recipe details page, but it has the comment message you posted in the **info** box for you to edit.
- Above this there is a heading that tells you to **Edit the comment you posted on the certain date and time**
- There is an green **update** button below the text box that when clciked will update the comment and bring you back to the recipe details page where you can view your updated comment.
- Beside this is an amber **Cancel** button that returns the user to recipe details page, if they decide not to update the comment.
- Please note that only the user who created the comment can edit it from here.
- After editing the Comment a success message will be displayed at the top of the screen.

![edit comment](readme-docs/images/edit-comment.jpg)
- - -

### Wines


- - -

### Wine Details page
- When a user clicks the green **View** button on one of the Wine cards from the **Wines** page they are brought to the wine details page.
- Here the user will see a larger bootstrap card that is centered, this displays the image larger and all of the wine details. There is a border around the card which is standard with bootstrap cards.
- At the bottom of the wine card there is a **Edit** and **Delete** Button.

![Wine details](readme-docs/images/wine-details.jpg)
- - -

### Add Wine Page
- When a user clicks the **Add Wine** button on the **Wines** page they are taken to the **Add Wine page** where they are greeted with a form to enter the details of the wine.
- At the top is a H1 heading that says for the user to **Add a Wine Below**
- below the heading is a simple form that is centered on the page and ask the user to fillin int he following fields enter the **Name** of the wine, upload an **Image**, choose a type of **wine** from the drop down, add the **Alcohol percentage** and finally add the **Country of Orgin** for the wine.
- Below this is a green **Submit** button that when clicked adds the wine and brings the user back to the Wines page, where they can see the wine they added as the first in the list.
- Beside the **Submit** button is an amber **Cancel** button, that will bring the user back to the **Wines** page if they decide that they do not want to post a wine.

![add wine](readme-docs/images/add-wine.jpg)
- - -

### Edit Wine Page
- The **Edit Wine page** is accessed when the user clicks the **Edit** button on the **Wine details** page.
- This exactly the same as the **Add Wine** page only for it has the details that the user already enter filled into the form fields so that the user can edit them and the heading also says **Edit Wine**
- Please note that only the user who created the wine can edit it from here.
- After editing the Wine a success message will be displayed at the top of the screen.

![edit wine](readme-docs/images/edit-wine.jpg)
- - -

### Delete Wine
- When a user clicks on the **Delete** button on the **Wine details** page a bootstrap modal pops up in the center and ask the user to confirm.
- This Modal is practically the same as the Delete recipe modal.
- After deleting the Wine a success message will be displayed at the top of the screen.

![Delete wine](readme-docs/images/delete-wine.jpg)

[Back to the top](#the-recipe-blog)
- - -

### Register Page
- The **Register** page has grey banner running accross the page and it has an image at the right hand side of the banner. In the center of the Banner is a green heading saying **Sign Up** and
beneath that it tells the user if they already have an account they can click here to go to the login page.
- Benath this is a centered from so that user can enter a **Username**, a **Email** which is optional and then enter the **password** which they will have to confirm by entering it again.
- At the bottom of the from there is a green **Signup** button.
- When the user fills out the form and clicks the **Signup** button then they will be logged in and redirected to the home page.
- The register nav link is not visible when a user is already signed in.

![Register](readme-docs/images/register.jpg)
- - -

### Login Page
- The **login** page is similar to the register page as it has a grey banner running accross the page and it has an image at the left hand side of the banner. In the center of the Banner is a green heading saying **Sign In** and underneath  it tells the user if they dont have an account they can click here to go to the register page.
- Below the banner and center is the login form with the **Username** and **Password**  fields and a **Remember Me** checkbox. At the bottom of the form is a green ** SIGN IN** Button and once clicked it signs the user in and redirect them to the home page.
- The login Nav link changes to a logout link when the user is signed in.

![Signin](readme-docs/images/signin.jpg)
- - -

### The Logout page
- The **logout** page follows the same style as the regiser and login pages with a grey banner accross the screen, It has a green heading that says **Sign out** and as the user if they are sure they want to sign out. Below this is a green **Sign Out** button which when clicked signs the user out.

![Signout](readme-docs/images/signout.jpg)
- - -

## Technologies Used

### Languages, Tools and Frameworks
- [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq) was used to create the wireframes.
- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the mark up.
- [CSS](https://en.wikipedia.org/wiki/CSS)  was used to style the site.
- [Django](https://www.djangoproject.com/) was the framework that was used.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), django is a python framework.
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) was used to style the site.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for interactiveness.
- [Gitpod](https://www.gitpod.io/about) was used to create this site and then push everything to github.
- [Visual Studio Code](https://en.wikipedia.org/wiki/Visual_Studio_Code) was used to work on the site locally.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) is used to host this site.
