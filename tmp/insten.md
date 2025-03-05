# Insten: Shopkeeper Application Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [App Overview](#app-overview)
3. [User Interface Guidelines](#user-interface-guidelines)
4. [Onboarding Process](#onboarding-process)
5. [Dashboard & Overview](#dashboard--overview)
6. [Inventory Management](#inventory-management)
7. [Order Management](#order-management)
8. [Financial Management](#financial-management)
9. [Profile Management](#profile-management)
10. [Settings](#settings)
11. [Order History](#order-history)
12. [Location Services](#location-services)
13. [Product Listing Management](#product-listing-management)
14. [Media Management](#media-management)
15. [Feedback System](#feedback-system)
16. [Insten Companion](#insten-companion)
17. [Filters & Categories](#filters--categories)
18. [Notifications](#notifications)
19. [Analytics](#analytics)
20. [Glossary](#glossary)

## Introduction

Insten is a quick commerce application designed for the Indian market that connects local shopkeepers with customers seeking fast delivery of various products. Similar to platforms like Zepto and Zomato but expanded to serve a wider range of product categories, Insten empowers shopkeepers with tools to manage inventory, process orders, and grow their business digitally.

This documentation provides comprehensive details about the Insten shopkeeper application, outlining all components, functionalities, workflows, and design specifications necessary for the development team to create a feature-rich, user-friendly, and aesthetically pleasing application.

## App Overview

**Platform:** Mobile application (iOS and Android)
**Target Users:** Shopkeepers and small business owners across India
**Primary Functions:**
- Inventory management
- Order processing
- Financial tracking
- Customer engagement
- Product listing and categorization

**Core Value Proposition:** Enabling shopkeepers to digitize their business operations and reach customers beyond their physical store location through a quick commerce delivery model.

## User Interface Guidelines

### Color Theme
- **Primary Color:** Vibrant Orange (#FF6B00)
- **Secondary Color:** Deep Orange (#E65100)
- **Gradient:** Linear gradient from #FF6B00 to #FF9E40
- **Background Color:** Light Orange/White (#FFF5EC)
- **Text Colors:**
  - Primary Text: Dark Gray (#212121)
  - Secondary Text: Medium Gray (#757575)
  - Accent Text: Vibrant Orange (#FF6B00)

### Typography
- **Primary Font:** Poppins
- **Secondary Font:** Roboto
- **Header Sizes:**
  - H1: 24sp, Bold
  - H2: 20sp, Bold
  - H3: 18sp, Medium
  - Body: 16sp, Regular
  - Caption: 14sp, Regular

### Visual Elements
- **Icons:** Outlined style with orange fills for active states
- **Buttons:**
  - Primary: Filled orange with white text
  - Secondary: Orange outline with orange text
  - Tertiary: Text-only in orange
- **Cards:** White background with subtle shadow (elevation: 2dp)
- **Interactive Elements:** Incorporate micro-animations for all touch interactions

### Insten Mascot
- **Character Name:** "Insti" - a small, cute cartoon shopkeeper with an orange outfit
- **Integration Points:** Appears throughout the app to guide users through:
  - Onboarding
  - Empty states
  - Loading screens
  - Achievement moments
  - Tips and suggestions

## Onboarding Process

### Welcome Screens
1. **Splash Screen**
   - Insten logo animation
   - Orange gradient background
   - Brief loading period (2 seconds max)

2. **Introduction Carousel**
   - Screen 1: "Welcome to Insten" with Insti mascot introducing the app
   - Screen 2: "Manage Your Inventory" showing inventory features
   - Screen 3: "Process Orders Quickly" demonstrating order management
   - Screen 4: "Grow Your Business" showcasing analytics features
   - Each screen features vibrant illustrations in orange theme

### Registration Process
1. **Business Information**
   - Fields:
     - Shop Name
     - Shop Category (dropdown with multiple options)
     - GSTIN (optional)
     - Business Address
     - Pincode
     - City
     - State
   - Validation for each field with inline error messages

2. **Personal Information**
   - Fields:
     - Owner Name
     - Mobile Number (OTP verification)
     - Email Address
     - Profile Picture (optional)
   - Privacy policy and terms consent checkbox

3. **Business Hours**
   - Operating days selection (multi-select)
   - Opening time (24-hour format)
   - Closing time (24-hour format)
   - Break hours (optional)

4. **Shop Verification**
   - Upload shop license/registration document
   - Upload shop front photo
   - Upload identity proof
   - Status tracking for verification process

### Initial Setup Wizard
1. **Inventory Quick Start**
   - Add 5 initial products to get started
   - Quick-add templates for common items
   - Bulk import option via CSV

2. **Delivery Settings**
   - Delivery radius selection (1-10 km)
   - Minimum order value setting
   - Delivery fee structure setup

3. **Payment Setup**
   - Bank account details
   - UPI ID configuration
   - Payment gateway integration preferences

4. **Tutorial Walkthrough**
   - Interactive guide with Insti mascot
   - Hotspot highlights for key features
   - Skip option available but not prominently displayed

## Dashboard & Overview

### Main Dashboard
1. **Header Section**
   - Shop status toggle (Open/Closed)
   - Notifications icon with counter
   - Profile quick access
   - Current date and day

2. **Quick Stats Cards**
   - Today's Orders (count)
   - Today's Revenue (amount)
   - Active Orders (count)
   - Pending Payments (amount)
   - Each card with appropriate icon and quick action button

3. **Order Status Breakdown**
   - Circular progress indicators showing:
     - New Orders
     - Processing Orders
     - Out for Delivery
     - Delivered Orders
     - Cancelled Orders

4. **Recent Activity Timeline**
   - Last 5 activities across various functions
   - Timestamp for each activity
   - Quick action buttons where applicable

5. **Inventory Alerts**
   - Low stock items (count and quick access)
   - Out of stock items (count and quick access)
   - Expiring soon items (for perishables)

6. **Business Insights**
   - Daily revenue graph (7-day view)
   - Most sold items (top 3)
   - Peak hours visualization

### Navigation Menu
1. **Bottom Navigation**
   - Dashboard (Home icon)
   - Orders (Package icon)
   - Inventory (Box icon)
   - Finance (Wallet icon)
   - More (Menu icon)

2. **More Menu Options**
   - Profile Management
   - Settings
   - Help & Support
   - Feedback
   - About Insten
   - Logout

## Inventory Management

### Inventory Dashboard
1. **Key Metrics**
   - Total SKUs count
   - Low stock items count
   - Out of stock items count
   - Recently added items

2. **Quick Actions**
   - Add New Item button
   - Bulk Upload button
   - Stock Update button
   - Barcode Scanner access

3. **Category-wise Breakdown**
   - Visual representation of inventory by category
   - Quick filter options
   - Sort capabilities (A-Z, Price, Stock level)

### Product Management
1. **Product List View**
   - Compact list with:
     - Thumbnail image
     - Product name
     - Current stock
     - Price
     - Category
     - Status indicator (In stock/Low stock/Out of stock)
   - Quick action buttons (Edit, Delete, Disable)
   - Pull-to-refresh functionality
   - Infinite scroll with lazy loading

2. **Product Detail View**
   - Image gallery with zoom capability
   - Product information section
   - Pricing history graph
   - Sales history graph
   - Variant management
   - Related products

3. **Add/Edit Product Form**
   - Fields:
     - Product Name
     - Description (rich text editor)
     - Category (multi-level selection)
     - Brand
     - SKU/Product Code
     - Barcode (with scanner integration)
     - MRP
     - Selling Price
     - Discount (percentage or amount)
     - Tax Rate
     - Stock Quantity
     - Unit (kg, g, l, ml, piece, pack, etc.)
     - Minimum Stock Alert Level
     - Product Images (up to 5)
     - Product Videos (optional, up to 2)
     - Specifications (key-value pairs)
     - Tags (for better searchability)
     - Product Visibility toggle
     - Featured Product toggle

4. **Bulk Operations**
   - Import products via CSV/Excel
   - Export product data
   - Bulk price update
   - Bulk stock update
   - Bulk category assignment
   - Bulk enable/disable

### Inventory Analytics
1. **Stock Movement Tracking**
   - Stock intake history
   - Sold quantity tracking
   - Returned/damaged item tracking
   - Stock adjustment logs

2. **Performance Metrics**
   - Fast-moving products
   - Slow-moving products
   - Never sold products
   - Best profit margin products

3. **Predictive Analytics**
   - Stock replenishment suggestions
   - Optimal inventory level recommendations
   - Seasonal trend identification
   - Sales prediction based on historical data

## Order Management

### Live Orders Dashboard
1. **Order Queue**
   - New orders section with notification sound
   - Processing orders section
   - Ready for delivery/pickup section
   - Failed/cancelled orders section

2. **Order Card Components**
   - Order ID and timestamp
   - Customer name and contact
   - Item count and total amount
   - Payment status indicator
   - Delivery type (home delivery/pickup)
   - Estimated delivery time
   - Status update buttons
   - View details button

3. **Order Filters**
   - By status
   - By date range
   - By payment method
   - By delivery method
   - By customer

### Order Processing Workflow
1. **New Order Received**
   - Push notification with sound
   - Order appears in New Orders queue
   - Accept/Reject buttons
   - 30-second countdown for action
   - Automatic assignment if no action taken

2. **Order Acceptance Process**
   - Inventory check confirmation
   - Preparation time estimation
   - Assign to delivery partner option
   - Customer notification trigger

3. **Order Preparation**
   - Itemized checklist
   - Packaging instructions
   - Special requests highlighting
   - Mark ready for delivery button

4. **Delivery Handover**
   - Delivery partner details
   - QR code generation for verification
   - Handover confirmation
   - Tracking initiation

5. **Order Completion**
   - Delivery confirmation
   - Customer rating prompt
   - Thank you message
   - Cross-sell recommendations for next order

### Order Details View
1. **Customer Information**
   - Name, contact number, and address
   - Previous order history link
   - Customer notes
   - Communication buttons (call, message)

2. **Item Details**
   - Itemized list with:
     - Product name and image
     - Quantity
     - Unit price
     - Total price
     - Special instructions per item
     - Substitution preferences

3. **Payment Information**
   - Payment method
   - Payment status
   - Transaction ID
   - Invoice download button
   - Refund/adjustment options

4. **Delivery Information**
   - Delivery address with map
   - Estimated delivery time
   - Delivery instructions
   - Delivery partner details
   - Live tracking link

5. **Order Timeline**
   - Status change history with timestamps
   - Agent/staff notes
   - System-generated events
   - Customer interaction logs

### Order Issue Management
1. **Cancellation Process**
   - Cancellation reason selection
   - Inventory restoration automation
   - Customer notification
   - Refund processing if applicable

2. **Modification Process**
   - Add/remove items
   - Quantity adjustment
   - Price adjustment
   - Customer approval requirement
   - Modified invoice generation

3. **Return and Refund Process**
   - Return reason documentation
   - Product condition assessment
   - Refund amount calculation
   - Refund method selection
   - Return inventory management

## Financial Management

### Financial Dashboard
1. **Key Metrics**
   - Today's revenue
   - This week's revenue
   - This month's revenue
   - Outstanding payments
   - Refunds processed
   - Transaction fees

2. **Revenue Charts**
   - Daily revenue line chart
   - Weekly comparison bar chart
   - Monthly trend analysis
   - Revenue by product category pie chart

3. **Payment Summary**
   - Payment method breakdown
   - Settlement status tracking
   - Pending payouts
   - Failed transactions

### Transaction Management
1. **Transaction List**
   - Comprehensive list with:
     - Transaction ID
     - Order ID reference
     - Amount
     - Payment method
     - Status
     - Timestamp
     - Customer details
   - Advanced filtering capabilities
   - Export functionality

2. **Transaction Details**
   - Complete payment flow timeline
   - Gateway response codes
   - Fee breakdown
   - Related documents
   - Action buttons for issues

3. **Settlement Tracking**
   - Bank account details
   - Settlement schedule
   - Settlement history
   - Pending settlements
   - Failed settlements with resolution steps

### Financial Reports
1. **Daily/Weekly/Monthly Reports**
   - Sales summary
   - Payment method breakdown
   - Tax collection summary
   - Fee deductions
   - Net earnings calculation

2. **Tax Management**
   - GST calculation breakdown
   - Tax collection summary
   - Tax filing assistance
   - Invoice compliance check

3. **Export Options**
   - PDF report generation
   - CSV data export
   - Accounting software integration
   - Custom date range selection

## Profile Management

### Shop Profile
1. **Basic Information**
   - Shop name and logo
   - Shop description
   - Category and subcategories
   - Established date
   - Registration/license numbers

2. **Contact Information**
   - Phone numbers
   - Email addresses
   - Website/social media links
   - Physical address with map
   - Operating hours

3. **Business Identity**
   - GSTIN details
   - PAN details
   - Business registration certificates
   - FSSAI license (for food businesses)
   - Other permits and certifications

4. **Shop Showcase**
   - Shop photos gallery
   - About us story
   - Team members
   - Achievements and badges
   - Customer testimonials

### Owner Profile
1. **Personal Information**
   - Name
   - Profile picture
   - Contact number
   - Email address
   - Role in business

2. **Account Security**
   - Password management
   - Two-factor authentication
   - Login history
   - Device management
   - Security questions

3. **KYC Documentation**
   - Identity proof
   - Address proof
   - PAN card
   - Aadhaar verification status
   - Document expiry tracking

4. **Preferences**
   - Language preference
   - Notification preferences
   - Theme options
   - Data usage settings
   - Accessibility options

## Settings

### Application Settings
1. **General Settings**
   - Language selection
   - Date and time format
   - Currency format
   - Distance unit
   - Weight unit

2. **Notification Settings**
   - New order alerts
   - Low stock alerts
   - Payment alerts
   - Customer message alerts
   - System update alerts
   - Sound settings for each alert type
   - Do not disturb schedule

3. **Display Settings**
   - Theme selection (Light/Dark/System)
   - Text size
   - Brightness control
   - Screen timeout
   - Home screen layout options

4. **Accessibility Settings**
   - Screen reader compatibility
   - Color contrast options
   - Font scaling
   - Gesture controls
   - Voice command options

### Business Settings
1. **Operational Hours**
   - Regular business hours by day
   - Special holiday hours
   - Break time settings
   - Auto-close scheduling
   - Temporary closure management

2. **Delivery Settings**
   - Delivery radius
   - Delivery fee structure
   - Minimum order value

