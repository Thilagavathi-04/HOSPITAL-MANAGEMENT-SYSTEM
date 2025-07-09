# 🏥 Hospital Management System (Python + SQLite)

This is a console-based **Hospital Management System** built using Python and SQLite. It allows **role-based access** for admins, doctors, and staff to manage patients, medicines, prescriptions, and medicine stock efficiently.

## 📌 Features

### ✅ Role-Based Access
- **Admin**
  - Register new users
  - Add new medicines
  - Manage medicine stock
- **Doctor**
  - Add patients
  - Prescribe medicines
- **Staff**
  - View medicine stock

---

### ✅ User Functionalities

| Role   | Functionalities |
|--------|------------------|
| Admin  | Add medicine, Add stock |
| Doctor | Add patient, Add prescription |
| Staff  | View stock |

---

## 🧩 Tech Stack

- **Language**: Python 3
- **Database**: SQLite
- **OOP Concepts**: Inheritance, Abstraction, Encapsulation, Polymorphism
- **Security**: Passwords hashed using SHA-256

---

## 📂 Folder Structure

├── database.py # Creates all required tables
├── main.py # Entry point of the application
├── user.py # User class with login/register logic
├── patient.py # Patient-related OOP logic
├── medicine.py # Medicine class

├── stock.py # Medicine stock management

├── prescriptions.py # Prescription logic

└── hospital.db # SQLite database (generated after running)
