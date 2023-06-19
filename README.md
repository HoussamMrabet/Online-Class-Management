# Online Class Management App

This is an online classroom management application developed by [Houssam Mrabet](https://github.com/HoussamMrabet) and [Hajar Ait Abdielmomin](https://github.com/Hajar20) as part of our bachelor's degree project. The application is built using *`Django`* and *`MySQL`* and provides a platform for students and professors to interact in a virtual classroom environment.

## Features

- **Landing Page**: The landing page of the application provides an overview of the app and its features.

- **Authentication**: Users can authenticate themselves by registering an account or logging in with their credentials.

- **User Spaces**: Upon successful authentication, users are redirected to their respective spaces based on their status, either as a student or a professor.

- **Professor's Profile**: Professors can manage their profile information, including their picture, name, password, and email.

- **Room Creation**: Professors can create study modules and invite their students by their unique ID codes to join the room.

- **Room Management**: Professors have administrative control over the study room. They can post courses, exercises, solutions, and TP assignments.

- **Student's Profile**: Students can manage their profile information, including their name, picture, password, and email.

- **Study Modules**: Students can access the study modules they have been invited to by their professors. They can view and download courses, as well as upload their answers for the exercises.

- **Admin Interface**: The admin interface, provided by Django, allows the admin to manage users and the application efficiently.

## Installation

1. Clone the repository from GitHub:

```bash
git clone https://github.com/your-github-repo-link
```

2. Change into the project directory:

```bash
cd online-classroom-management
```

3. Set up the MySQL database by creating a new database and updating the `settings.py` file with the appropriate credentials.

4. Apply the database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the application by visiting [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

- Register a new account or log in with existing credentials.

- Depending on your status (student or professor), you will be directed to your respective space.

- Professors can manage their profile, create study modules, and invite students to join.

- Students can manage their profile, access study modules they are invited to, and interact with course materials.

- The admin interface can be accessed at [http://localhost:8000/admin](http://localhost:8000/admin), where the admin can manage users and the application.

## Contributing

We welcome contributions to enhance the functionality and usability of the application. Feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or feedback, please contact [houssammrabet5@gmail.com](mailto:houssammrabet5@gmail.com).
