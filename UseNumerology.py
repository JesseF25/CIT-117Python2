# Author:  Jesse Ferguson
#
# Make sure to put the .py files in the SAME directory/folder.

class Numerology:
    
    def __init__(self, input_name, DOB):
        self.__input_name = input_name
        self.__DOB = DOB
   

    def get_DOB(self, DOB, value):
        self.DOB = DOB
        self.value = value
  
    def get__LifePath(self, DOB):

        # class NumerologyCalculator:
    def __init__(self, DOB_string):
        """Expects dob_string in format MM/DD/YYYY"""
        self.DOB_string = DOB_string

    def get_reduced_sum(self):
        # 1. Extract only the digits from the string (ignore '/')
        digits = [int(d) for d in self.DOB_string if d.isdigit()]
        
        # 2. Add all digits together
        total = sum(digits)
        
        # 3. Reduce to a single digit (1-9) using the digital root formula
        # Formula: 1 + (n - 1) % 9
        if total == 0:
            return 0
        return 1 + (total - 1) % 9

# Example Usage:

calc = NumerologyCalculator(dob)
result = calc.get_reduced_sum()

print(f"Date of Birth: {dob}")
print(f"Reduced Sum (1-9): {result}")
        
        return self.date_of_birth
        return self.__LifePath

    def __getAttitude(self):
        return (self.__Attitude)

    def __getBirthDay(self, birthday):
        self.birthday = birthday
        self._year = year
        self._month = month
        self._day = day
        return self.__birthday

    def __getPersonality(self):
        return self.__Personality

    def __getPowerName(self):
        return self.__PowerName

    def __getSoul(self):
        
        return self.__Soul 
            
    # Code the "setters":
    def _setDateofBirth(self, DateofBirth):
        self.__number = number
        self.__DateofBirth = DateofBirth
