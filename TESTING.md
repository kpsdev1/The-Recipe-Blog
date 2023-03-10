## Validator Testing

### HTML
All the site pages were run through the W3C validator to check for any issues and HTML syntax errors. The W3C validator can be found [here](https://validator.w3.org/). As you can see from the below screenshots there are no errors.

<details>
    <summary>Home Page</summary>  
    
![home validation ](readme-docs/images/htmlhome.jpg)  
</details>
  
<details>
    <summary>Recipes page</summary>  
    
![Recipes validation](readme-docs/images/htmlrecipes.jpg)  
</details>  

<details>
    <summary>Wines Page</summary>  
    
![Wines validation](readme-docs/images/htmlwines.jpg)
</details>  
  
<details>
    <summary>Add Wine Page</summary>  
    
![Add wine validation](readme-docs/images/htmladdwine.jpg)
</details> 

<details>
    <summary>edit Wine Page</summary>  
    
![edit wine validation](readme-docs/images/htmleditwine.jpg)
</details> 

<details>
    <summary>Register Page</summary>  
    
![Register validation](readme-docs/images/htmlregister.jpg)
</details> 

<details>
    <summary>Login Page</summary>  
    
![Add wine validation](readme-docs/images/htmllogin.jpg)
</details> 

<details>
    <summary>Logout Page</summary>  
    
![Add wine validation](readme-docs/images/htmllogout.jpg)
</details> 

The **Add Recipe** and **Edit Recipe** pages threw errors in the Validator that were related to the **Summernote** library that I used. I ignored these errors as it was not in any code I had written and because it is a popular django library I presume these are false positives. Below you can see a screenshot of the errors.

![Register validation](readme-docs/images/htmladdrecipe.jpg)
- - -

### CSS
- The CSS stylesheet was put through the W3C Jiqsaw validator to see if there was any errors. The W3C Jiqsaw validator can be found [here](https://jigsaw.w3.org/css-validator/)  .
- As you can see from the below screenshot of the result there were no errors.

![Css Validator screenshot](readme-docs/images/css-validator.jpg)  
- - -

### JavaScript
- The Javascript file was put through Jshint code validator to see if there were any errors. Jshint can be found [here](https://jshint.com/).
- As you can see from the below screenshot, there were no errors.

![JS Validator screenshot](readme-docs/images/js-testing.jpg)  
- - -

### Python
- I tested the project using the PEP8 validator in gitpod, this I had installed from my previous project, but it can be installed by running **pip3 install pycodestyle** then searching for **Python**, Select **Linter** and then select **pycodestyle**. The PEP8 erorrs would then be underlined in red and also listed in **Problems tab**. This returned no errors.
- I also tested the site on **Code Institutes pep8 online** website. Which casn be found [here](https://pep8ci.herokuapp.com/). As you can see from the below screenshots, no errors were found.

##### Meals App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing admin.py file](readme-docs/images/adminpy.jpg)  
</details>
  
<details>
    <summary>forms.py</summary>  
    
![image of Python testing forms.py file](readme-docs/images/formspy.jpg)  
</details>  

<details>
    <summary>models.py</summary>  
    
![image of Python testing models.py file](readme-docs/images/modelspy.jpg)
</details>  
  
<details>
    <summary>urls.py</summary>  
    
![image of Python testing urls.py file](readme-docs/images/urlspy.jpg)
</details>  

<details>
    <summary>views.py</summary>  
    
![image of Python testing views.py file](readme-docs/images/viewspy.jpg)
</details>  

##### Wines App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing admin.py file in wine app](readme-docs/images/wine-adminpy.jpg)  
</details>
  
<details>
    <summary>forms.py</summary>  
    
![image of Python testing forms.py file in wine app](readme-docs/images/wine-formspy.jpg)  
</details>  

<details>
    <summary>models.py</summary>  
    
![image of Python testing models.py file in wine app](readme-docs/images/wine-modelspy.jpg)
</details>  
  
<details>
    <summary>urls.py</summary>  
    
![image of Python testing urls.py file in wine app](readme-docs/images/wine-urlspy.jpg)
</details>  

<details>
    <summary>views.py</summary>  
    
![image of Python testing views.py file in wine app](readme-docs/images/wine-viewspy.jpg)
</details>  

**#** Just to note, the settings.py file gave some **line too long** errors which are related to the default authorization, which I was told can be ignored in this file.
- - - 

### Lighthouse
Lighthouse in chrome dev tools was used to generate a report that tests the sites **Performance**, **Accessibility**, **Best Practices** and **Seo**. 
![chrome browser test](readme-docs/images/lighthouse.jpg)
- - - 

## Browser and Device Testing
- In order to make sure the site was fully responsive and compatible with different browsers and devices, I tested the site on multiple browsers and devices. 
- The browsers I tested the site on **chrome**, **edge** and **Firefox**, when using **chrome** i was able to use the dev tools and test the site on many different device sizes  like **iphones 5, 6, 7, 8, X, SE and 12 pro**, **Ipad mini and air** , and **samsung s9+ and s20 ultra**, the site worked as expected on all.
- I also tested the site on a number of real mobile and tables, the devices i tested on were **Samsung S8 and a53**, **Ipad 7** and **Iphone 7 and 11**.
- From testing the site on multiple browsers and devices, along with different screen widths, I can confirm that the site is fully responsive and compatible with multiple browsers and devices as you will see from the screenshots below.

#### Browser Screenshots

<details>
    <summary>Chrome</summary>  

![chrome browser test](readme-docs/images/chrome.jpg)
</details>  

<details>
    <summary>Edge</summary>  

![edge browser test](readme-docs/images/edge.jpg)
</details>  

<details>
    <summary>Firefox</summary>  

![firefox browser test](readme-docs/images/firefox.jpg)
</details>

<details>
    <summary>Chrome Dev tools Iphone 5</summary>  

![Iphone 5 image](readme-docs/images/iphone5.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Iphone 6, 7, 8</summary>  

![Iphone 6,7,8 image](readme-docs/images/iphone678.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Iphone SE</summary>  

![Iphone SE image](readme-docs/images/iphonese.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Iphone X</summary>  

![Iphone X image](readme-docs/images/iphonex.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Iphone 12 Pro</summary>  

![Iphone 12 image](readme-docs/images/iphone12.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Ipad Mini</summary>  

![Ipad mini image](readme-docs/images/ipadmini.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Ipad air</summary>  

![Ipad Air image](readme-docs/images/ipadair.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Samsung S9 </summary>  

![Samsung S9 image](readme-docs/images/s9.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Samsung S20 Ultra</summary>  

![Samsung S20 image](readme-docs/images/s20.jpg)
</details>  
- - - 

#### Real Device Screenshots

<details>
    <summary>Samsung a53</summary>  

![Samsung a53 image](readme-docs/images/a53.jpg)
</details>  

<details>
    <summary> Iphone 11</summary>  

![Iphone 11 image](readme-docs/images/iphone11.jpg)
</details>  

<details>
    <summary> Ipad 7</summary>  

![Ipad 7 image](readme-docs/images/ipad7.jpg)
</details>  
- - - 


## User Story Testing

##### Navigation
*As a User I can easily navigate around the website so that i can view different pages and sections of the site.*
 - The Navigation at the top of the page is easy to navigate and the current page link is bold which clearly indicates what page you are on.


#### Register
*As a User I can Create and account so that I can view recipe details and add my own.*
 - In the Navigation bar at the top of the page, if a User clicks on the Register link, they will be brought to the registeration page wehere they can sign up, once they sign up they will be able to access full functionality of the site.
 
#### Login | Logout
*As a User I can Sign-in/ Sign-out so that can access features when signed in and sign-out so that no one can access my account.*
 - When a User is not logged in the login link will be visible in at the far right in the navigation bar, the same link will change to logut when the user is logged in.
 - When the User enters their login credentials they wil be able to access the full fuctionality of the site, when the user is logged out they will not have full access on the site and their account will be secure.

#### About The site
*As a User I want to understand what the site is about.*
 - On the home page is an About us section that cleary tells the user what the site is about and how to use it.

#### View Recipes
*As a User I can view the list of recipes so that I can pick one to read.*
 - The user is able to clcik the recipes link in the nav bar and theis will take them to the recipes page where they can view a list of recipes.
 - If they wish to view one in full detail they can click Read More and they will then be able to see the recipe details, the user must be signed in to view the recipe details as if they are not signed in the Read More button will be diabled.
