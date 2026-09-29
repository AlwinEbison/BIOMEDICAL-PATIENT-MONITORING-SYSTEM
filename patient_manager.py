from risk import risk_of


def create_patient(patients, name, age, hr, spo2, temp, resp_rate):
    
    patient = {
        "id": "P" + str(len(patients) + 1),
        "name": name,
        "age": age,
        "heart_rate": hr,
        "spo2": spo2,
        "temperature": temp,
        "respiratory_rate": resp_rate,
    }
    patients.append(patient)
    return patient


def find_patient(patients, patient_id):
    
    patient_id = patient_id.strip().upper()
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None


def get_highest_risk_patient(patients):
    
    if not patients:
        return None
    return max(patients, key=risk_of)