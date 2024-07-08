# 5-YEAR JOURNAL

### Video Demo
<https://youtu.be/8c--HvXIgCk>

### Description

A 5-year journal is a type of journal designed to record the most memorable events, feelings or thoughts of each day, within a period of 5 years. Each page of the journal is destined to a day of the year, divided in 5 sections, one per year. In the end, this diary will allow the user to reflect on how they and the world around them have changed during this period of time.
This is a digital journal application that allows users to keep track of their daily thoughts and rate their day using emojis, over a period of 5 years. Users can register, log in, write new entries, read previous entries and delete entries as needed.

### Features

- User registration and login system.
- Create a new journal for each user.
- Write new journal entries for specific dates.
- Read entries across years for a specific date.
- Delete entries by choosing a date.

### Requirements

- Python 3.x
- `pip install tabulate`

### Usage

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Run the application by executing the following command: `python digital_journal.py`
4. Follow the on-screen prompts to register/login and use the journal features.

### Files

- `digital_journal.py`: Main Python script containing the application logic.
- `test_digital_journal.py`: Test script containig unit tests for the application functions.
- `usernames.csv`: File storing user account information (username and password).
- `*.csv`: Journal files, one for each user, storing journal entries.

### Challenges Encountered

This is my first project in Python, also my final project for HarvardX CS50 Python Couse.
It was an overall nice project to solidify my knowledge of Python, practice file I/O and dict handling, as well as implement several functions, including nested functions. I have also learned how to comment properly a large script using docstring, and improve my code regarding consistency, code reusability, input sanitization and user experience.
My main challenge was writing a solid unit test file. Most of the functions in this project are void functions, which I had never had to test before. I still have a lot of work to do here!
