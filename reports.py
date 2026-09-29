from vitals import (
    check_heart_rate,
    check_spo2,
    check_temperature,
    check_respiratory_rate,
)
from risk import risk_of, patient_status


def display_report(patient):
    
    print("\n========== PATIENT REPORT ==========")
    print("Patient ID   :", patient["id"])
    print("Name         :", patient["name"])
    print("Age          :", patient["age"])

    print("\n--- Vital Signs ---")
    print("Heart Rate   :", patient["heart_rate"], "bpm")
    print("SpO2         :", patient["spo2"], "%")
    print("Temperature  :", patient["temperature"], "C")
    print("Resp. Rate   :", patient["respiratory_rate"], "/min")

    print("\n--- Results ---")
    print("Heart Rate   :", check_heart_rate(patient["heart_rate"]))
    print("SpO2         :", check_spo2(patient["spo2"]))
    print("Temperature  :", check_temperature(patient["temperature"]))
    print("Resp. Rate   :", check_respiratory_rate(patient["respiratory_rate"]))

    risk = risk_of(patient)
    print("\nRisk Score   :", risk)
    print("Status       :", patient_status(risk))
    print("====================================")


def display_all_patients(patients):
    
    if not patients:
        print("\nNo patients available.")
        return

    print("\n========== ALL PATIENTS ==========")
    for patient in patients:
        risk = risk_of(patient)
        print(patient["id"], "|", patient["name"],
              "| Risk:", risk, "|", patient_status(risk))


def display_highest_risk(patient):
    
    if patient is None:
        print("\nNo patients available.")
        return

    risk = risk_of(patient)
    print("\n========== HIGHEST RISK PATIENT ==========")
    print("Patient ID :", patient["id"])
    print("Name       :", patient["name"])
    print("Risk Score :", risk)
    print("Status     :", patient_status(risk))