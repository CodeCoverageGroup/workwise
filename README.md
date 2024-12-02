# Workwise

Workwise is a system designed to streamline workforce management, automate machine maintenance, and improve departmental collaboration. The project utilizes a React.js frontend and Django backend, adhering to industry-standard principles and patterns for scalability, security, and maintainability.

## Table of Contents

- [Overview](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)
- [Features](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)
- [Architecture](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)
- [Installation](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)
- [Usage](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)
- [API Documentation](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)
- [Design Principles](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)
- [Project Plan](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)
- [License](https://www.notion.so/Workwise-14b9487cfd3d808a86bae20bc937db52?pvs=21)

---

## Overview

Workwise integrates the following core functionalities:

- **Workforce Management**: Efficient employee scheduling and communication.
- **Machine Maintenance**: Automated ticketing for issue tracking and resolution.
- **Job Scheduling**: Automated scheduling based on deadlines and priorities.
- **Departmental Collaboration**: Tools for managing tasks across departments.
- **Secure Access**: Role-based access with JWT authentication.

---

## Features

1. **Authentication**: Secure login, registration, and token-based authentication.
2. **User Management**: Add, update, and remove users with role-based permissions.
3. **Machine Management**: Maintain a list of machines and manage maintenance tickets.
4. **Job Scheduling**: Prioritize and assign tasks dynamically.
5. **Notifications**: Send and manage alerts for events and updates.
6. **Departmental Management**: Organize and manage departmental information.
7. **Admin Panel**: Manage application data with Django's built-in admin interface.

---

## Architecture

- **Frontend**: **React.js** with Context API for state management and modular components for reusability.
- **Backend**: **Django REST Framework** with PostgreSQL for robust API handling.
- **API Integration**: Centralized logic in `frontend2/src/services/api.js` for seamless communication between frontend and backend.

---

## Installation

### Prerequisites

- **Node.js**
- **React.js**
- **Python 3.x**
- **PostgreSQL**
- **Git**

### Setup Instructions

1. Clone the repository:
    
    ```bash
    git clone https://github.com/your-username/workwise.git
    cd workwise
    ```
    
2. Install dependencies:
- **Frontend**:
    
    ```bash
    cd /workwise-01/frontend2
    npm install
    ```
    
- **Backend**:
    
    ```bash
    cd /workwise-01/backend
    pip install -r requirements.txt
    ```
    
1. Configure the database:
    - Update database settings in `backend/settings.py`.
2. Apply migrations:
    
    ```bash
    python manage.py migrate
    ```
    
3. Start the servers:
- Backend:
    
    ```bash
    cd /workwise-01/backend
    python manage.py runserver
    ```
    
- Frontend:
    
    ```bash
    cd /workwise-01/frontend2
    npm start
    ```
    

---

## Usage

1. Access the frontend at `http://localhost:3000`
2. Use the (backend) API at `http://localhost:8000/api/`

---

## API Documentation

### **Authentication**

- **`POST /api/auth/token/`** - Obtain a JWT token.
- **`POST /api/auth/token/refresh/**` - Refresh an expired JWT token.
- **`POST /api/auth/register/**` - Register a new user.

---

### **User Management**

- **`GET /api/auth/users/**` - Retrieve a list of all users.
- **`GET /api/auth/users/<id>/**` - Retrieve details of a specific user.
- **`PATCH /api/auth/users/<id>/`** - Update specific details of a user.
- **`DELETE /api/auth/users/<id>/`** - Delete a specific user.

---

### **Department Management**

- **`GET /api/departments/departments/`** - Retrieve a list of all departments.
- **`POST /api/departments/departments/`** - Create a new department.
- **`GET /api/departments/departments/<id>/`** - Retrieve details of a specific department.
- **`PATCH /api/departments/departments/<id>/**` - Update a specific department.
- **`DELETE /api/departments/departments/<id>/`** - Soft delete a department.
- **`GET /api/departments/departments/count/**` - Retrieve the total count of departments.

---

### **Job Management**

- **`GET /api/jobs/jobs/**` - Retrieve a list of all jobs.
- **`GET /api/jobs/jobs/<id>/**` - Retrieve details of a specific job.

---

### **Machine Management**

- **`GET /api/machines/machines/`** - Retrieve a list of all machines.
- **`POST /api/machines/machines/**` - Add a new machine.
- **`GET /api/machines/machines/<id>/`** - Retrieve details of a specific machine.
- **`PATCH /api/machines/machines/<id>/`** - Update machine details.
- **`DELETE /api/machines/machines/<id>/**` - Remove a machine.
- **`GET /api/machines/machines/maintenance_due/`** - List machines with upcoming maintenance needs.

---

### **Maintenance Tickets**

- **`GET /api/machines/tickets/`** - Retrieve a list of all maintenance tickets.
- **`POST /api/machines/tickets/`** - Create a new maintenance ticket.
- **`GET /api/machines/tickets/open_tickets/`** - Retrieve a list of open tickets.

---

### **Notifications**

- **`GET /api/notifications/notifications/**` - Retrieve a list of all notifications.
- **`PATCH /api/notifications/notifications/<id>/mark-read/**` - Mark a notification as read.
- **`PATCH /api/notifications/notifications/<id>/mark-unread/**` - Mark a notification as unread.
- **`DELETE /api/notifications/notifications/delete-all/**` - Delete all notifications.

---

### **Admin Panel**

- **`GET /admin/**` - Access the Django admin interface.
- **`GET /admin/<app_name>/<model_name>/**` - Access a specific model's data.

---

## Design Principles

### Frontend

1. **Separation of Concerns**
    - Each module is designed to handle a single responsibility, making the codebase easier to maintain and test.
    - Example:
        - **API Interaction**: Centralized in src/services/api.js to decouple backend communication from UI logic.
    - **Layouts**: Components like dashboard and authentication handle only the structural and layout aspects of the application, with no logic coupling.
2. **Reusable Components**
    - Modular and reusable components reduce code duplication and improve maintainability.
    - Example:
        - **DashboardNavbar**: A reusable navigation bar used across various dashboard views.
        - **OrderOverview**: A widget for displaying dynamic order summaries.
3. **Consistency**
    - Uniform design patterns and coding conventions across the frontend improve readability and reduce onboarding time for developers.
    - Example:
        - Theming: All styles are centralized in src/assets/theme, ensuring consistent design across the application.
        - API Calls: Consistent methods (get, post, put, delete) in src/services/api.js provide predictable and manageable API interactions.

**4. State Management**

- The application uses the React Context API for managing global states like user authentication and theme preferences, ensuring a clean separation between state and UI.
- Example:
    - Authentication Context: Manages user login state and provides role-based rendering.
1. **References**
    - [React Documentation: Context API](https://reactjs.org/docs/context.html)
    - [Frontend Best Practices](https://frontendchecklist.io/)

### Backend

1.  **Design Principles**
    1. **Single Responsibility Principle (SRP)**: Each app handles a specific task (e.g., Accounts, Machines).
        - **Accounts App**: Handles user authentication and registration.
        - **Machines App**: Manages machine data and maintenance tickets.
    2. **Open/Closed Principle (OCP)**
        - Classes and modules are open for extension but closed for modification.
        - Example:
            - Abstract Base Classes: Common logic (e.g., created_at, updated_at fields) is defined in abstract base models, which can be extended by other models without altering the base implementation.
    3. **Dependency Inversion Principle (DIP)**
        - High-level modules depend on abstractions, not concrete implementations.
        - Example:
            - Django serializers define how models interact with APIs, abstracting away database dependencies from views.
    4. **Don’t Repeat Yourself (DRY)**
        - Repeated logic is abstracted into shared utilities or services.
        - Example:
            - A utility function for sending notifications (utils/notification_service.py) is shared across multiple apps (Jobs, Machines, Departments).
    5. **Separation of Concerns (SoC)**
        - The backend architecture is divided into distinct layers:
        - **Models**: Represent database schemas.
        - **Views**: Handle business logic and API interactions.
        - **Serializers**: Convert models to JSON and validate incoming data.
        - **Tests**: Validate each layer independently for better reliability.
2. **Design Patterns**:
    - **Factory Pattern**: Dynamic object creation (e.g., user roles).
    - **Observer Pattern**: Notifications on system events.

---

## Project Plan

### Milestones

1. **Planning & Design**: Architecture and requirements gathering.
2. **Frontend Development**: Component and state management.
3. **Backend Development**: API and database implementation.
4. **Integration & Testing**: Validation and deployment.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.