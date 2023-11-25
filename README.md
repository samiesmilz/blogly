# Welcome To logly

Blogly is a simple Flask web application for managing user profiles.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samiesmilz/blogly.git
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```bash
   flask run
   ```

## Usage

- Visit [http://localhost:5000](http://localhost:5000) in your web browser to access the Blogly application.
- Explore various features such as creating, updating, and deleting user profiles.

## Features

- **User Management:**

  - Create new user profiles.
  - View a list of all users.
  - View a single user's profile.
  - Edit and update user profiles.
  - Delete user profiles.

- **Simple and Responsive Design:**
  - Responsive design for a seamless experience on various devices.

## Contributing

Contributions are welcome! If you have any improvements or feature suggestions, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
