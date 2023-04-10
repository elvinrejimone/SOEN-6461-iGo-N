import time

class FerrySchedule:
    def __init__(self):
        self.schedules = {
    "Montreal": [
        {
            "time": 900,
            "time_text": "9:00 AM Ferry",
            "remaining_seats": 56,
            "price": 45.00
        },
        {
            "time": 1300,
            "time_text": "1:00 PM Ferry",
            "remaining_seats": 76,
            "price": 30.00
        },
        {
            "time": 1700,
            "time_text": "5:00 PM Ferry",
            "remaining_seats": 81,
            "price": 55.00
        }
    ],
    "Kingston": [
        {
            "time": 930,
            "time_text": "9:30 AM Ferry",
            "remaining_seats": 34,
            "price": 45.00
        },
        {
            "time": 1330,
            "time_text": "1:30 PM Ferry",
            "remaining_seats": 12,
            "price": 30.00
        },
        {
            "time": 1730,
            "time_text": "5:30 PM Ferry",
            "remaining_seats": 18,
            "price": 55.00
        }
    ],
    "Toronto": [
        {
            "time": 1000,
            "time_text": "10:00 AM Ferry",
            "remaining_seats": 43,
            "price": 45.00
        },
        {
            "time": 1400,
            "time_text": "2:00 PM Ferry",
            "remaining_seats": 63,
            "price": 30.00
        },
        {
            "time": 1800,
            "time_text": "6:00 PM Ferry",
            "remaining_seats": 22,
            "price": 55.00
        }
    ],
    "Ottawa": [
        {
            "time": 1030,
            "time_text": "10:30 AM Ferry",
            "remaining_seats": 17,
            "price": 45.00
        },
        {
            "time": 1430,
            "time_text": "2:30 PM Ferry",
            "remaining_seats": 29,
            "price": 30.00
        },
        {
            "time": 1830,
            "time_text": "6:30 PM Ferry",
            "remaining_seats": 37,
            "price": 55.00
        }
    ],
    "Quebec City": [
        {
            "time": 1100,
            "time_text": "11:00 AM Ferry",
            "remaining_seats": 62,
            "price": 45.00
        },
        {
            "time": 1500,
            "time_text": "3:00 PM Ferry",
            "remaining_seats": 49,
            "price": 30.00
        },
        {
            "time": 1900,
            "time_text": "7:00 PM Ferry",
            "remaining_seats": 28,
            "price": 55.00
        }
    ]
}

    
    def get_schedule(self, city):
        current_time = int(time.strftime("%H%M"))
        schedule = [s for s in self.schedules[city] if s["time"] > current_time]
        return schedule
    
    def decrement_seats(self, city, time):
        for s in self.schedules[city]:
            if s["time"] == time:
                s["remaining_seats"] -= 1
                return True
        return False