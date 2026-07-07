import pandas as pd
from chore_create import chore
import os


def load_chores_from_csv(filename="csv_files/chores.csv"):
    if not os.path.exists(filename):
        return []
    chore_df = pd.read_csv(filename)
    chores = []
    for _, row in chore_df.iterrows():
        start_date = pd.to_datetime(row["start_date"]) if "start_date" in row and pd.notnull(row["start_date"]) else None
        last_completed = pd.to_datetime(row["last_completed"]) if "last_completed" in row and pd.notnull(row["last_completed"]) else None
        next_due_date = pd.to_datetime(row["next_due_date"]) if "next_due_date" in row and pd.notnull(row["next_due_date"]) else None
        new_chore = chore(
            name=row["name"],
            description=row["description"],
            frequency=row["frequency"],
            length=row["length"],
            area=row["area"],
            start_date=start_date,
            last_completed=last_completed,
            next_due_date=next_due_date
        )
        chores.append(new_chore)
    return chores

def save_chores_to_csv(chores, filename="csv_files/chores.csv"):
    chore_data = [chore.get_info() for chore in chores]
    chore_df = pd.DataFrame(chore_data)
    chore_df.to_csv(filename, index=False)
    print(f"Chores saved to {filename}")