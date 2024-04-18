#BoboShop
<h1 align="center">BoboShop</h1>

[View the live project here](https://boboshop-4896cb751ade.herokuapp.com/)

At BoboShop, we take pride in using only the finest, high-quality ingredients to craft our cakes. Each cake is made from scratch by our team of skilled pastry chefs, who meticulously blend together premium butter, fresh eggs, sweet vanilla, and other carefully selected components. Whether you're in the mood for a rich, decadent chocolate cake or a light and airy lemon chiffon, we have a wide selection of flavors to satisfy every palate.

Beyond classic flavors, we also offer innovative and unique cake designs to make your special occasions even more memorable. From elegant tiered wedding cakes to whimsical birthday cakes adorned with edible flowers, our cakes are not only delicious, but true works of art. We work closely with each customer to customize the cake of their dreams, ensuring that every detail is perfect.

![Mockup](documentation/headimage.png)

## Index – Table of Contents
- [Index – Table of Contents](#index--table-of-contents)
- [User Experience (UX)](#user-experience-ux)
- [Features](#features)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Bugs](#bugs)
- [Acknowledgements](#acknowledgements)


## User Experience (UX)

- ### User stories
  - #### A. First Time Visitor
    1. As a first time visitor, I want to see the most rated cakes.
    3. As a first time visitor, I want to purchase without creating an account.
    4. As a first time visitor, I want an easy and secure checkout process.
    4. As a first time visitor, I want an order confirmation.

  - #### B. Returning Visitor
    1. As a first time visitor, I want to be able to register on website.
    2. As a returning visitor, I want to be able to log in to the website.
    3. As a returning visitor, I want to be able to favourite cakes.
    4. As a returning visitor, I want to be able to change my password.
    5. As a returning visitor, I want to be able to add, edit or delete reviews for cakes.
  - #### C. Administrator
    1. As an administrator, I want to be able to add cakes.
    2. As an administrator, I want to be able to edit cakes.
    2. As an administrator, I want to be able to delete the cakes.
    2. As an administrator, I want to be able to track the cakes stats.
    2. As an administrator, I want to be able to track sales.


## Features
 - ### NavBar
    This navigation bar provides a user-friendly interface for navigating through various product categories on a website. It includes dropdown menus for easy access to different types of cakes, including layer cakes, sponge cakes, and cheesecakes. Users can easly access their account and see the total price of the bag content. The navigation bar is responsive, ensuring accessibility across different devices.
    ![Mockup](documentation/features/navbar.png)
- ### Index Page
   Index page consist of a background image with a welcome message and a button to redirect users to the cake list.
    ![Mockup](documentation/features/index.png)

- ### Free Delivery banner
    Right under the navbar, there is a section where visitors are informed about the delivery threshold.
    ![Mockup](documentation/features/deliverybanner.png)
- ### Toast Messages
    Toast messages are displayed for many different event types, including Success, Error, Info, and Warning. They serve as concise notifications that inform users about various outcomes, such as successful completion of tasks or encountering errors. Toast messages offer great functionality in enhancing user experience by promptly delivering relevant information in a non-intrusive manner. For instance, toast messages are very useful for following the shopping bag while users are adding products, ensuring they stay informed about their shopping progress.
    ![Mockup](documentation/features/toast.png)
- ### Sign In and Sign Up 
    Sign in and Sign up functionalities are essential components of our cake website, providing users with personalized access to a range of features and services. Existing users can easily access their accounts by signing in, this process  grants them access to their saved preferences, order history and profile.
    ![Mockup](documentation/features/signup.png)

    ![Mockup](documentation/features/login.png)

- ### User Profile
  Enables users to access and modify their default delivery details. Also shows a list of orders placed by the user.
    ![Mockup](documentation/features/profile.png)

- ### Products view
  This page is displaying products in a grid layout tailored to the user's device. It serves as a hub for displaying all products, along with options for filtering by category and search parameters. Additionally, users can access their favorite products through the "My Account" menu. Results on this page can be sorted using various criteria available in the "sort by" menu. Each product is tagged with ratings, categories and whether it's on whishlist for another user. For superusers, there's the added feature of displaying the total number of favorites a product has, along with links for editing and deleting products. Lastly, a "back to top" button is conveniently included below.
  ![Mockup](documentation/features/productsview.png)

- ### Product detail
  This page offers users a detailed product description along with the information tags featured on the product page. Here, users can conveniently add or remove the product from their favorites. Additionally, there's a quantity selector input allowing users to add the item to their bag or return to the products view. For superusers, the page also showcases the total number of favorites the product has gain from users, along with links for editing and deleting the product.
  ![Mockup](documentation/features/productdetail.png)

- ### Review Section
  The website's review section provides users with a way to share their experiences, opinions, and ratings. It enables users to leave feedback on products, services, or any aspect of our platform. With this feature, users can make informed decisions based on real user experiences and insights.
  ![Mockup](documentation/features/reviewsection.png)

- ### Shopping Bag
  This feature offers customers a platform to review their selected purchases before proceeding to checkout. The page showcases a comprehensive list of products added to the user's bag, featuring each item's thumbnail image, title, price, quantity selection with the option to remove, and line total/subtotal. A user-friendly quantity selector, enhancing ease of use. The page displays the bag total, delivery cost, and grand total, along with buttons to proceed to checkout or return to shopping. Additionally, if the free delivery threshold hasn't been met, a note is displayed to guide customers on how much more they need to spend to qualify for free delivery.
  ![Mockup](documentation/features/shoppingbag.png)

- ### Checkout page
  The checkout process provides users with an overview of their order and a form to finalize payment. For registered users, the address information is automatically populated, streamlining the checkout experience.

  Key features of the checkout process include:

  Guest Checkout: Non-registered users can complete their purchases without creating an account, simplifying the process for first-time shoppers and reducing barriers to conversion.
  Navigation Buttons: The interface includes "Return to Bag" and "Complete Order" buttons, allowing users to easily navigate back to their shopping bag or proceed with the order. A warning message informs users that their card will be charged upon completing the order.

  Loading Overlay: During payment processing, a loading overlay is displayed to prevent interruptions and ensure a seamless experience.
  Secure Payment Processing: The checkout system integrates with Stripe, a reliable and secure payment gateway, to handle payment transactions.
  ![Mockup](documentation/features/checkout.png)

- ### Order Confirmation
  Upon successful completion of the payment webhook, the system takes two important actions:

  Order Confirmation Display: The user is presented with a confirmation page and a toast message, providing them with a summary of their order details. This confirmation serves as a visual acknowledgment that the payment has been processed successfully and the order has been placed.
  ![Mockup](documentation/features/orderconfirmation.png)


  Email Notification: Simultaneously, an email is automatically sent to the customer's provided email address. This email contains the order confirmation details, serving as an additional record of the transaction and providing the customer with a reference for future inquiries or follow-ups.
  ![Mockup](documentation/features/orderemail.png)

- ### Cake statistics
  The cake statistics feature provides website administrators with valuable insights into product performance and user engagement. It offers a comprehensive overview of two key metrics:

  Total Sales per Product: The statistics display the total sales generated by each cake product. This information allows administrators to identify top-selling cakes and understand which products are driving the most revenue.

  Favorite Count: The statistics also showcase how many times each cake has been added to users' favorites. This metric indicates the popularity and desirability of individual cakes among the website's users.

  By analyzing these statistics, administrators can gain a deeper understanding of user preferences, identify trends, and make informed decisions to optimize product offerings and promote popular cakes. The cake statistics empower administrators with data-driven insights to enhance the website's performance and user experience.
  ![Mockup](documentation/features/cakesales.png)

- ### Oder stats
  The order stats feature provides website administrators with a powerful tool to monitor and analyze every order placed on the platform. It offers a comprehensive view of order details, enabling administrators to track and manage orders effectively.

  With the order stats, administrators can:

  Track Every Order: The system captures and records all orders placed on the website, creating a complete history of transactions. Administrators have access to a detailed list of orders, allowing them to easily locate and review specific orders as needed.

  View Order Details: For each order, administrators can access a range of relevant information. This may include the order number, customer details, product(s) purchased, quantities, prices, shipping information, payment status, and any other pertinent data associated with the order.
  ![Mockup](documentation/features/orderstats.png)

- ### Product Management
  The website provides user administrators with powerful control over the product catalog. Through a dedicated interface, administrators have the ability to manage products effectively, ensuring that the website offers an up-to-date and accurate selection of items.

  The key capabilities of the product management feature include:

  Edit Products: Administrators can modify existing product details to keep the information current and relevant. They can update product names, descriptions, prices, images, categories, and any other associated attributes.
  ![Mockup](documentation/features/productedit.png)


  Add New Products: When new items need to be introduced to the website, administrators can seamlessly add them to the product catalog. They can input all the necessary details, such as product name, description, price, images, and categorization. This enables the website to expand its offerings and stay competitive in the market.
  ![Mockup](documentation/features/addproduct.png)


  Delete Products: In cases where a product is no longer available, out of stock, or needs to be removed from the website for any reason, administrators have the power to delete it.
  ![Mockup](documentation/features/productdelete.ong.png)
  
- ## Design
   - ### Color scheme
    As part of designing I have used the pallete generated using [coolors.co](https://coolors.co/)
    ![Mockup](documentation/design/palette.png)
   - ### Typography
    Default bootstrap4 has been used to font styling.
   - ### Database schema
     PostgreSQL is used as relational database using ElephantSQL as a host service
      ![Mockup](documentation/design/dbschema.png)

- ## Wireframes 
  - ## Home Page <br>
    [Home page desktop](documentation/design/IndexDesktop.png)<br>
    [Home page mobile](documentation/design/IndexMobile.png)
  - ## Products 
    [Favourite Desktop](documentation/design/ProductsDesktop.png)<br>
    [Favourite Mobile](documentation/design/ProductsMobile.png)
  - ## Product details
    [My Recipes Dekstop](documentation/design/ProductDetailsDesktop.png)<br>
    [My Recipes Mobile](documentation/design/ProductDetailsMobile.png)
  - ## Profile
    [Categories Desktop](documentation/design/ProfileDesktop.png)<br>
    [Categories Mobile](documentation/design/ProfileMobile.png)
  - ## CakeSales
    [Edit Categories Desktop](documentation/design/CakeSalesDesktop.png)<br>
    [Edit Categories Mobile](documentation/design/CakeSalesMobile.png)

    ## Technologies Used
  - ### Languages Used
    -   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    -   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    -   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   [Python](https://www.python.org/)
   
  - ### Frameworks, Libraries and Programs Used
    -   [Git:](https://git-scm.com/) was used for version control by utilising VSCode terminal to commit to Git and Push to GitHub.
    -   [GitHub:](https://github.com/) was used as the repository for the project's code after being pushed from Git.
    -   [Visual Studio Code](https://code.visualstudio.com/) was used as IDE editor.
    -   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes.
    -   [Django:](https://www.djangoproject.com/) Micro web framework written in Python.
    -   [ElephantSQL:](https://www.elephantsql.com/) PostgreSQL database hosting service for hosting website database.
    -   [Bootstrap](https://getbootstrap.com/) For making the website responsive.
    -   [DbSchema:](https://dbschema.com/) For creating the database schema logic and     diagram.
## Testing
  - ### For testing please refer to the [TESTING.md](/TESTING.md)