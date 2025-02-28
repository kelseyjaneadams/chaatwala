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

## Logo 
![Logo](documentation/features/logo.png)