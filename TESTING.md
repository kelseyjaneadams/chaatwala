# Testing

## Manual Testing

Testing was done throughout site development.

Usability was tested with the below user acceptance testing.

## Navbar
| #  | User Actions                                | Expected Results                                        | Y/N | Comments |
|----|-------------------------------------------|--------------------------------------------------------|-----|----------|
| 1  | Visit the website                         | Navbar loads and is visible at the top                | Y   |          |
| 2  | Click on "Menus"                          | Redirects to the home page                            | Y   |          |
| 3  | Click on "Book a Table"                   | Redirects to the bookings page                        | Y   |          |
| 4  | Click on "Profile" (while logged in)      | Redirects to the user's profile page                  | Y   |          |
| 5  | Click on "Logout" (while logged in)       | User is logged out and redirected to home page        | Y   |          |
| 6  | Click on "Register" (while logged out)    | Redirects to the sign-up page                         | Y   |          |
| 7  | Click on "Login" (while logged out)       | Redirects to the login page                           | Y   |          |
| 8  | Click the mobile menu (hamburger icon)    | Expands the navigation menu                          | Y   |          |
| 9  | Click outside the mobile menu             | The mobile menu collapses                            | Y   |          |


## Footer

| #  | User Actions                                | Expected Results                                        | Y/N | Comments |
|----|-------------------------------------------|--------------------------------------------------------|-----|----------|
| 1  | Visit any page on the website             | Footer is visible at the bottom of the page           | Y   |          |
| 2  | Click on the Facebook icon                | Opens Facebook in a new tab                           | Y   |          |
| 3  | Click on the Twitter icon                 | Opens Twitter in a new tab                            | Y   |          |
| 4  | Click on the Instagram icon               | Opens Instagram in a new tab                          | Y   |          |
| 5  | Click on the YouTube icon                 | Opens YouTube in a new tab                            | Y   |          |
| 6  | Click on the TikTok icon                  | Opens TikTok in a new tab                             | Y   |          |
| 7  | Check the copyright text                  | Displays "© 2024 Chaatwala"                          | Y   |          |

## Menus/Home Page

| #  | User Actions                         | Expected Results                                          | Y/N | Comments |
|----|--------------------------------------|----------------------------------------------------------|-----|----------|
| **Hero Section** | | | | |
| 1  | Load the home page                   | The hero image should be visible at the top              | Y   |          |
| **Menu Section** | | | | |
| 2  | Scroll to menu section               | Menu heading and subheading should be displayed          | Y   |          |
| 3  | Click on "Food Menu" image           | Opens the Food Menu in a new tab                         | Y   |          |
| 4  | Click on "Drinks Menu" image         | Opens the Drinks Menu in a new tab                       | Y   |          |
| 5  | Click on "Kids Menu" image           | Opens the Kids Menu in a new tab                         | Y   |          |
| 6  | Click on "Sweet Menu" image          | Opens the Sweet Menu in a new tab                        | Y   |          |
| **Customer Reviews Section** | | | | |
| 7  | Scroll to reviews section            | Reviews heading should be visible                        | Y   |          |
| 8  | Check for reviews                     | Approved reviews should be displayed                     | Y   |          |
| 9  | Check for pending reviews            | Pending reviews should only be visible to their authors  | Y   |          |
| 10 | Submit a review (logged in user)     | Review should be added and appear with "Pending" status  | Y   |          |
| 11 | Submit a review (not logged in)      | User should be prompted to log in                        | Y   |          |
| **Navigation & Buttons** | | | | |
| 12 | Click "Log in to leave a review"     | Redirects to login page                                  | Y   |          |
| 13 | Click "Submit Review" (empty form)   | Validation errors should appear                          | Y   |          |

## Booking Page

| #  | User Actions                          | Expected Results                                    | Y/N | Comments |
|----|--------------------------------------|--------------------------------------------------|-----|----------|
| 1  | Visit the Booking Page               | The page loads successfully without errors      | Y   |          |
| 2  | Enter a contact name                 | Name is accepted                                | Y   |          |
| 3  | Enter a valid number of guests       | Only numbers 1-6 are accepted                  | Y   |          |
| 4  | Select a valid booking date          | Future dates are allowed, past dates are blocked | Y   |          |
| 5  | Select an hour and minute for time   | Dropdown menus allow selection                 | Y   |          |
| 6  | Enter a special request (optional)   | Text is accepted                               | Y   |          |
| 7  | Submit the booking form              | Confirmation or error flash message | Y   |          |
| 8  | Try submitting without required fields | Form validation error messages appear         | Y   |          |

## Log In Page

# Manual Testing - Login Page (login.html)

| #  | User Actions                          | Expected Results                                    | Y/N | Comments |
|----|--------------------------------------|--------------------------------------------------|-----|----------|
| 1  | Visit the Login Page                 | The page loads successfully without errors      | Y   |          |
| 2  | Enter a valid email/username         | Input is accepted                               | Y   |          |
| 3  | Enter a valid password               | Input is accepted                               | Y   |          |
| 4  | Click "Log In" button with valid credentials | User is redirected to the profile or home page | Y   |          |
| 5  | Click "Log In" button with incorrect credentials | Displays an error message                     | Y   |          |
| 6  | Click "Forgot Password?" link        | Redirects to password reset page               | Y   |          |
| 7  | Click "Register here" link           | Redirects to the registration page             | Y   |          |
| 8  | Click "Cancel" button                | Redirects to the home page                     | Y   |          |
| 9  | Submit the form with empty fields    | Displays validation errors                     | Y   |          |
