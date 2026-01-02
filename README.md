# Flask Superheroes API

A RESTful API for tracking superheroes and their superpowers built with Flask, SQLAlchemy, and Flask-Mail.

## Author

**Sylvia Malala**

## Description

This API allows you to manage a database of superheroes and their superpowers. You can:
- View all heroes and their associated powers
- View individual hero and power details
- Update power descriptions
- Create associations between heroes and powers
- Send email notifications using Flask-Mail

The application implements a many-to-many relationship between Heroes and Powers through a HeroPower join table, with proper validations and serialization rules to prevent infinite recursion.

## Features

- **RESTful API Design**: Follows REST conventions for all endpoints
- **CRUD Operations**: Full Create, Read, Update operations for managing heroes and powers
- **Data Validation**: 
  - Power descriptions must be at least 20 characters
  - HeroPower strength must be 'Strong', 'Weak', or 'Average'
- **Relationship Management**: Many-to-many relationships with cascade deletes
- **Email Integration**: Flask-Mail configuration for sending notifications
- **Proper Error Handling**: Returns appropriate HTTP status codes and error messages
- **Serialization**: Uses SQLAlchemy-Serializer to prevent infinite recursion
- **Database Migrations**: Flask-Migrate for database version control

## Technologies Used

- **Python 3.x**
- **Flask**: Web framework
- **Flask-SQLAlchemy**: ORM for database operations
- **Flask-Migrate**: Database migration management
- **SQLAlchemy-Serializer**: JSON serialization with relationship handling
- **Flask-Mail**: Email functionality
- **SQLite**: Database (easily replaceable with PostgreSQL, MySQL, etc.)

## Database Schema

### Models

1. **Hero**
   - `id`: Integer (Primary Key)
   - `name`: String (Hero's real name)
   - `super_name`: String (Hero's superhero alias)
   - Relationships: Has many Powers through HeroPower

2. **Power**
   - `id`: Integer (Primary Key)
   - `name`: String (Power name)
   - `description`: String (Must be at least 20 characters)
   - Relationships: Has many Heroes through HeroPower

3. **HeroPower**
   - `id`: Integer (Primary Key)
   - `strength`: String (Must be 'Strong', 'Weak', or 'Average')
   - `hero_id`: Foreign Key to Hero
   - `power_id`: Foreign Key to Power
   - Relationships: Belongs to Hero and Power

### ER Diagram

```
Hero ←→ HeroPower ←→ Power
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd postman_collection
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your email credentials:
   ```
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_app_password
   ```
   
   **Note**: For Gmail, you need to generate an [App Password](https://support.google.com/accounts/answer/185833) instead of using your regular password.

6. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

7. **Seed the database**
   ```bash
   python seed.py
   ```

8. **Run the application**
   ```bash
   python app.py
   ```
   
   The API will be available at `http://localhost:5555`

## API Endpoints

### 1. Get All Heroes
- **URL**: `/heroes`
- **Method**: `GET`
- **Response**: Array of hero objects (id, name, super_name)
- **Status Code**: `200 OK`

**Example Response**:
```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  }
]
```

### 2. Get Hero by ID
- **URL**: `/heroes/:id`
- **Method**: `GET`
- **Response**: Hero object with nested hero_powers
- **Status Codes**: 
  - `200 OK`: Hero found
  - `404 Not Found`: Hero doesn't exist

**Example Response**:
```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "hero_id": 1,
      "id": 1,
      "power": {
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        "id": 2,
        "name": "flight"
      },
      "power_id": 2,
      "strength": "Strong"
    }
  ]
}
```

### 3. Get All Powers
- **URL**: `/powers`
- **Method**: `GET`
- **Response**: Array of power objects
- **Status Code**: `200 OK`

**Example Response**:
```json
[
  {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  }
]
```

### 4. Get Power by ID
- **URL**: `/powers/:id`
- **Method**: `GET`
- **Response**: Power object
- **Status Codes**: 
  - `200 OK`: Power found
  - `404 Not Found`: Power doesn't exist

**Example Response**:
```json
{
  "description": "gives the wielder super-human strengths",
  "id": 1,
  "name": "super strength"
}
```

### 5. Update Power
- **URL**: `/powers/:id`
- **Method**: `PATCH`
- **Request Body**:
  ```json
  {
    "description": "Valid Updated Description (at least 20 characters)"
  }
  ```
- **Status Codes**: 
  - `200 OK`: Update successful
  - `404 Not Found`: Power doesn't exist
  - `400 Bad Request`: Validation failed

**Example Response** (Success):
```json
{
  "description": "Valid Updated Description",
  "id": 1,
  "name": "super strength"
}
```

**Example Response** (Validation Error):
```json
{
  "errors": ["Description must be present and at least 20 characters long"]
}
```

### 6. Create Hero Power
- **URL**: `/hero_powers`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "strength": "Average",
    "power_id": 1,
    "hero_id": 3
  }
  ```
- **Status Codes**: 
  - `201 Created`: HeroPower created successfully
  - `400 Bad Request`: Validation failed

**Example Response** (Success):
```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  }
}
```

**Example Response** (Validation Error):
```json
{
  "errors": ["validation errors"]
}
```

## Testing with Postman

1. Import the provided Postman collection: `challenge-2-superheroes.postman_collection.json`
2. Ensure the API is running on `http://localhost:5555`
3. Run the collection to test all endpoints

## Email Functionality

The application includes Flask-Mail configuration for sending emails. To use this feature:

1. Set up your email credentials in the `.env` file
2. For Gmail users, enable 2-factor authentication and generate an App Password
3. The mail server is configured to use Gmail's SMTP server by default

You can extend the application to send notifications when heroes or powers are created/updated.

## Project Structure

```
postman_collection/
├── app.py                 # Main application file with routes
├── models.py              # Database models
├── seed.py                # Database seeding script
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore file
├── README.md             # This file
└── challenge-2-superheroes.postman_collection.json
```

## Validation Rules

### Power Model
- **description**: Required, minimum 20 characters

### HeroPower Model
- **strength**: Must be one of: 'Strong', 'Weak', 'Average'

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK`: Successful GET/PATCH request
- `201 Created`: Successful POST request
- `400 Bad Request`: Validation error
- `404 Not Found`: Resource not found

Error responses include descriptive messages:
```json
{
  "error": "Hero not found"
}
```

or

```json
{
  "errors": ["validation errors"]
}
```

## Development

To make changes to the database schema:

1. Update the models in `models.py`
2. Create a new migration:
   ```bash
   flask db migrate -m "Description of changes"
   ```
3. Apply the migration:
   ```bash
   flask db upgrade
   ```

## Support

For questions or issues, please contact:
- **Email**: sylviamalala@example.com
- **GitHub**: [@SylviaMalala](https://github.com/SylviaMalala)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Challenge provided by Moringa School
- Built as part of Phase 4 Flask assessment
- Thanks to the Flask and SQLAlchemy communities

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**Note**: This is an educational project for learning Flask, SQLAlchemy, and RESTful API design.