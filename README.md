# 3DCouponTnCs
Terms and Conditions of 3D Print Coupons

# Terms and Conditions for 3D Printing Coupons

## 1. Purpose
Each coupon entitles the holder to request a single 3D printing project from Bear.

## 2. Limitations
- Only one coupon will be provided per person.
- The project must use no more than one kilogram of filament.
- One Coupon per project.

## 3. Exchange Policy
- Coupons can be exchanged or gifted to other family members.

## 4. Scheduling
- Coupon holders must schedule their project request at least two weeks in advance.
- Scheduling will be done via a Microsoft Form[(https://forms.office.com/r/BVrCDAT8cm?origin=lprLink)].

## 5. Project Commitment
- Once a project is initiated using the coupon, no significant changes can be made to the project. The coupon will be forfeited, and the project will be considered in progress.

## 6. Agreement
By using the coupon, the holder agrees to these terms, ensuring a smooth process and allowing adequate time for project completion.

## Article API

This repository includes a small FastAPI application providing two routes:

- `GET /api/articles` – return recent articles with optional `category`, `date` and `urgency` query parameters for filtering.
- `POST /api/articles` – add a new article which will be broadcast to connected WebSocket clients.
- `WS /ws/articles` – receive newly posted articles in real time.

To run the server locally:

```bash
pip install -r requirements.txt
python main.py
```
