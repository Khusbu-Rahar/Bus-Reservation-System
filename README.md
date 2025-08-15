Bus Reservation System (SQL Version)
Overview

This project is a simple Bus Reservation System made using MySQL.
It allows passengers to book seats and cancel bookings.
The system automatically updates the available seats using SQL Triggers.

Features

Book a seat for a passenger.

Cancel a booking.

Check available seats for each bus.

Automatic seat update after booking or cancellation.

Secure login system for users.

Database Structure

Tables:

routes – Stores bus routes (source, destination, distance).

buses – Stores bus details and available seats.

users – Stores user login details.

bookings – Stores booking details (passenger name, seat number, date).

Keys:

Primary Keys: route_id, bus_id, user_id, booking_id

Foreign Keys:

buses.route_id → routes.route_id

bookings.bus_id → buses.bus_id

bookings.user_id → users.user_id

How It Works

Booking a Seat

Add a new record to the bookings table.

The after_booking_insert trigger decreases available_seats by 1.

Cancelling a Booking

Call the cancel_booking() procedure with the booking ID.

The after_booking_delete trigger increases available_seats by 1.

Demo Commands
-- Booking
INSERT INTO bookings (passenger_name, seat_no, bus_id, user_id, booking_date)
VALUES ('Reet Sharma', 5, 1, 1, CURDATE());

-- Cancel Booking
CALL cancel_booking(1);

-- Check Buses Table
SELECT * FROM buses;

Advantages

Easy to use and maintain.

Automatic seat management.

Real-time updates in the database.

Can be extended for GUI or web interface.
