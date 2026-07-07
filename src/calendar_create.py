import pandas as pd


def get_current_date():
    return pd.Timestamp.now().date()  


def generate_calendar():
    new_calendar = pd.DataFrame({
        "Date": pd.date_range("2026-01-01", "2026-12-31", freq="D")
    })

    new_calendar["Year"] = new_calendar["Date"].dt.year
    new_calendar["Month"] = new_calendar["Date"].dt.month
    new_calendar["MonthName"] = new_calendar["Date"].dt.month_name()
    new_calendar["Day"] = new_calendar["Date"].dt.day
    new_calendar["Weekday"] = new_calendar["Date"].dt.day_name()
    new_calendar["Week"] = new_calendar["Date"].dt.isocalendar().week
    new_calendar["Quarter"] = new_calendar["Date"].dt.quarter
    new_calendar["IsWeekend"] = new_calendar["Weekday"].isin(["Saturday", "Sunday"])

    print(new_calendar.head())
    return new_calendar

def save_calendar_to_csv(calendar_df, filename="calendar.csv"):
    calendar_df.to_csv(filename, index=False)
    print(f"Calendar saved to {filename}")

class Calendar:
    def __init__(self):
        self.chores = []


    
    def add_chore(self, chore):
        self.chores.append(chore)
    
    def remove_chore(self, chore):
        self.chores.remove(chore)
    
    def get_chores(self):
        return self.chores