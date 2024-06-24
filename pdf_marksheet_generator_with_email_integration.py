import smtplib
from email.message import EmailMessage
def send_email_with_attachment(receiver_email, subject, body, attachment_filename):
    sender_email = "Enter your email"  # Update with your email
    sender_password = "Enter your password"  # Update with your password

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

    with open(attachment_filename, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Update with your SMTP server details
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


from fpdf import FPDF

def generate_pdf(marksheet, pdf_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in marksheet.split("\n"):
        pdf.cell(190, 10, txt=line, ln=True)

    pdf.output(pdf_filename)

def create_and_print_marksheet(student_name, marksheet):
    pdf_filename = f"{student_name}_Marksheet.pdf"
    generate_pdf(marksheet, pdf_filename)
    print(f"PDF marksheet saved as: {pdf_filename}")

subject_1_name = "EM IV"
subject_1_type = "Theory"
subject_1_total_marks = 30

subject_2_name = "OS"
subject_2_type = "Theory"
subject_2_total_marks = 30

subject_3_name = "Tafl"
subject_3_type = "Theory"
subject_3_total_marks = 30

subject_4_name = "Cloud Computing"
subject_4_type = "Theory"
subject_4_total_marks = 30

subject_5_name = "Technical Communication"
subject_5_type = "Theory"
subject_5_total_marks = 30

subject_6_name = "Java"
subject_6_type = "Theory"
subject_6_total_marks = 30

subject_7_name = "Cyber Security"
subject_7_type = "Theory"
subject_7_total_marks = 30

total_marks = (
    subject_1_total_marks
    + subject_2_total_marks
    + subject_3_total_marks
    + subject_4_total_marks
    + subject_5_total_marks
    + subject_6_total_marks
    + subject_7_total_marks
    
)

def is_valid_string(user_input):
    valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,'"
    for char in user_input:
        if char not in valid_characters:
            return False
    return True


def get_string_input(prompt):
    while True:
        user_input = input(prompt)
        if is_valid_string(user_input):
            return user_input
        else:
            print("Please enter a valid string.")

institute_name = get_string_input("Enter Institute Name: ")
print()  
course_name = get_string_input("Enter Course Name: ")
print()  
branch_name = get_string_input("Enter Branch Name: ")
print()
session = input("Enter Session (Format: YYYY-YY): ")
print()
semester = input("Enter Semester (Single digit, 1-8): ")
print()
roll_number = input("Enter Roll Number (13 digits): ")
print()
student_name = get_string_input("Enter Student Name: ")
print() 

print(
    """         
                *Enter Internal Marks*          
"""
)

def input_and_validate_internal_marks(subject_name, max_marks):

    marks = -1  

    while marks < 0 or marks > max_marks:  
        marks = int(
            input(f"{subject_name} (0-{max_marks}): ")
        )  
        if marks < 0 or marks > max_marks: 
            print(
                f"""
                Marks should be between 0 and {max_marks}.  # Informing the user about the valid range of marks
                """
            )
    print()  
    return marks  
subject_1_internal_marks = input_and_validate_internal_marks(subject_1_name, 30)
subject_2_internal_marks = input_and_validate_internal_marks(subject_2_name, 30)
subject_3_internal_marks = input_and_validate_internal_marks(subject_3_name, 30)
subject_4_internal_marks = input_and_validate_internal_marks(subject_4_name, 30)
subject_5_internal_marks = input_and_validate_internal_marks(subject_5_name, 30)
subject_6_internal_marks = input_and_validate_internal_marks(subject_6_name, 30)
subject_7_internal_marks = input_and_validate_internal_marks(subject_7_name, 30)

total_mark_obtained = (
    subject_1_internal_marks
    + subject_2_internal_marks
    + subject_3_internal_marks
    + subject_4_internal_marks
    + subject_5_internal_marks
    + subject_6_internal_marks
    + subject_7_internal_marks

)

subject_1_percentage = (subject_1_internal_marks / subject_1_total_marks) * 100
subject_2_percentage = (subject_2_internal_marks/ subject_2_total_marks) * 100
subject_3_percentage = (subject_3_internal_marks / subject_3_total_marks) * 100
subject_4_percentage = (subject_4_internal_marks / subject_4_total_marks) * 100
subject_5_percentage = (subject_5_internal_marks / subject_5_total_marks) * 100
subject_6_percentage = (subject_6_internal_marks/ subject_6_total_marks) * 100
subject_7_percentage = (subject_7_internal_marks / subject_7_total_marks) * 100

overall_percentage = (total_mark_obtained / total_marks) * 100

if overall_percentage >= 40:
    passing_status = "Passed"  
else:
    passing_status = "Failed" 

def calculate_grade(percentage):
    
    if percentage >= 90:
        return "A+" 
    elif percentage >= 80:
        return "A"  
    elif percentage >= 70:
        return "B+" 
    elif percentage >= 60:
        return "B" 
    elif percentage >= 50:
        return "C"  
    elif percentage >= 45:
        return "D" 
    elif percentage >= 40:
        return "E"  
    else:
        return "F"  
    
subject_1_grade = calculate_grade(subject_1_percentage)
subject_2_grade = calculate_grade(subject_2_percentage)
subject_3_grade = calculate_grade(subject_3_percentage)
subject_4_grade = calculate_grade(subject_4_percentage)
subject_5_grade = calculate_grade(subject_5_percentage)
subject_6_grade = calculate_grade(subject_6_percentage)
subject_7_grade = calculate_grade(subject_7_percentage)

def calculate_grade_points(grade):
    if grade == "A+":
        return 10  
    elif grade == "A":
        return 9  
    elif grade == "B+":
        return 8  
    elif grade == "B":
        return 7 
    elif grade == "C":
        return 6  
    elif grade == "D":
        return 5  
    elif grade == "E":
        return 4 
    elif grade == "F":
        return 0  
    
subject_1_grade_points = calculate_grade_points(subject_1_grade)
subject_2_grade_points = calculate_grade_points(subject_2_grade)
subject_3_grade_points = calculate_grade_points(subject_3_grade)
subject_4_grade_points = calculate_grade_points(subject_4_grade)
subject_5_grade_points = calculate_grade_points(subject_5_grade)
subject_6_grade_points = calculate_grade_points(subject_6_grade)
subject_7_grade_points = calculate_grade_points(subject_7_grade)

marksheet = f"""
===================================================================================================================
Institute Name  :  {institute_name.upper()}
Course Name     :  {course_name.upper(): <40}   
Session         :  {session: <40}               
Roll Number     :  {roll_number: <40}        
Student Name    :  {student_name.upper(): <40} 
Branch Name     :  {branch_name.upper()}
Semester        :  {semester}

===================================================================================================================
 ___________________________________
| Name                      | Type                      | Internal                          | Grade |
|----------|--------------------------------------------------------|----------------|----------|---------
| {subject_1_name: <54}     | {subject_1_type: <14}     | {subject_1_internal_marks: <8}    | {subject_1_grade: <5} |
| {subject_2_name: <54}     | {subject_2_type: <14}     | {subject_2_internal_marks: <8}    | {subject_2_grade: <5} |
| {subject_3_name: <54}     | {subject_3_type: <14}     | {subject_3_internal_marks: <8}    | {subject_3_grade: <5} |
| {subject_4_name: <54}     | {subject_4_type: <14}     | {subject_4_internal_marks: <8}    | {subject_4_grade: <5} |
| {subject_5_name: <54}     | {subject_5_type: <14}     | {subject_5_internal_marks: <8}    | {subject_5_grade: <5} |
| {subject_6_name: <54}     | {subject_6_type: <14}     | {subject_6_internal_marks: <8}    | {subject_6_grade: <5} |
| {subject_7_name: <54}     | {subject_7_type: <14}     | {subject_7_internal_marks: <8}    | {subject_7_grade: <5} |

--------------------------------------------------------------------------------------------------------------------
Result: {passing_status: <40} Total Marks: {total_marks: <34} Marks Obtained: {total_mark_obtained} 
"""

create_and_print_marksheet(student_name, marksheet)


def create_and_send_marksheet(student_name, marksheet, receiver_email):
    pdf_filename = f"{student_name}_Marksheet.pdf"
    generate_pdf(marksheet, pdf_filename)
    print(f"PDF marksheet saved as: {pdf_filename}")

    subject = "Marksheet for " + student_name
    body = "Please find attached the marksheet for the student."

    send_email_with_attachment(receiver_email, subject, body, pdf_filename)

receiver_email = input("Enter receiver's email address: ")
create_and_send_marksheet(student_name, marksheet, receiver_email)