# Chaatwala

## Features

The Chaatwala web application includes the following pages:

- **Home/Menu Page**
- **Book a Table Page**
- **Log In Page**
- **Register Page**
- **Profile Page**
- **Log Out Page**

---

## 🔑 User & Admin Access Levels

### 👥 User Roles & Permissions

| Feature | **Regular User** | **Admin** |
|---------|:--------------:|:------:|
| **Authentication & Account Management** | ✅ Can sign up, log in, and log out | ✅ Full control over all user accounts |
| **Password Reset** | ✅ Can reset their own password | ✅ Can reset any user’s password |
| **Profile Management** | ✅ Can update their profile picture & view their bookings & reviews | ✅ Can update any user’s profile if needed |
| **Booking System** | ✅ Can create, edit, & cancel their own bookings | ✅ Can view, edit, and delete **all** bookings |
| **Booking Status** | ✅ Can see their booking status (Pending, Confirmed, Cancelled) | ✅ Can **change** any booking status |
| **Review System** | ✅ Can submit, edit, and delete their own reviews | ✅ Can **approve, reject, or delete** any review |
| **Review Approval Process** | ❌ Cannot approve reviews (must wait for admin) | ✅ Can approve or reject pending reviews |
| **Viewing Other Users' Reviews** | ✅ Can only see **approved** reviews | ✅ Can see **all reviews** (approved & pending) |
| **Deleting Content** | ❌ Cannot delete other users' reviews or bookings | ✅ Can delete **any** review, booking, or user profile |
| **Admin Dashboard Access** | ❌ No access | ✅ Full access to the Django admin panel |
| **Site Settings & Management** | ❌ No access | ✅ Can update menus, change business hours, and manage users |

---

## 🛠 Navigation & User Interface

### Navbar

#### Logged-Out Users
![Navbar](documentation/features/navbar-unlogged.png)

#### Logged-In Users
![Navbar](documentation/features/navbar-logged.png)

The navbar contains the following links:

- **Menu Page**
- **Book a Table Page**
- **Register Page**
- **Log In Page**

Once a user logs in, additional options appear:

- **Menu Page**
- **Book a Table Page**
- **Profile Page**
- **Log Out Page**

The **restaurant logo** is prominently displayed in the navbar and serves as a clickable link to the **Home/Menu page**.

On smaller screens, the navbar collapses into a **hamburger menu** for better usability.

![Navbar](documentation/features/navbar-burger.png)

The design is intentionally simple to ensure easy navigation.

---

## 🎨 Branding & Design

### Logo
![Logo](documentation/features/logo.png)

Clicking the logo redirects users to the **Home/Menu Page**.

### Footer
![Footer](documentation/features/footer.png)

The footer includes **five social media links**, which open in new tabs when clicked.

---

## 📸 Visual Highlights

### Hero Image
![Hero](documentation/features/hero-image.png)

The hero image provides users with a **glimpse of the restaurant's interior**, allowing them to experience its aesthetic before visiting.

### Menu Title
![MenuTitle](documentation/features/menu-title.png)

The **menu title** clearly indicates the beginning of the restaurant's menu section.

### Menu Categories
![Menus](documentation/features/menu-choices.png)

Users can choose from **four** menu categories:

- **Food Menu**
- **Drinks Menu**
- **Kids Menu**
- **Sweet Menu**

On mobile screens, these options are displayed in **two rows**.

![Menus](documentation/features/menus-mobile.png)

Clicking on a menu option opens a **full menu image** in a new tab.

#### Food Menu
![Menus](documentation/features/food-menu.png)

#### Drinks Menu
![Menus](documentation/features/drinks-menu.png)

#### Kids Menu
![Menus](documentation/features/kids-menu.png)

#### Sweet Menu
![Menus](documentation/features/sweet-menu.png)

---

## ⭐ Reviews Section

The **Reviews section** is located below the menu, providing users with **authentic feedback from previous customers**.

### For Unregistered Users
Users who are **not logged in** will only see **approved reviews** in a **scrollable list**.

![Reviews](documentation/features/reviews-unlogged.png)

To leave a review, users must log in. A **login button** redirects them to the login page. If they don’t have an account, they can register.

![Reviews](documentation/features/reviews-button-unlogged.png)

### For Logged-In Users
Logged-in users **see all of their own pending reviews**. Pending reviews are **greyed out** and include a **message indicating they are awaiting approval**.

![Reviews](documentation/features/review-pending.png)

### Review Submission Form
Below the review section, logged-in users can **submit new reviews**.

The form includes:
- **Rating dropdown menu**
- **Comment field**
- **Submit button**

![Review Form](documentation/features/reviews-form.png)

#### Rating Selection
Users can select a **rating from the dropdown**.

![Rating Dropdown](documentation/features/rating-dropdown.png)

#### Review Submit Button
When a user is ready to submit their review, they click the **Submit Review** button.
![Review Button](documentation/features/review-button.png)

#### Review Success Flash Message
Upon Submitting the review a success flash message will pop up at the top of the page.

![Review Submit Flash Message](documentation/features/review-flash.png)

---

## 📅 Booking System

The **Book a Table page** features a **booking form** where users can make reservations.

![Booking Form](documentation/features/booking-form.png)

### Booking Form Fields
- **Contact Name**
- **Number of Guests (Dropdown)**
- **Booking Date (Date Picker)**
- **Booking Time (Hour & Minute Dropdowns)**
- **Special Requests**
- **Submit Button**

### Interactive Form Features
- **Guest Selection (1-6 guests)**
  
  ![Guest Dropdown](documentation/features/guest-dropdown.png)

- **Date Picker (Prevents selecting past dates)**
  
  ![Date Picker](documentation/features/date-picker.png)

- **Hour Selection (Only shows restaurant opening hours)**
  
  ![Hour Selection](documentation/features/time-hour.png)

- **Minute Selection (Quarter-hour increments)**
  
  ![Minute Selection](documentation/features/time-min.png)

### Submit Button
Once a user fills out the form, they can click the **Submit Booking** button.

![Booking Button](documentation/features/booking-button.png)

#### Booking Success Flash Message
Upon Submitting the booking a success flash message will pop up at the top of the page.

![Booking Submit Flash Message](documentation/features/booking-flash.png)


---

### 🔐 Booking Restrictions for Unregistered Users
If a user is **not logged in**, clicking on "Book a Table" **redirects them to the login page**.

---

## Sign Up Form

The **Register Page** contains a **Sign Up form** that allows users to create an account to make bookings and leave reviews on the website.

### Sign Up Form Fields:
- **Email**
- **Username**
- **Password**
- **Confirm Password**

![Sign Up Form](documentation/features/signup-form.png)

Once a user fills out the form, they can **sign up** by clicking the **"Sign Up"** button.

![Sign Up Button](documentation/features/signup-button.png)

If a user decides not to proceed, they can click the **"Cancel"** button, which redirects them to the **Menus/Home page**.

![Cancel Button](documentation/features/cancel-buttom.png)

If a user already has an account, they can click the **"Log In"** link at the top of the form, which will redirect them to the **Log In page**.

![Log In Link](documentation/features/login-redirect.png)

#### Sign Up Success Flash Message
Upon creating an account, you will be redirected to the Menu/Home page with a success flash message at the top of the page. 

![Sign Up Submit Flash Message](documentation/features/signin-flash.png)

---

## Log In Form

The **Log In page** contains a **Log In form** that allows registered users to access their accounts.

### Log In Form Fields:
- **Username or Email**
- **Password**

![Log In Form](documentation/features/login-form.png)

After entering their credentials, users can log in by clicking the **"Log In"** button.

![Log In Button](documentation/features/login-button.png)

If a user has forgotten their password, they can click the **"Forgot Password?"** link to be redirected to the **password reset form**.

![Forgot Password](documentation/features/forgot-password.png)

If a user does not have an account, they can click the **"Register"** link, which redirects them to the **Sign Up form** to create an account.

![Register Link](documentation/features/register-link.png)

---

## Password Reset Form

When a user clicks the forgot password link it takes them to this password reset page with the reset form.

Password Reset Form Fields:
- Email

![Password Reset Form](documentation/features/password-reset.png)

When the user inputs their email they can reset their password by clicking the Reset Password button

![Reset Password Button](documentation/features/reset-password-button.png)

The user can leave the reset password form and go back to the log in page via this link. 

![Register Link](documentation/features/back-login.png)

If a user wants to cancel they can click the cancel button which will redirect them to the hmenu/home page.

![Register Link](documentation/features/cancel-buttonn.png)

---

## Profile Image

When a user creates an account a user profile is also created. The user is able to personalise their profile on the profile page by uploading a display picture.

![Profile](documentation/features/profile-default.png)

A user will be assigned the default image initially. 

![Profile Picture Default](documentation/features/default-pp.png)

The user clicks the choose file button to select an image from their files. The selected file name will then be displayed in the input field beside the button to communicate a file has been selected.

![Profile Image Selection](documentation/features/chose-file.png)

The user then has to click the upload button to upload the profile image. 

![Upload Button](documentation/features/upload-button.png)

The page will refresh and the new image will be displayed in the profile picture.

![New Profile Image](documentation/features/profile-image.png)

A flash success message will also appear at the top of the screen.

![Profile Flash Message](documentation/features/profile-flash.png)

---

## Booking Section

A user is able to manage their bookings on their profile page. The booking section displays all previous bookings in a table display format.

Each row includes the following information:
- Date
- Time 
- Guests
- Status
- Actions

![User Bookings ](documentation/features/user-bookings.png)

To edit the booking the user will click the edit button. 

![Edit Button](documentation/features/edit-button.png)

To delete a booking the user will click the delete button. 

![Delete Button](documentation/features/delete-button.png)

Before a user can delete a booking, a modal will pop up with a final warning to the user of the deletion. The delete button will remove the booking from the users bookings and the database. The cancel button will close the modal.

![Delete Modal](documentation/features/delete-modal.png)

## Edit Booking

When a user clicks to edit a booking on their bookings section in the prpfile page it will open up an edit booking form with all pre-populated data from their selected booking they want to edit. 

![Edit Booking Form](documentation/features/edit-booking.png)

Edit Booking Form Input Fields:
- **Contact Name**
- **Number of Guests (Dropdown)**
- **Booking Date (Date Picker)**
- **Booking Time (Hour & Minute Dropdowns)**
- **Special Requests**
- **Submit Button**

Guest Dropwdown when clicked.

![Edit Booking Form](documentation/features/guest-edit.png)

Date picker when clicked.

![Edit Booking Date Picker](documentation/features/date-picker-edit.png)

Booking Hour Dropdown when clicked.

![Edit Booking Form](documentation/features/time-picker-edit.png)

Booking Minute Dropdown when clicked.

![Minute Dropdown](documentation/features/min-picker-edit.png)

When a user has finished editing their booking they click the Update Booking button.

![Update Booking Button](documentation/features/update-booking.png).

A success flash message will appear at the top of the page to confirm this, and users will be able to see the updated booking in their bookings.

![Edit Success Flash Message](documentation/features/edit-flash.png)
