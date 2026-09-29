HEART_RATE_RANGE = (60, 100)        
SPO2_MIN = 95                       
TEMPERATURE_RANGE = (36, 37.5)      
RESP_RATE_RANGE = (12, 20)          


def _classify_range(value, low, high):
    
    if value < low:
        return "LOW"
    elif value > high:
        return "HIGH"
    return "NORMAL"


def check_heart_rate(hr):
    return _classify_range(hr, *HEART_RATE_RANGE)


def check_spo2(spo2):
    return "LOW" if spo2 < SPO2_MIN else "NORMAL"


def check_temperature(temp):
    return _classify_range(temp, *TEMPERATURE_RANGE)


def check_respiratory_rate(rate):
    return _classify_range(rate, *RESP_RATE_RANGE)