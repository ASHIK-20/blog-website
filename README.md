# blog-website
website learners task (blog webpage) 
STRUCTURE OF API 
1. Routes and Endpoints:
    `/`: Main page displaying blog posts and navigation.
   /login: Handles user login and displays login forms.
   /signup: Handles user registration and displays signup forms.
   /logout: Logs the user out by removing session data.
   /add_post: Displays the form to add a new blog post and handles post addition.
   /edit_post/<int:index>: Allows users to edit existing blog posts based on index.
   /delete_post/<int:index>: Allows users to delete existing blog posts.
   /add_comment/<int:index>: Lets users add comments to specific blog posts.

2. HTTP Methods:
   -GET: Retrieve and display content, including web pages and forms.
   -POST: Submit data to the server, e.g., login credentials, blog posts, and comments.
   -DELETE: Not explicitly used, but typically for deleting resources (e.g., blog posts)
   
4. Session Management:
    Utilizes Flask's 'session' object to manage user sessions.
   Stores the user's username in the session upon login for session-based authentication.
   
6. Authentication and Authorization:
    Authentication: Performed during login to verify user identity.
    Authorization: Ensured by checking if a user is logged in before performing actions like adding, editing, or deleting posts.
   
8. Templates and Forms:
   HTML templates generate web pages, while forms gather user input for various actions.
   Forms included for login, registration, and post submission
   
10. Flash Messages:
   Used to provide user feedback, such as success or error messages

12. Data Storage:
   Stores data (users, blog posts, comments) in memory as Python lists and dictionaries.

