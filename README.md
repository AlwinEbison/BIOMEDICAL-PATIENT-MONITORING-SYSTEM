# Biomedical Patient Monitoring System

## 1. Project Overview

The **Biomedical Patient Monitoring System** is a simple Python project that helps store and check basic patient information and vital signs.

The system allows the user to:

* Add a new patient
* View a patient's report
* Search for a patient
* Display all patients
* Find the patient with the highest risk
* Check the patient's vital signs
* Calculate a risk score
* Display the patient's health status

The project is made using basic Python concepts such as **functions, lists, dictionaries, loops, conditions, and modules**.


## 2. Features

### Add New Patient

The user can enter:

* Patient name
* Age
* Heart rate
* SpO2
* Temperature
* Respiratory rate

Each patient is automatically given a unique Patient ID such as `P1`, `P2`, etc.

### Check Vital Signs

The system checks four vital signs:

* Heart rate
* SpO2
* Temperature
* Respiratory rate

The values are classified as **LOW, HIGH, or NORMAL** based on the ranges defined in the program.

### Risk Score

The system calculates a risk score based on how many vital signs are outside the normal range.

The patient status is shown as:

* `NORMAL` — Risk score is 0
* `REQUIRES ATTENTION` — Risk score is 1 or 2
* `HIGH ALERT` — Risk score is more than 2

### Patient Reports

A detailed report can be displayed for a patient. It includes their personal information, vital signs, results, risk score, and status.

### Highest Risk Patient

The system can find and display the patient with the highest risk score.

---

## 3. Technologies and Tools Used

* **Python 3**
* Python functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Modules
* VS Code or any Python-compatible code editor

### Python Files

The project is divided into different files to keep the code organized:

```text
Biomedical Patient Monitoring/
│
├── main.py
├── patient_manager.py
├── risk.py
├── reports.py
└── vitals.py
```

### Description of Files

**main.py**
This is the main file of the project. It displays the menu and takes input from the user.

**patient_manager.py**
This file is used to create and search for patients and find the highest-risk patient.

**vitals.py**
This file contains the normal ranges and functions used to check the patient's vital signs.

**risk.py**
This file calculates the risk score and determines the patient's status.

**reports.py**
This file displays individual patient reports, all patients, and the highest-risk patient.

---

## 4. Installation and Running the Project

### Step 1: Download the Project

Download or clone the project files to your computer.

Make sure all five Python files are in the **same folder**:

```text
main.py
patient_manager.py
risk.py
reports.py
vitals.py
```

### Step 2: Open the Project

Open the project folder in **VS Code** or another Python editor.

### Step 3: Run the Program

Open the terminal inside the project folder and run:

```bash
python main.py
```

The main menu will appear:

```text
1. Add New Patient
2. View Patient Report
3. Search Patient
4. Display All Patients
5. Find Highest Risk Patient
6. Exit
```

Choose an option by entering its number.

## 5. Instructions for Testing

The project can be tested manually using different patient values.

### Test 1: Add a Patient

1. Run the program.
2. Select option `1`.
3. Enter the patient's name and vital signs.
4. Check that a Patient ID is created.

Example:

```text
Enter patient name: Rahul
Enter age: 20
Enter heart rate: 75
Enter SpO2: 98
Enter temperature: 36.8
Enter respiratory rate: 16
```

The program should create a patient ID such as:

```text
Patient added successfully!
Patient ID: P1
```

### Test 2: View Patient Report

1. Select option `2`.
2. Enter the Patient ID.
3. Check that the patient's information, vital signs, risk score, and status are displayed.

### Test 3: Search for a Patient

1. Select option `3`.
2. Enter an existing Patient ID.
3. Check that the correct patient report is displayed.

Try entering an incorrect Patient ID as well. The program should display:

```text
Patient not found.
```

### Test 4: Display All Patients

1. Add two or more patients.
2. Select option `4`.
3. Check that all added patients are displayed with their risk scores and statuses.

### Test 5: Find Highest Risk Patient

1. Add multiple patients with different vital sign values.
2. Select option `5`.
3. Check that the patient with the highest calculated risk score is displayed.

### Test 6: Invalid Input

Try entering invalid values such as text when a number is required.

The program should show an error message and ask for the value again.

##
