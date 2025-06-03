# TomeVault

**TomeVault** is a web-based Library Management System designed to streamline library operations for administrators, librarians, and students. Built using Python (Flask), JavaScript, and HTML, it offers a user-friendly interface for managing books, users, and transactions.

## Features

### Admin

* **Authentication**: Secure login system for administrators.
* **User Management**: View and edit librarian and student details.

### Librarian

* **Authentication**: Secure login system for librarians.
* **Profile Management**: Edit personal details.
* **Book Management**: Search for books, issue books to students, and update book statuses.

### Student

* **Authentication**: Secure login system for students.
* **Profile Management**: Edit personal details and view profile information.
* **Penalty Calculation**: Calculate penalties for overdue books.

## Technologies Used

* **Backend**: Python 3 with Flask framework
* **Frontend**: HTML, CSS (to be added), JavaScript
* **Database**: MySQL

## Directory structure
```
TomeVault/
├── client/           # Client side interface
├── server/           # Server side logic
├── .gitignore        # Git ignore file
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/PALLADIUM26/TomeVault.git
   cd TomeVault
   ```



2. **Set up a virtual environment** (optional):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```



4. **Configure the database**:

   * Set up your database and update the configuration in the application as needed.

5. **Run the application**:

   ```bash
   python app.py
   ```



6. **Access the application**:

   * Open your web browser and navigate to `http://localhost:5000`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.


