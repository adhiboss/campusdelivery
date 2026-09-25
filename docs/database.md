# Database Design - Campus Delivery Hub

## Overview
The database is PostgreSQL, accessed via SQLAlchemy ORM. Migrations are managed by Alembic.

## Core Entities

### `users`
- `id` (UUID, PK)
- `email` (String, Unique)
- `password_hash` (String)
- `role` (Enum: STUDENT, DELIVERY_PARTNER, UNIVERSITY_ADMIN)
- `phone` (String)
- `created_at` (Timestamp)

### `students`
- `id` (UUID, PK)
- `user_id` (UUID, FK -> users.id, Unique)
- `usn` (String, Unique)
- `hostel_block` (String)
- `room_no` (String)

### `delivery_partners`
- `id` (UUID, PK)
- `user_id` (UUID, FK -> users.id, Unique)
- `company` (String)
- `vehicle_no` (String)

### `pickup_counters`
- `id` (UUID, PK)
- `name` (String)
- `location` (String)

### `deliveries`
(Combines Order and Parcel concepts into a unified state machine)
- `id` (UUID, PK)
- `student_id` (UUID, FK -> students.id)
- `delivery_partner_id` (UUID, FK -> delivery_partners.id, Nullable)
- `vendor_name` (String)
- `product_name` (String)
- `tracking_id` (String, Unique)
- `pickup_counter_id` (UUID, FK -> pickup_counters.id, Nullable)
- `status` (Enum: CREATED, ASSIGNED, IN_TRANSIT, ARRIVED_AT_HUB, READY_FOR_PICKUP, VERIFICATION_PENDING, PICKED_UP, COMPLETED)
- `otp_code` (String, Nullable)
- `qr_payload` (String, Nullable)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

### `notifications`
- `id` (UUID, PK)
- `user_id` (UUID, FK -> users.id)
- `message` (String)
- `type` (String)
- `is_read` (Boolean)
- `created_at` (Timestamp)

### `marketplace_listings`
- `id` (UUID, PK)
- `seller_id` (UUID, FK -> students.id)
- `title` (String)
- `description` (Text)
- `price` (Decimal)
- `status` (Enum: AVAILABLE, SOLD)

## Indexes and Constraints
- Foreign keys must cascade on delete where appropriate (e.g., deleting a User deletes the Student record).
- Indexes on `email`, `usn`, `tracking_id` for fast lookups.
- Delivery status transitions will be enforced in the Service layer, but Enum types constrain invalid raw strings in the DB.
