# Elevator Management System

The Elevator Management System is a Django project designed to manage the operations of an elevator system. It provides APIs for initializing the elevators, handling user requests, and managing elevator status.

## Features

- Ability to move elevators up and down
- Opening and closing doors
- Starting and stopping elevators
- Displaying current status
- Assigning elevators to floors based on requests
- Marking elevators as available, busy, or under maintenance

## Installation

1. Clone the repository: `git clone https://github.com/your-username/elevator-management-system.git`
2. Change to the project directory: `cd elevator-management-system`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py migrate`

## Usage

1. Start the development server: `python manage.py runserver`
2. Access the API endpoints:
   - Initialize the elevator system: `POST /api/elevators/initialize/`
   - Fetch requests for a given elevator: `GET /api/elevators/{elevator_id}/requests/`
   - Fetch the next destination floor for a given elevator: `GET /api/elevators/{elevator_id}/next-destination/`
   - Fetch if the elevator is moving up or down currently: `GET /api/elevators/{elevator_id}/is-moving/`
   - Save a user request: `POST /api/requests/`
   - Mark an elevator as not working or in maintenance: `PUT /api/elevators/{elevator_id}/maintenance/`
   - Open or close the elevator door: `PUT /api/elevators/{elevator_id}/door/`

For more detailed API documentation and examples, refer to the [API documentation](api.md) file.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
