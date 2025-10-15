class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name  # Private attribute
        self._date_of_birth = date_of_birth  # Private attribute (read-only)
        self._place_of_birth = place_of_birth  # Private attribute (read-only)
    
    # Getter and setter for name (can be changed)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        self._name = name.strip()
    
    # Getters for immutable attributes (read-only)
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    @property
    def place_of_birth(self):
        return self._place_of_birth
    
    def talk(self):
        return f"Hi, my name is {self._name} and I was born in {self._place_of_birth}."