import random

TASKS = {
    "easy": {
        "alert_type": "brute_force",
        "failed_logins": random.randint(50,150),
        "malware_detected": False,
        "network_traffic": random.randint(200,500),
        "severity": 3,
        "correct_action": 2
    },

    "medium": {
        "alert_type": "malware",
        "failed_logins": 0,
        "malware_detected": True,
        "network_traffic": random.randint(400,700),
        "severity": 4,
        "correct_action": 3
    },

    "hard": {
        "alert_type": "data_exfiltration",
        "failed_logins": random.randint(10,30),
        "malware_detected": True,
        "network_traffic": random.randint(800,1200),
        "severity": 5,
        "correct_action": 4
    }
}