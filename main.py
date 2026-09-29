from patient_manager import create_patient, find_patient, get_highest_risk_patient
from reports import display_report, display_all_patients, display_highest_risk


def read_number(prompt, cast=float, minimum=0):

    while True:
        try:
            value = cast(input(prompt))
            if value < minimum:
                print("Value cannot be less than", minimum)
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def read_name(prompt):
    
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Name cannot be empty.")


def add_patient_menu(patients):
    print("\n========== ADD PATIENT ==========")
    name = read_name("Enter patient name: ")
    age = read_number("Enter age: ", cast=int)
    hr = read_number("Enter heart rate: ")
    spo2 = read_number("Enter SpO2: ")
    temp = read_number("Enter temperature: ")
    resp_rate = read_number("Enter respiratory rate: ")

    patient = create_patient(patients, name, age, hr, spo2, temp, resp_rate)
    print("\nPatient added successfully!")
    print("Patient ID:", patient["id"])


def view_patient_menu(patients):
    if not patients:
        print("\nNo patients available.")
        return
    patient = find_patient(patients, input("\nEnter Patient ID: "))
    if patient:
        display_report(patient)
    else:
        print("Patient not found.")


def main():
    patients = []

    print("\n======================================")
    print("   BIOMEDICAL PATIENT MONITORING")
    print("======================================")

    while True:
        print("\n1. Add New Patient")
        print("2. View Patient Report")
        print("3. Search Patient")
        print("4. Display All Patients")
        print("5. Find Highest Risk Patient")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_patient_menu(patients)
        elif choice in ("2", "3"):
            view_patient_menu(patients)
        elif choice == "4":
            display_all_patients(patients)
        elif choice == "5":
            display_highest_risk(get_highest_risk_patient(patients))
        elif choice == "6":
            print("\nThank you for using the system!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()