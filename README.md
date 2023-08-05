# Employee Management System

The Employee Management System is a comprehensive application designed to manage, query, and manipulate employee-related data within an organization. It provides options to view, add, update, and delete various data points, such as employee information, salaries, job titles, and more.

## Features
- View employee data count per country
- View manager count by department
- View dependent data per job title
- View hiring data by year and department
- View average salary data by job title
- View salary data by department
- Add/Delete/Update dependents
- Add/Delete/Update jobs
- User-friendly interface with error handling

## Requirements
- Python 3.x
- MySQL Database Server
- mysql-connector-python package

## Installation and Setup
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Run `pip install mysql-connector-python` to install the required MySQL connector.
3. **Database Configuration**: Set up your own MySQL database (see the "Database Configuration" section below).
4. **Update Connection Details**: Update the database connection details within the application's configuration.

## Database Configuration
Follow the instructions in the [Database Configuration section](#database-configuration) to set up your MySQL database.

## Usage
Run `python main.py` from the command line to launch the application. Follow the on-screen prompts to interact with the various features and functions.

## Support and Contribution
If you encounter any issues or have suggestions for improvements, please file an issue on GitHub or feel free to contribute by submitting a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Special thanks to Akpowo.

---

### Database Configuration

1. **Install MySQL**
2. **Create Database**
3. **Import Schema**: Import the provided SQL schema file into the newly created database.
4. **Configure Connection**: Provide the connection details, including host, username, password, and database name.
5. **Test Connection**

### Note
- Make sure that the MySQL server is running when using the application.
- Ensure proper permissions for the user connecting to the database.

Refer to the [MySQL official documentation](https://dev.mysql.com/doc/) for detailed instructions.

### Security Consideration
Keep your database credentials secure. Consider using environment variables or a separate configuration file that is not tracked by version control.
