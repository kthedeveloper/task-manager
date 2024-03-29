# task-manager

task-manager is a Django-based web application designed to facilitate project and task management. It enables users to create projects, assign tasks to users, and track the progress of these tasks. With a built-in notification system, task-manager ensures that all team members stay informed about task assignments and updates.

## Features

- **Project Management**: Create and manage projects with descriptions, start and end dates.
- **Task Management**: Add tasks to projects, assign them to users, and track their status (New, In Progress, Completed).
- **User Roles**: Support for different roles within the project, including project managers and team members, with role-based access control.
- **Notifications**: Automated notifications for new task assignments and status updates via email.
- **RESTful API**: A comprehensive API for managing projects, tasks, and users.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Django 3.2 or higher
- Django Rest Framework
- Celery
- Redis

## Usage
After starting the development server, you can access the TaskManager web application at http://localhost:8000/.

Use the following endpoints to interact with the API:

* /api/projects/ - Manage projects
* /api/tasks/ - Manage tasks within projects
* /api/register/ - User registration
