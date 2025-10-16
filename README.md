[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iX-nLBJ4)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20963308)

# SafeBoda Rwanda - Digitizing Urban Mobility

## Project Description

SafeBoda Rwanda is a web application designed to revolutionize urban mobility by bringing trust, safety, and formalization to the moto-taxi ecosystem in Kigali and beyond. Our platform addresses critical challenges in the informal moto-taxi industry by creating a secure, transparent, and reliable digital marketplace that connects verified drivers with passengers.

### Problems We Solve

**For Passengers:**
- Safety concerns due to unverified driver credentials
- Inconsistent and unpredictable fare negotiations
- Lack of trip tracking and emergency features
- Limited payment options and transparency

**For Drivers:**
- Difficulty establishing credibility and reputation
- Lack of job security and consistent income
- Limited access to financial services and benefits
- No digital trail to demonstrate reliability and performance

### Our Vision

To create East Africa's safest and most reliable digital moto-taxi platform that empowers both riders and drivers through technology, building a community based on trust, safety, and mutual economic growth.

## User Roles

### Rider (Passenger)

**Needs & Expectations:**
- Safe and verified transportation
- Transparent, upfront pricing
- Real-time trip tracking
- Multiple payment options (cash, mobile money, card)
- Emergency safety features
- Reliable driver ratings and reviews
- Quick and easy booking process

### Driver

**Requirements & Motivations:**
- Verified platform to build reputation
- Consistent ride requests and stable income
- Access to financial services and benefits
- Fair commission structure
- Rider ratings and feedback system
- Navigation and route optimization
- Business growth opportunities

## Core Features & User Stories

### Feature 1: User Authentication & Registration

**User Story (Rider):** 
"As a Rider, I want to create an account using my phone number and basic information so that I can access safe and reliable moto-taxi services."

**User Story (Driver):** 
"As a Driver, I want to register with my driver's license, moto registration details, and insurance information so that I can be verified and start accepting rides."

### Feature 2: Ride Request & Booking

**User Story (Rider):** 
"As a Rider, I want to input my pickup and destination locations and see the estimated fare before booking so that I can make informed decisions about my trip."

**User Story (Driver):** 
"As a Driver, I want to receive ride requests with pickup location and fare information so that I can accept rides that match my current location and preferences."

### Feature 3: Real-time Map View

**User Story (Rider):** 
"As a Rider, I want to see my driver's real-time location and estimated time of arrival on a map so that I can track my ride and plan accordingly."

**User Story (Driver):** 
"As a Driver, I want to see the rider's pickup location and optimal route on a map so that I can navigate efficiently to the passenger."

### Feature 4: Trip History

**User Story (Rider):** 
"As a Rider, I want to view my past trips with details like date, route, and fare so that I can track my transportation expenses and history."

**User Story (Driver):** 
"As a Driver, I want to access my trip history and earnings report so that I can monitor my performance and income."

### Feature 5: Driver Ratings & Reviews

**User Story (Rider):** 
"As a Rider, I want to rate and review my driver after each trip so that I can share my experience and help maintain service quality."

**User Story (Driver):** 
"As a Driver, I want to see my average rating and read customer feedback so that I can improve my service and build my reputation."

### Feature 6: Fare Calculation & Payment

**User Story (Rider):** 
"As a Rider, I want multiple payment options including cash, mobile money, and card so that I can choose the most convenient payment method."

**User Story (Driver):** 
"As a Driver, I want transparent fare calculation and secure payment processing so that I receive my earnings reliably."

## Architecture Diagram

```mermaid
graph TB
    subgraph Frontend
        A[React + TypeScript Client]
        B[Vite Build Tool]
    end

    subgraph Backend
        C[Django REST API]
        D[Authentication Service]
        E[Ride Management]
        F[Payment Processing]
    end

    subgraph Database
        G[PostgreSQL]
    end

    subgraph External Services
        H[Map Service]
        I[Payment Gateway]
        J[SMS Service]
    end

    A --> C
    C --> G
    C --> H
    C --> I
    C --> J
    
    style A fill:#61dafb
    style C fill:#0c4b33
    style G fill:#336791
    style H fill:#ff6b6b
    style I fill:#28a745
    
