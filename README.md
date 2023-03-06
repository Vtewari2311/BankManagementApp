# MadHacksProject

## Inspiration
Creating a financial application that makes it easy for users to save money and take advantage of local deals and discounts. The problem being solved is the difficulty that many people face in managing their finances and finding the best deals and discounts in their area. By automating the savings process and using location services to provide targeted deals, the app can help users maximize their savings potential and improve their financial well-being. This project would involves developing a web-based application using the Django framework, integrating payment processing and location-based services, and creating a user-friendly interface for managing finances and accessing local deals.

## What it does
Offers several features to help users save money and take advantage of local deals and discounts. The main feature is the round-up feature, which automatically rounds up users' purchases to the nearest dollar and directs the extra change towards their savings. This feature helps users save money without having to think about it or actively manage their savings.

In addition to the round-up feature, the app also offers location-based services that provide users with access to local deals and discounts. This feature allows users to take advantage of discounts and promotions offered by businesses in their area, helping them save money on everyday purchases.

Overall, the app aims to revolutionize the digital consumer experience by making it easier for users to save money and take advantage of local deals and discounts. It does this by automating the savings process and providing targeted deals through location-based services, all while offering a user-friendly and secure platform for managing finances.

## How we built it
To build a financial application with the round-up feature and location-based services, we used a combination of technologies for both the backend and frontend. We chose Django, a Python web framework that offers features such as database management, user authentication, and URL routing, as our backend technology. We used Python, a powerful scripting language that can handle complex calculations and data processing, making it well-suited for financial applications.

For the frontend, we used HTML and CSS to create user interfaces that are responsive and easy to use. We also utilized Bootstrap, a popular CSS framework, to create a consistent and professional-looking design.

To implement the round-up feature, we integrated with a payment processor that supports automatic rounding up of transactions. The extra change was then directed towards a savings account or investment account. We implemented location-based services using a combination of GPS and IP address tracking, allowing the application to provide targeted deals and discounts to users based on their location.

Overall, building an application with these features required a solid understanding of both backend and frontend development, as well as experience with integrating with payment processors and location-based services.

## Challenges we ran into
During the development of the financial application with the round-up feature and location-based services, we encountered several challenges that required creative problem-solving and collaboration.

One of the main challenges was integrating with the payment processor to enable the round-up feature. We had to carefully read through the documentation and test various configurations to ensure that the transactions were being properly rounded up and directed towards the savings account or investment account.

Another challenge was implementing the location-based services. We had to experiment with different methods of GPS and IP address tracking to accurately determine the user's location and provide targeted deals and discounts. We also had to consider user privacy and make sure that the location data was being handled securely.

Finally, we faced challenges with ensuring a smooth and seamless user experience across different devices and platforms. We had to test the application thoroughly and make adjustments to the design and functionality to ensure that it worked well on both desktop and mobile devices.

Despite these challenges, we were able to successfully overcome them through collaboration and persistence, resulting in a functional and user-friendly financial application.

In addition to the challenges mentioned earlier, we also faced some issues in our views.py file when handling GET and POST requests. We had to carefully define the logic for each request and ensure that the appropriate data was being passed between the frontend and backend.

We also had to implement CSRF (Cross-Site Request Forgery) protection to ensure the security of our application. This involved generating a unique token for each user session and including it in each form submission. We had to modify our views.py file to include the CSRF token in our form submissions and validate it on the server side to prevent unauthorized access.

Integrating CSRF protection and properly handling GET and POST requests required some additional time and effort, but it was essential for ensuring the security and functionality of our application.

## Accomplishments that we're proud of
We are proud of creating a user-friendly and responsive design that works well on both desktop. We were able to incorporate Bootstrap to create a consistent and professional-looking design, while also ensuring that the application was easy to use and navigate.

Overall, we are proud of the hard work and dedication that went into the development of our financial application, and we believe that it has the potential to make a positive impact on users' financial lives.

## What we learned
During the development of our financial application with the round-up feature and location-based services, we learned a great deal about both backend and frontend development, as well as the importance of security and user experience.

From a technical standpoint, we gained experience in using Django and Python for the backend, as well as HTML, CSS, and JavaScript for the frontend. We also learned about integrating with payment processors and using location-based services to provide targeted deals and discounts.

In addition to technical skills, we also learned about the importance of security in web development. We had to carefully implement CSRF protection to prevent unauthorized access to our application and ensure the safety of user data. We also had to handle user location data securely to protect user privacy.

Finally, we learned about the importance of user experience in creating successful web applications. We had to create a design that was both visually appealing and easy to use, while also ensuring that the application was responsive and worked well on both desktop.

Overall, we gained valuable experience and knowledge throughout the development of our financial application, and we believe that this will serve us well in future web development projects.

## What's next for Bank Management App
Moving forward, there are several improvements and new features that we plan to add to our Bank Management App. First and foremost, we need to fix the round-up feature, which did not work as expected during our initial testing. We will continue to work on this functionality to ensure that it accurately rounds up transactions and directs the extra change towards the user's savings or investment account.

Additionally, we plan to add more advanced financial management features, such as budget tracking, investment advice, and debt management tools. We also plan to expand the location-based services to provide users with more targeted deals and discounts based on their interests and preferences.

In terms of user experience, we plan to make several improvements to the design and user interface of the application. This will include streamlining the user registration and login process, improving the navigation and usability of the application, and making it easier for users to track their financial goals and progress.

Finally, we plan to continue to prioritize security and privacy in our Bank Management App. We will ensure that all user data is handled securely and implement additional security features as needed to prevent unauthorized access and protect user privacy.

Overall, we are excited about the potential of our Bank Management App and look forward to continuing to improve and expand its features and functionality.
