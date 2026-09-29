from vitals import (
    check_heart_rate,
    check_spo2,
    check_temperature,
    check_respiratory_rate,
)


def calculate_risk(hr, spo2, temp, resp_rate):
    
    checks = [
        check_heart_rate(hr),
        check_spo2(spo2),
        check_temperature(temp),
        check_respiratory_rate(resp_rate),
    ]
    return sum(1 for result in checks if result != "NORMAL")


def patient_status(risk):
    
    if risk == 0:
        return "NORMAL"
    elif risk <= 2:
        return "REQUIRES ATTENTION"
    return "HIGH ALERT"


def risk_of(patient):
    
    return calculate_risk(
        patient["heart_rate"],
        patient["spo2"],
        patient["temperature"],
        patient["respiratory_rate"],
    )