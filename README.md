# Scorix

**Scorix** is a Python-based tool that automates the creation of student marksheets in PDF format and delivers them directly via email.  
It streamlines the grading process, eliminates manual data entry, and ensures accurate, fast, and hassle-free distribution.

---

## 🚀 Features
- **Automated Marksheet Generation** – Create formatted PDF marksheets with ease.
- **Email Integration** – Send marksheets directly to student inboxes via SMTP.
- **Grade Calculation** – Automatically compute grades based on marks.
- **Error Reduction** – Minimizes manual errors and boosts efficiency.
- **Speed Boost** – Up to 80% faster than manual processing.

---

## 🛠️ Tech Stack
- **Python**
- **fpdf** – PDF generation
- **smtplib** – Email sending via SMTP
- **email.message** – Email formatting

---

## 📂 How It Works
1. **Collect Data** – Input student details and subject marks.
2. **Calculate Grades** – Automatically compute final grades.
3. **Generate PDF** – Use `fpdf` to create a clean, formatted marksheet.
4. **Send Email** – Use `smtplib` and `email.message` to send the PDF to the student’s email.

---

## 📋 Requirements
- Python 3.x
- fpdf (`pip install fpdf`)
- SMTP credentials for email sending

---

## ▶️ Usage
```bash
# Clone the repository
git clone https://github.com/your-username/scorix.git

# Navigate to project folder
cd scorix

# Install dependencies
pip install -r requirements.txt

# Run the script
python scorix.py
