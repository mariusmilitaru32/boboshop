Back to [README.md](/README.md)

- ## Validator Testing
  - ### HTML Validator
    - [HTML results Index page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2F): no errors
    - [HTML results Products page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Fproducts%2F): no errors
    - [HTML results Product detail page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Fproducts%2F4%2F): no errors
    - [HTML results Bag page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Fbag%2F): no errors
    - [HTML results Checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Fcheckout%2F): no errors
    - [HTML results Register page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Faccounts%2Fsignup%2F): no errors
    - [HTML results Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Faccounts%2Flogin%2F): no errors
    - [HTML results Profile page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Fprofile%2F): no errors
    - [HTML results Cake stats page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Fcake_tracker%2Fstats%2F): no errors
    - [HTML results Order stats page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Fcake_tracker%2Fmanage_orders%2F): no errors
    - [HTML results Favourite page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboboshop-4896cb751ade.herokuapp.com%2Fproducts%2Ffavorites%2F): no errors

  - ### CSS Validator
    -base.css
    ![Mockup](documentation/testing/basecss.png)

    -checkout.css
    ![Mockup](documentation/testing/checkoutcss.png)

  - ### JsLint Validator
    - stripe_element.js
    ![Mockup](documentation/testing/stripeelementjs.png)
    - Sort selector
    ![Mockup](documentation/testing/sort%20selector.png)
    - Country field
    ![Mockup](documentation/testing/sort%20selector.png)
    - Quntity input
    ![Mockup](documentation/testing/quantityinput.png)
- ## Browser Compatibility
  - Testing has been carried out on the following browsers with no issues:
    - Chrome Version 119.0.6045.124 (Official Build) (64-bit)
    - Firefox Version 119.0.1 (64-bit)
    - Edge Version 119.0.2151.58 (Official build) (64-bit)

 - ## Python Linter by CodeInstitute
  - ### products/views.py 
    ![Mockup](documentation/testing/productsview.png)
  - ### products/views.py 
    ![Mockup](documentation/testing/productsurls.png)
  - ### products/models.py
    ![Mockup](documentation/testing/productsmodels.png)
  - ### products/forms.py
    ![Mockup](documentation/testing/productsforms.png)
  - ### profile/views.py
    ![Mockup](documentation/testing/profilesviews.png)
  - ### profiles/models.py
    ![Mockup](documentation/testing/profilesmodels.png)
  - ### profiles/forms.py
    ![Mockup](documentation/testing/profilesforms.png)
  - ### checkout/webhook.py
    ![Mockup](documentation/testing/checkoutwebhook.png)
  - ### checkout/webhook_handeler.py
    ![Mockup](documentation/testing/checkoutwebhandler.png)
  - ### checkout/views.py
    ![Mockup](documentation/testing/checkoutviews.png)
  - ### checkout/models.py
    ![Mockup](documentation/testing/checkoutmodels.png)
  - ### checkout/forms.py
    ![Mockup](documentation/testing/checkoutforms.png)
  - ### cake_tracker/views.py
    ![Mockup](documentation/testing/caketrackerviews.png)
  - ### cake_tracker/models.py
    ![Mockup](documentation/testing/caketrackermodels.png)
  - ### bag/views.py
    ![Mockup](documentation/testing/bagviews.png)
  - ### bag/contexts.py
    ![Mockup](documentation/testing/bagcontext.png)

- ## User Story Testing
 | User Story                                                                   | Screenshot                                                |
 | ---------------------------------------------------------------------------- | --------------------------------------------------------- |
 | As a first time visitor, I want to see the most rated cakes.                 | ![screenshot](documentation/features/rating.png)          |
 | As a first time visitor, I want to purchase without creating an account.     | ![screenshot](documentation/features/checkout.png)        |
 | As a first time visitor, I want an easy and secure checkout process.         | ![screenshot](documentation/features/securecheckout.png)  |
 | As a first time visitor, I want an order confirmation.                       | ![screenshot](documentation/features/orderemail.png)      |
 | As a first time visitor, I want to see clear product descriptions and images | ![screenshot](documentation/features/description.png)     |
 | As a returning visitor, I want to be able to register in to the website      | ![screenshot](documentation/features/signup.png)          |
 | As a returning visitor, I want to be able to log in to the website.          | ![screenshot](documentation/features/login.png)           |
 | As a returning visitor, I want to be able to favourite cakes.                | ![screenshot](documentation/features/addfavorite.png)     |
 | As a returning visitor, I want to be able to update my profile.              | ![screenshot](documentation/features/profile.png)         |
 | As a returning visitor, I want to be able to change my password.             | ![screenshot](documentation/features/passwordresset.png)  |
 | As a returning visitor, I want to be able to add, edit or delete reviews for cakes.| ![screenshot](documentation/features/reviewsection.png)|
 | As a administrator, I want to be able to add cakes.                          | ![screenshot](documentation/features/addproduct.png)      |
 | As a administrator, I want to be able to edit cakes.                         | ![screenshot](documentation/features/productedit.png)     |
 | As a administrator, I want to be able to delete the cakes.                   | ![screenshot](documentation/features/deletecake.png)      |
 | As a administrator, I want to be able to see the order details.              | ![screenshot](documentation/features/orderstats.png)      |
 | As a administrator, I want to be able to track sales.                        | ![screenshot](documentation/features/cakesales.png)       |

 - ## Lighthouse test

 | Page         | Device  | Screenshot                                                             | Notes                                          |
| ------------ | ------- | ---------------------------------------------------------------------- | ---------------------------------------------- |
| Home         | Mobile  | ![screenshot](documentation/testing/lighthouse/indexmobile.png)        |                                                |
| Home         | Desktop | ![screenshot](documentation/testing/lighthouse/indexdesktop.png)       |                                                |
| Favourites   | Mobile  | ![screenshot](documentation/testing/lighthouse/favouritemobile.png)    |                                                |
| Favourites   | Desktop | ![screenshot](documentation/testing/lighthouse/favouritedesktop.png)   |                                                |
| Products     | Mobile  | ![screenshot](documentation/testing/lighthouse/productsmobile.png)     |    68 performance due to image rendering       |
| Products     | Desktop | ![screenshot](documentation/testing/lighthouse/productsdekstop.png)    |                                                |
| Product details     | Mobile  | ![screenshot](documentation/testing/lighthouse/productdetailsmobile.png)|                                        |
| Product details     | Desktop | ![screenshot](documentation/testing/lighthouse/productdetailsdesktop.png)|                                       |
| Cake Sale    | Mobile  | ![screenshot](documentation/testing/lighthouse/cakesalesmobile.png)|                                                    |
| Cake Sale    | Desktop | ![screenshot](documentation/testing/lighthouse/cakesalesdesktop.png)|                                                   |
| Order Stats  | Mobile  | ![screenshot](documentation/testing/lighthouse/orderstatsmobile.png)|                                                   |
| Order Stats  | Desktop | ![screenshot](documentation/testing/lighthouse/orderstatsdesktop.png)|                                                  |
| Profile      | Mobile  | ![screenshot](documentation/testing/lighthouse/profilemobile.png)   |                                                   |
| Profile      | Desktop | ![screenshot](documentation/testing/lighthouse/profiledesktop.png)  |                                                   |
| Bag          | Mobile  | ![screenshot](documentation/testing/lighthouse/bagmobile.png)       |                                                   |
| Bag          | Desktop | ![screenshot](documentation/testing/lighthouse/bagdesktop.png)      |                                                   |
| Checkout     | Mobile  | ![screenshot](documentation/testing/lighthouse/checkoutmobile.png)  |                                                   |
| Checkout     | Dekstop  | ![screenshot](documentation/testing/lighthouse/checkoutdesktop.png)|                                                   |

- ## Responsiveness
  The website has been tested on different screen sizes using Google Chrome developer tool simulating devices like Iphone 14 Pro Max, Samsung S20 Ultra and Surface Pro 7 with no issues reported.
   - #### Iphone 14 Pro Max DevTool Screenshoot
    ![Mockup](documentation/testing/iphone14resp.png)
    ![Mockup](documentation/testing/cakesalesresp.png)
    
   - #### Iphone SE for small mobile screens
    ![Mockup](documentation/testing/iphoneseresp.png)
    ![Mockup](documentation/testing/iphoneseproduct.png)
   - #### Desktop
    ![Mockup](documentation/testing/productsdesktopres.png)
    ![Mockup](documentation/testing/orderstatsdekstop.png)
    ![Mockup](documentation/testing/productdetailresp.png)
    