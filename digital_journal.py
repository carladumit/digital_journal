# Digital 5-year journal!

import sys
import csv
import os.path
import re
from tabulate import tabulate
from datetime import date


def main():

    # Displays a welcome message. Prompts the user to log in or register.
    print(tabulate([["WELCOME TO YOUR 5-YEAR JOURNAL"], ["[1] Log in"],
          ["[2] Register"], ["[3] Exit"]], headers='firstrow', tablefmt="outline"))

    # Read input from user
    while True:
        try:
            intro = int(input("What would you like to do? "))
            if 1 <= intro <= 3:
                break
        except ValueError:
            continue

    # Match the cases for the user's choice
    match intro:
        case 1:
            while True:
                username = input("Username: ")
                password = input("Password: ")
                if login("usernames.csv", username, password) == True:
                    journal = f"{username}_journal.csv"
                    options(journal)
                    break
                else:
                    continue
        case 2:
            while True:
                username = input("Username: ")
                password = input("Password: ")
                if register("usernames.csv", username, password) == True:
                    journal = f"{username}_journal.csv"
                    new_journal(journal)
                    options(journal)
                    break
                else:
                    continue
        case 3:
            sys.exit(0)


def register(users, username, password):
    """  Allows the user to register if the username is not already in use. """

    # Create the usernames CSV file if it does not exist
    if not os.path.exists(users):
        with open(users, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["username", "password"])
            writer.writeheader()
            #writer.writerow({"username": username, "password": password})

    # Read the file and check if the username already exists
    with open(users) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username:
                print("Username already exists. Please choose a different one.")
                return False

    # If the username is available, append the new username to the file
    with open(users, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        writer.writerow({"username": username, "password": password})
    print("User registered successfully")
    return True


def login(users, username, password):
    """Allows the user to log in if the username and password match the users file."""

    # Read the file cointaining the usernames and passwords
    # and check that both match the input data
    with open(users) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                print("Login successful. Welcome back!")
                return True

    # If incorrect username or password:
    print("Incorrect username or password.")
    return False


def options(filename):
    """Dispalys the options and prompts the user to choose from a menu of options."""

    print(tabulate([["5-YEAR JOURNAL"], ["[1] New Entry"], ["[2] Read Journal"], ["[3] Delete Entry"],
                    ["[4] Exit"]], headers='firstrow', tablefmt="outline"))

    # Get input from user and handle errors
    while True:
        try:
            option = int(input("What would you like to do? "))
            if 1 <= option <= 4:
                break
        except ValueError:
            continue

    # Match the user's choice
    match option:
        case 1:
            while True:
                date = input("For what date [yyyy-mm-dd] would you like to write an entry? ")
                if valid_date(date):
                    break
            new_entry(filename, date)
        case 2:
            while True:
                date = input("For what day [yyyy-mm-dd] do you want to read your journal? ")
                if valid_date(date):
                    break
            y,mm,dd = date.split("-")
            read_entry(filename, dd, mm)
        case 3:
            while True:
                date = input("What entry do you want to delete? Enter a date [yyyy-mm-dd]: ")
                if valid_date(date):
                    break
            delete_entry(filename, date)
        case 4:
            sys.exit(0)


def valid_date(date):
    """ Checks if input date is valid."""

    if (re.match(r"^\d{4}-\d{2}-\d{2}$", date)
            and 1 <= int(date.split("-")[1]) <= 12
            and 1 <= int(date.split("-")[2]) <= 31):
        return True
    else:
        print("Please enter a valid date in yyyy-mm-dd format.")
        return False


def new_journal(filename):
    """ Creates a new journal."""

    # Create a new CSV file and writes the header only
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "rating", "text"])
        writer.writeheader()
    print(f"Your journal was created successfully!")

    # Create the first entry, for today's date
    today = date.today().isoformat()
    print(f"Today is {today}")
    new_entry(filename, today)


def new_entry(filename, date):
    """Writes a new entry in the journal, containing the text and the rating for a date.
    Shows previous entries for the same date.
    """

    # Get day and month from date
    month = date.split("-")[1]
    day = date.split("-")[2]

    # Prompt the user for the entry and the rating of the day using emojis
    # and handles numeric input errors
    text = input("What are your thoughts today? ")
    while True:
        try:
            rating = int(input("How would you rate your day? [1:😭 2:🙁 3:😐 4:🙂 5:😄] "))
            if 1 <= rating <= 5:
                break
        except ValueError:
            continue

    # Convert user's numeric input to emojis
    match rating:
        case 1:
            rating = "😭"
        case 2:
            rating = "🙁"
        case 3:
            rating = "😐"
        case 4:
            rating = "🙂"
        case 5:
            rating = "😄"

    # Append the information to a new row in the file
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "rating", "text"])
        writer.writerow({"date": date, "rating": rating, "text": text})
    print("Entry added successfully!")

    # Show previous entries for the same day and month
    read_entry(filename, day, month)


def read_entry(filename, day, month):
    """Retrieves entries for a specific day and month."""

    # Creates empty list to store entries
    entries = []

    # Read file
    with open(filename) as file:
        reader = csv.DictReader(file)
        # Parse each row in file, compares date with specified day and month, adds matching data to list
        for row in reader:
            entry_date = row["date"]
            entry_year = entry_date.split("-")[0]
            entry_month = entry_date.split("-")[1]
            entry_day = entry_date.split("-")[2]
            if entry_day == day and entry_month == month:
                entries.append({"year": entry_year, "rating": row["rating"], "text": row["text"]})

        # Print each entry
        print(f"Entries for {day}/{month}:")
        for entry in entries:
            print(tabulate([[entry["year"]], ["Today was a " + entry["rating"] + " day"],
                  [entry["text"]]], headers='firstrow', tablefmt="outline"))

    # Go back to menu to allow other actions
    options(filename)


def delete_entry(filename, date):
    """Delete the entry for the selected date."""

    entries = []  # Create an empty list to store entries
    deleted = False  # Set deleted state to false

    # Read the CSV file
    with open(filename) as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames  # Store fieldnames values
        for row in reader:
            # Copy all entries save for the one that should be deleted
            if row["date"] != date:
                entries.append(row)
            else:
                deleted = True  # Set deleted state to True: the entry was found

    # Write the entries that are stored in the list to the file
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

    # Print a message for the user
    if deleted == True:
        print(f"Entry for {date} deleted successfuly.")
    elif deleted == False:
        print(f"Could not find entry for {date}.")

     # Go back to menu to allow other actions
    options(filename)

    
if __name__ == "__main__":
    main()
