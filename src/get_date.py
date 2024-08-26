from datetime import date

def get_date():
    try:
        current_date = date.today()
        return str(current_date)
    except Exception as e:
        print(f"An error occurred while getting the date: {e}")
        return None
