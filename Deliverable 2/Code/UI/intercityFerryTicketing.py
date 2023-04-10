import json
import datetime

INTERCITY_SCHEDULE = "./configs/intercity_ferry_schedule.json"

class FerrySchedule:
    def __init__(self, city):
        self.city = city
        self.data = {}
        self.load_data()

    def load_data(self):
        with open(INTERCITY_SCHEDULE, "r") as f:
            self.data = json.load(f)
        
    def save_data(self):
        with open(INTERCITY_SCHEDULE, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_next_ferry_schedules(self):
        self.load_data()
        schedules = []
        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d")
        for schedule in self.data[self.city]:
            schedule_time = datetime.datetime.strptime(f"{today} {schedule['time']}", "%Y-%m-%d %H%M")
            if schedule_time > now and schedule['remaining_seats'] > 0:
                schedules.append(schedule)
        return schedules

    def decrement_seats(self, schedule):
        for s in self.data[self.city]:
            if s["time"] == schedule["time"]:
                s["remaining_seats"] -= 1
                self.save_data()
                break
    
    def decrement_seats_by_value(self, schedule, value):
        for s in self.data[self.city]:
            if s["time"] == schedule:
                s["remaining_seats"] -= value
                self.save_data()
                break
    
    def get_ferry_schedule_by_time(self, time):
        for schedule in self.data[self.city]:
            if schedule['time'] == time:
                return schedule
        return None