""" Model for aircraft flights """
class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.get_seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def get_aircraft_model(self):
        return self._aircraft.get_model()

    def get_number(self):
        return self._number

    def get_airline(self):
        return self._number[:2]

    def get_seating(self):
        return self._seating
