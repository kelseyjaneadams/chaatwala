# Chaatwala

## Features

Web application has the following pages:

- Menu/Home Page
- Booking A Table Page
- Log In Page
- Register Page
- Profile Page
- Log Out Page

## 🔑 User & Admin Access Levels for Chaatwala App

### 👥 User Roles & Access Permissions

| Feature | **Regular User** | **Admin** |
|---------|:--------------:|:------:|
| **Authentication & Account Management** | ✅ Can Sign Up, Log In, Log Out | ✅ Full control over all user accounts |
| **Password Reset** | ✅ Can reset own password | ✅ Can reset any user’s password |
| **Profile Management** | ✅ Can update profile picture & view own bookings & reviews | ✅ Can update any user’s profile if needed |
| **Booking System** | ✅ Can create, edit, & cancel own bookings | ✅ Can view, edit, and delete **all** bookings |
| **Booking Status** | ✅ Can see their booking status (Pending, Confirmed, Cancelled) | ✅ Can **change** any booking status |
| **Viewing Restaurant Menus** | ✅ Can view/download menus | ✅ Can update menus (e.g., add new items) |
| **Review System** | ✅ Can submit, edit, and delete their own reviews | ✅ Can **approve/reject/delete** any review |
| **Review Approval Process** | ❌ Cannot approve reviews (must wait for admin) | ✅ Can approve or reject pending reviews |
| **Viewing Other Users' Reviews** | ✅ Can only see **approved** reviews | ✅ Can see **all reviews** (approved & pending) |
| **Deleting Content** | ❌ Cannot delete other users' reviews or bookings | ✅ Can delete **any** review, booking, or user profile |
| **Admin Dashboard Access** | ❌ No access | ✅ Full access to the Django admin panel |
| **Site Settings & Management** | ❌ No access | ✅ Can update menus, change business hours, and manage users |

---


## Navbar

### Logged Out User
![Navbar](documentation/features/navbar-unlogged.png)
### Logged In User
![Navbar](documentation/features/navbar-logged.png)

Navbar has the following links:
- Menus Page
- Booking a Table Page
- Register Page
- Log In Page

When a user signs up/logs in then the following pages appear on the Navbar:
- Menus Page
- Booking a Table Page
- Profile Page
- Log Out Page

The Navbar has a logo of the Restauraunt.

The Navabar also turns into a Burger on smaller screens. 

![Navbar](documentation/features/navbar-burger.png)



The design of the Navbar is kept simple so the User can easily navigate their way through the website.

## Logo 
![Logo](documentation/features/logo.png)

This logo when clicked redirects to the Home/Menu Page.

## Footer
![Footer](documentation/features/footer.png)

The Footer has 5 Social Media links which take the User to the relevant Social Media page in a new tab once clicked.

## Hero Image
![Hero](documentation/features/hero-image.png)

The Hero image displays the inside of the restuaraunt to the User so they can get a feel for the aesthetic.

## Menu Title 
![MenuTitle](documentation/features/menu-title.png)

The Menu title communicates to the User the beginning of the Menu section.

## Menus 
![Menus](documentation/features/menu-choices.png)

There are 4 Menu Options:
- Food Menu
- Drinks Menu
- Kids Menu
- Sweet Menu

On Mobile screens the Menu Choices are displayed in two rows.

![Menus](documentation/features/menus-mobile.png)

The Menu choices, once clicked, open the Menu images in a new tab so the User can review the food and drink options.

#### Food Menu
![Menus](documentation/features/food-menu.png)

#### Drinks Menu
![Menus](documentation/features/drinks-menu.png)

#### Kids Menu
![Menus](documentation/features/kids-menu.png)

#### Sweet Menu
![Menus](documentation/features/sweet-menu.png)

## Reviews 
The Reviews section sits underneath the Menus section so User's can see honest feedback from previous customers.

 For a User who has not registered or logged in the section will show approved reviews in a scrollable list.

![Menus](documentation/features/reviews-unlogged.png)

For a User to leave a review they must be signed in. The log in button redirects the User to the log in page, if it is a new User they will have the option to register via this log in page.

![Menus](documentation/features/reviews-button-unlogged.png)


For a registered/logged in User, the review section will appear slightly different.

The User will be able to see all of their own pending reviews if they have made any. The pending reviews will be greyed out with a message to communicate this.

![Menus](documentation/features/review-pending.png)

The review form will appear undereneath this, giving the User the ability to create a review.

The form will have the following:
- Review Rating Dropdown Menu
- Comment Field
- Submit Button

![Menus](documentation/features/reviews-form.png)

![Menus](documentation/features/rating-dropdown.png)

![Menus](documentation/features/review-button.png)
