# Requirements - Campus Delivery Hub

## 1. Functional Requirements

### Authentication & Authorization
- **Roles:** STUDENT, DELIVERY_PARTNER, UNIVERSITY_ADMIN.
- Secure login and registration using JWT (Access & Refresh tokens).
- Passwords must be hashed using bcrypt/Argon2.
- Backend must enforce role-based access control (RBAC).

### Deliveries & Packages
- Students can view and track their deliveries.
- Delivery Partners can view assigned deliveries, update status, and drop packages at the hub.
- Packages follow a strict state machine: `CREATED -> ASSIGNED -> IN_TRANSIT -> ARRIVED_AT_HUB -> READY_FOR_PICKUP -> VERIFICATION_PENDING -> PICKED_UP -> COMPLETED`.
- QR/OTP verification must happen server-side when a student picks up a package.

### Notifications (Real-Time)
- Users receive real-time notifications via WebSocket/Socket.IO.
- Notifications trigger on key delivery status changes (e.g., ARRIVED_AT_HUB, READY_FOR_PICKUP).
- Read/Unread status tracking.

### Additional Modules
- **Marketplace:** Peer-to-peer student marketplace to buy/sell items.
- **University Store:** Purchase college merchandise, stationery, etc.
- **Discounts:** Browse and claim student-exclusive discounts.
- **Admin Dashboard:** Monitor deliveries, users, and overall analytics.

## 2. Non-Functional Requirements
- **Security:** Protection against SQLi, XSS, CSRF. Passwords never returned.
- **Validation:** Pydantic on the backend, TypeScript/Form validation on frontend.
- **Performance:** Pagination for lists. Fast API response times.
- **Architecture:** Monorepo, Dockerized, easy local setup.

## 3. Assumptions
- Students must belong to a specific hostel and room.
- QR codes encode an internal delivery ID or secure token, not sensitive data.
- E-commerce order syncing is simulated manually by students or admins in this iteration.

## 4. Risks
- Managing WebSocket connection drops and reconnects reliably.
- Ensuring secure OTP generation and expiry without race conditions.
