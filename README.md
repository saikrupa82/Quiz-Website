# College Student Quiz System - Django Web Application

This is a Django-based web application designed for colleges to create and manage quizzes for students. The application allows lecturers to create quizzes, manage quiz sessions, and view the performance of students. Students can take quizzes, view results, and track their progress. It includes features like user authentication, quiz creation, leaderboard management, and session handling.
![image](https://github.com/user-attachments/assets/4de9b914-88ce-4554-96f6-6e8b4308748c)

## Features

### 1. **User Authentication**
   - Custom user models for students and lecturers with login and registration functionalities.
   - Role-based access control using Django’s built-in authentication system.
   - Separate dashboards for students and lecturers.

### 2. **Quiz Creation and Management**
   - Lecturers can create quizzes with multiple-choice questions.
   - Quiz creation interface where lecturers can define quiz duration, questions, and answers.
   - Quizzes are stored in the database and tied to specific sessions and classes.
   - Real-time update of quiz details and questions.

### 3. **Quiz Sessions**
   - Sessions track individual quiz sessions, including branches, year, and types of exams (Quiz or Lab).
   - Session management with the ability to start and stop quizzes dynamically.

### 4. **Quiz Taking**
   - Students can take quizzes with real-time progress tracking and a timer for each session.
   - Results are calculated upon submission, with correct answers and scores displayed.

### 5. **Leaderboard**
   - A leaderboard that tracks student performance across multiple quizzes.
   - Scores are stored and displayed for each quiz with the correct and wrong answers.

### 6. **Profile Management**
   - Users can update their profile information.
   - Lecturers and students can view performance statistics and track quiz history.

### 7. **Data Export**
   - Quiz results are exported to CSV files for record-keeping.
   - Quiz data and student scores can be exported for external use.

## Folder Structure

```
- CSV/                   # CSV files for quiz data and leaderboard export
- CollegeWebsite/         # Main website directory
- quiz/                   # Django app for managing quizzes
- root/                   # Core Django project files
- static/                 # Static assets for the project (CSS, JS, etc.)
- students/               # Django app managing student information
- users/                  # Django app managing user authentication and roles
- README.md               # Documentation for the project
- db.sqlite3              # SQLite database storing application data
- manage.py               # Django management script
```

## Setup Instructions

### Requirements:
- Python 3.x
- Django 3.x
- SQLite (or any other database configured in settings)
- Other dependencies are listed in `requirements.txt` (if available).

### Steps to Run:
1. Clone the repository:
   ```
   git clone https://github.com/saikrupa82/College-Quiz-System.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```
   python manage.py migrate
   ```
4. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```
6. Access the application via:
   ```
   http://127.0.0.1:8000/
   ```

## Key Models and Functionality

### `Session_Details`
Handles the session data, including quiz names, branches, years, and the quiz creator’s information.
![image](https://github.com/user-attachments/assets/9e42028c-56e7-498b-9616-b9f05ddf0284)


### `Quiz`
Stores individual quiz questions and their options. Also tracks correct answers for each quiz session.
![image](https://github.com/user-attachments/assets/dbe3b938-3443-4d88-a1e7-f40e67d1ef04)


### `QuizList`
Tracks the list of quizzes and handles the duration and number of questions.

### `LeaderBoard`
Stores the results for each quiz, including total scores, correct answers, and wrong answers.

### `Student_Details`
Handles student-specific information like roll number, role, and other personal details.

### `CustomUser`
Custom user model extending Django’s `AbstractUser` for handling different user types.
![image](https://github.com/user-attachments/assets/a0057158-fde9-44a6-8b29-5ee7afde7293)


## Screenshots
![image](https://github.com/user-attachments/assets/0bec9579-7524-49ad-afc6-07111c75769d)

![image](https://github.com/user-attachments/assets/3a90df20-415c-405b-9ba4-ac04d8678550)


