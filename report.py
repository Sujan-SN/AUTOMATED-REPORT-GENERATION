import csv
from fpdf import FPDF

# Read data
names = []
marks = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append(row["Name"])
        marks.append(int(row["Marks"]))

# Analysis
total_students = len(marks)
average_marks = sum(marks) / total_students
highest_marks = max(marks)
lowest_marks = min(marks)

# Create PDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=16)
pdf.cell(200, 10, "Student Report", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)

# Summary
pdf.cell(200, 10, f"Total Students: {total_students}", ln=True)
pdf.cell(200, 10, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(200, 10, f"Highest Marks: {highest_marks}", ln=True)
pdf.cell(200, 10, f"Lowest Marks: {lowest_marks}", ln=True)

pdf.ln(10)

# Table Header
pdf.cell(100, 10, "Name", border=1)
pdf.cell(50, 10, "Marks", border=1)
pdf.ln()

# Table Data
for i in range(total_students):
    pdf.cell(100, 10, names[i], border=1)
    pdf.cell(50, 10, str(marks[i]), border=1)
    pdf.ln()

# Save PDF
pdf.output("report.pdf")

print("PDF report generated successfully!")
