# Project Name: Microservice Template

## Introduction

This is a template for creating microservices in Python. Clone or use this template to kickstart your microservice development.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- `pip` package manager

### Installing

A step-by-step guide to get the development environment running.

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository

2. Install dependencies:

   ```bash 
   pip install -r requirements.txt

3. Setting up Environment Variables:

   Create a .env file in the root directory of the project.

   Add the following environment variables to the `.env` file:
   
   ```bash
   RABBITMQ_USERNAME=your_rabbitmq_username
   RABBITMQ_PASSWORD=your_rabbitmq_password
   RABBITMQ_HOST=your_rabbitmq_host

4. Running the Application from terminal
   ```bash 
   python3 -u -m service.main

   OR

   sh run-service.sh

