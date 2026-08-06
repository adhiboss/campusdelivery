Campus Delivery Hub — Full-Stack Build Prompt (for Antigravity)

Paste everything below into Antigravity as your project prompt.

PROJECT OVERVIEW

Build a full-stack web application called "Campus Delivery Hub" — a campus logistics and delivery management platform for Jain University that acts as a middle layer between e-commerce deliveries (Amazon, Flipkart, Swiggy, Zepto) and hostel students.

Core concept: Delivery agents drop parcels at a central campus "Delivery Hub" counter instead of waiting at the gate for students to come down. Students get notified and collect their parcel via QR code / OTP verification. The platform also supports university-negotiated student discounts, a university essentials store, and a peer-to-peer student marketplace.

Three user roles: Student, Delivery Partner, University Admin.

This must be a working, runnable full-stack application — real database persistence, real authentication, real status transitions between roles — not a static mock or a single-file demo.

TECH STACK
Frontend: React + Vite, Tailwind CSS, react-router-dom, recharts (admin charts), lucide-react (icons), qrcode.react (QR generation), axios.
Backend: Node.js + Express, REST API, JWT auth.
Database: PostgreSQL with Prisma ORM. If PostgreSQL is unavailable in this environment, fall back to SQLite with the same Prisma schema so it's a one-line config change later — do not silently switch ORMs.
Real-time updates: Socket.io for pushing notifications/status changes live to connected clients (student sees "parcel arrived" without refreshing).
Package manager: npm (do not mix with yarn/pnpm).
PROJECT STRUCTURE (monorepo)
campus-delivery-hub/
├── backend/
│   ├── prisma/
│   │   ├── schema.prisma
│   │   └── seed.js
│   ├── src/
│   │   ├── routes/
│   │   ├── controllers/
│   │   ├── middleware/
│   │   ├── sockets/
│   │   ├── utils/
│   │   └── server.js
│   ├── .env.example
│   └── package.json
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── student/
│   │   │   ├── delivery-partner/
│   │   │   └── admin/
│   │   ├── components/
│   │   ├── context/        (auth context, socket context)
│   │   ├── api/            (axios instance + endpoint functions)
│   │   └── App.jsx
│   ├── .env.example
│   └── package.json
├── package.json            (root, with concurrently script)
└── README.md
DATABASE SCHEMA (Prisma models)

Implement these entities with sensible field types, relations, and enums:

User — id, name, email (unique), password_hash, role (enum: STUDENT, DELIVERY_PARTNER, ADMIN), phone, created_at
Student — id, user_id (FK, 1:1), usn (unique), hostel_block, room_no
DeliveryPartner — id, user_id (FK, 1:1), vehicle_no, company
Order — id, student_id (FK), vendor_name, product_name, external_order_id, status (enum: ORDERED, SHIPPED, OUT_FOR_DELIVERY, ARRIVED_AT_CAMPUS, READY_FOR_PICKUP, COLLECTED, CANCELLED), order_date, expected_date
PickupCounter — id, name, location
Parcel — id, order_id (FK, 1:1), tracking_id, pickup_counter_id (FK), arrival_time, otp_code, qr_payload, status
Pickup — id, parcel_id (FK), pickup_time, otp_used (bool), status
Discount — id, brand_name, title, description, discount_type, start_date, end_date, active (bool)
Transaction — id, user_id (FK), discount_id (FK, nullable), amount, payment_method, status, created_at
MarketplaceItem — id, seller_id (FK → User), category, title, description, price, status (enum: AVAILABLE, SOLD)
Notification — id, user_id (FK), message, type, read_status (bool), created_at

Add appropriate indexes on foreign keys and unique constraints (email, usn, external_order_id).

BACKEND API ENDPOINTS

Implement full REST endpoints with validation and role-guard middleware:

Auth

POST /api/auth/register — role-aware registration (student needs usn/hostel/room; delivery partner needs vehicle/company)
POST /api/auth/login — returns JWT
GET /api/auth/me — current user from token

Orders

POST /api/orders — student creates/simulates a placed order
GET /api/orders?studentId= — list with filters (status, vendor)
PATCH /api/orders/:id/status — update status (simulates vendor progression)

Parcels

POST /api/parcels/arrive — delivery-partner-only; marks arrival at hub, auto-generates OTP + QR payload, creates a notification for the student, emits a socket event to that student
POST /api/parcels/:id/collect — validates OTP or QR payload, marks collected, updates linked order status

Discounts

GET /api/discounts
POST /api/discounts/:id/claim

University Store

GET /api/store/items
POST /api/store/order

Marketplace

GET /api/marketplace?category=
POST /api/marketplace
POST /api/marketplace/:id/message (mock — just logs/stores a message record)

Notifications

GET /api/notifications?userId=
PATCH /api/notifications/:id/read

Admin

GET /api/admin/stats — today's deliveries by vendor, parcels currently in hub, collected count, pending count, computed peak delivery hour

Seed the database (prisma/seed.js) with: 5+ students, 3 delivery partners, 1 admin, 10+ orders across different statuses/vendors, 6 discounts, 6 marketplace listings, 6 university store items, a spread of notifications.

FRONTEND REQUIREMENTS

Three role-based experiences, all wired to the real backend (no mock/hardcoded data once connected — everything comes from API calls):

Student view — Dashboard (stat cards, recent activity, order trackers, discount cards), My Orders (filterable, status stepper), Pickup Center (live QR + OTP), Discounts, University Store, Marketplace, Notifications, Profile.
Delivery Partner view — list of assigned/pending drops, "Mark Arrived at Hub" action.
Admin view — live stats from /api/admin/stats, delivery volume chart (recharts), peak time callout, vendor leaderboard.

Design: left sidebar nav, top bar with search + notification bell, card-based layout, Jain University maroon/red (
#8B1E2F) as primary accent, blue for secondary buttons, white/light-gray background, fully responsive.

RULES THE AGENT MUST FOLLOW
Process rules
Build in stages, verify at each stage before moving on: Stage 1 — backend scaffold + Prisma schema + migrations run successfully. Stage 2 — seed script runs and populates the DB correctly (print a summary of rows created). Stage 3 — all API endpoints implemented and manually testable (e.g. via a curl/README snippet). Stage 4 — frontend scaffold + auth flow wired to backend. Stage 5 — role-based pages wired one at a time (student → delivery partner → admin). Do not move to the next stage until the current one runs without errors.
After each stage, run the relevant server/build command and confirm it starts without errors before proceeding. If something fails, fix it before continuing — don't layer more code on top of a broken stage.
Do not silently invent scope. If a requirement is ambiguous (e.g. exact OTP expiry time), make a reasonable assumption, implement it, and note the assumption in the README rather than asking mid-build.
Code quality rules
Use async/await, not callback chains, throughout the backend.
All backend routes must have try/catch error handling and return consistent JSON error shapes: { error: string, details?: any }.
Passwords must be hashed with bcrypt — never stored or returned in plaintext, and never included in any API response.
JWT secret and DB connection string must be read from environment variables (.env), never hardcoded. Provide .env.example files with placeholder values in both backend/ and frontend/.
Use role-guard middleware on the backend for any endpoint restricted to a specific role (e.g. only DELIVERY_PARTNER can hit /api/parcels/arrive; only ADMIN can hit /api/admin/stats). Do not rely on frontend-only role checks for security.
Validate request bodies on the backend (e.g. with a lightweight validator or manual checks) — reject malformed requests with a 400, not a 500.
Frontend components should be functional components with hooks, no class components. Keep components under roughly 200 lines; extract reusable pieces (StatCard, OrderStatusStepper, DiscountCard, etc.) into components/.
No mock/dummy data left inside frontend components once wired to the real backend — all data must come through the api/ layer.
Consistent naming: camelCase for JS variables/functions, PascalCase for React components, snake_case for database columns (Prisma will map this).
Data & security rules
OTP codes should be numeric, 6 digits, and single-use (mark otp_used = true after a successful collection).
QR payloads should encode enough info to look up the parcel (e.g. a signed token or the parcel's tracking_id) — do not put raw sensitive data like passwords or full user records in a QR payload.
Every state-changing action (claim discount, mark collected, place order) must persist to the database — nothing should live only in frontend state after a page refresh.
Notifications must actually be created server-side when relevant events happen (parcel arrives, offer claimed, order status changes) — not faked on the frontend.
Deliverable rules
Include a README.md at the project root with: prerequisites, setup steps (install deps, configure .env, run migrations, run seed script), how to start both servers (ideally one root command via concurrently), and a table of default login credentials for one seeded user per role (student / delivery partner / admin) so it can be demoed immediately.
Include a root package.json with a script (e.g. npm run dev) that starts backend and frontend together using concurrently.
The final app must be demo-ready in one command after setup: seed data should already tell a coherent story (a student with orders in various stages, at least one parcel already sitting in "ready for pickup" with a valid OTP/QR, at least one delivery partner with a pending drop, admin stats reflecting the seeded orders).
FINAL CHECK BEFORE CALLING IT DONE

Before finishing, the agent should confirm:

 npm run dev from root starts both backend and frontend without errors
 Registering and logging in works for all 3 roles
 A delivery partner marking a parcel "arrived" generates a real OTP/QR and creates a notification the student can see
 A student can collect a parcel using that OTP/QR and its status updates to COLLECTED everywhere (student view, admin stats)
 Admin dashboard numbers reflect actual seeded/created data, not static placeholders
 README setup instructions work if followed from a clean clone
