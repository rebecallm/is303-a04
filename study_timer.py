'''
Rebeca Llontop
IS 303 - A04

Study Timer: This program logs study sessions with subject, duration, and date, 
then shows statistics.

Inputs:
- subject(str)
- duration(int)
- date(int, int, int)

Processes:
- datetime library for date handling
- get_valid_int(prompt): keeps asking until user enters a valid integer (try/except)
- calculate_total_sessions(sessions, subject): returns the total number of study sessions 
along with their subjects
- calculate_total_minutes(sessions, minutes): returns the total minutes studied
- find_busiest_subject(sessions, duration): returns the subject with the most study time
- display_report(total_sessions, total_minutes, busiest_subject): prints formatted statistics

Outputs:
- display report
- total sessions logged
- total minutes studied 
- busiest subject
'''
import datetime

# ----Functions----

def get_valid_int(prompt):
    """Keep asking until user enters a valid integer number."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def calculate_total_sessions(sessions): 
    """returns the total number of study sessions along with their subjects. """
    return len(sessions)

def calculate_total_minutes(sessions):
    """returns the total minutes studied. """
    total = 0 
    for log in sessions: 
        total += log['minutes']
    return total  

def find_busiest_subject(sessions):
    """returns the subject with the most study time. """
    subject_time = {}
    for log in sessions:
        subject = log['subject']
        minutes = log['minutes']
        if subject in subject_time:
            subject_time[subject] += minutes
        else:
            subject_time[subject] = minutes
    busiest_subject = max(subject_time, key=subject_time.get)
    return busiest_subject

def display_report(total_sessions, total_minutes, busiest_subject):
    """prints formatted statistics."""
    print("\nStudy Report:")
    print(f"Total sessions logged: {total_sessions}")
    print(f"Total minutes studied: {total_minutes}")
    print(f"Busiest subject: {busiest_subject}")

# ----Main Program----
def main():
    sessions = []
    num_sessions = get_valid_int("Enter the number of study sessions: ")
    for i in range(num_sessions):
        print(f"\nSession {i+1}:")
        subject = input("Enter the subject: ")
        minutes = get_valid_int("Enter the duration in minutes: ")
        sessions.append({
            "subject": subject, "minutes": minutes
        })
        
    total_sessions = calculate_total_sessions(sessions)
    total_minutes = calculate_total_minutes(sessions) 
    busies_subject = find_busiest_subject(sessions)
    
    display_report(total_sessions, total_minutes, busies_subject)

if __name__ == "__main__":
    main()
