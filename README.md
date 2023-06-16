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

## Installation


[![Python Version](https://img.shields.io/badge/python-3.8.1-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0.6-brightgreen.svg)](https://djangoproject.com)


* First, clone the repository to your local machine:

```bash
https://github.com/samirpatil2000/ElevatorManagementSystem.git
```
* Create & Activate Virtual Environment For Windows

```bash
>> virtualenv env
>> .\env\Scripts\activate
```

* Create & Activate Virtual Environment For MacOs/Linux

```bash
>> virtualenv env
>> . env/bin/activate
```


* Install the requirements:

```bash
>> pip install -r requirements.txt
```

* Create Database Tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

* Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
   
### SEQUENCE DIAGRAM
![Screenshot 2023-06-16 at 6 51 12 PM](https://github.com/samirpatil2000/ElevatorManagementSystem/assets/55244065/b152309a-e8fa-47e9-b0f4-9b15572b9a73)

### DataBase Schema

![Screenshot 2023-06-16 at 6 58 47 PM](https://github.com/samirpatil2000/ElevatorManagementSystem/assets/55244065/22912203-d544-42d3-bd08-57e8f202f576)

## API Endpoints

<table>
  <tr>
    <th>Method</th>
    <th>Endpoint</th>
    <th>Description</th>
    <th>Request Body</th>
    <th>Response Body</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>/elevators-api/initialise-system/</td>
    <td>Initialize the elevator system</td>
    <td><pre>{ 
    "elevators": "2" 
}</pre></td>
    <td><pre>{
    "message": "Elevators Created Successfully"
}</pre></td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/elevators-api/elevators/{elevator_id}</td>
    <td>Fetch requests for a given elevator and all other information regarding it</td>
<td>NA</td>      
<td>
      <pre>{
    "id": 6,
    "requests": [
        {
            "pk": 20,
            "floor": 1,
            "timestamp": "2023-06-15T17:25:33.039755Z",
            "is_completed": true
        },
        {
            "pk": 21,
            "floor": 1,
            "timestamp": "2023-06-15T17:27:06.195018Z",
            "is_completed": true
        }
    ],
    "status": "operational",
    "current_floor": 6,
    "direction": "UP",
    "timestamp": "2023-06-15T14:32:29.685211Z",
    "is_door_opened": true
}</pre></td>
    
  </tr>
<tr>
    <td>GET</td>
    <td>/elevators-api/elevators/</td>
    <td>Fetch all the elevators </td>
<td>NA</td>      
<td>
      <pre>[
    {
        "id": 6,
        "requests": [
            {
                "pk": 20,
                "floor": 1,
                "timestamp": "2023-06-15T17:25:33.039755Z",
                "is_completed": true
            },
            {
                "pk": 21,
                "floor": 1,
                "timestamp": "2023-06-15T17:27:06.195018Z",
                "is_completed": true
            }
        ],
        "status": "operational",
        "current_floor": 6,
        "direction": "UP",
        "timestamp": "2023-06-15T14:32:29.685211Z",
        "is_door_opened": true
    },
]</pre></td>
    
  </tr>
  <tr>
    <td>PUT</td>
    <td>/elevators-api/elevators/{elevator_id}</td>
    <td>Update properties of elevator</td>
    <td><pre>{
    "is_door_opened": false,
    "direction": "DOWN",
    "status": "operational"
}</pre></td>
    <td><pre>
{
    "id": 6,
    "requests": [
        {
            "pk": 20,
            "floor": 1,
            "timestamp": "2023-06-15T17:25:33.039755Z",
            "is_completed": true
        },
        {
            "pk": 21,
            "floor": 1,
            "timestamp": "2023-06-15T17:27:06.195018Z",
            "is_completed": true
        }
    ],
    "status": "operational",
    "current_floor": 6,
    "direction": "DOWN",
    "timestamp": "2023-06-15T14:32:29.685211Z",
    "is_door_opened": false
}</pre></td>
  </tr>

  <tr>
    <td>POST</td>
    <td>/elevators-api/requests/</td>
    <td>Create Request for elevator</td>
    <td><pre>{
    "floor": "1"
}</pre></td>
    <td><pre>{
    "message": "Requested for elevator successfully Elevator 7 is on the way"
}</pre></td>
  </tr>
  <tr>
    <td>POST</td>
    <td>destination-request/{elevator_id}</td>
    <td>Request for elevator</td>
    <td><pre>{
    "floor": "1"
}</pre></td>
    <td><pre>
{
    "message": "Elevator 6 Reach To destination floor 2"
}</pre></td>
  </tr>
</table>


## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
