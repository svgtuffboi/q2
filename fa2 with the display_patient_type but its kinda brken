# Keith Esdrelon || 9-PINATUBO || CS3FA1Q2

# Creating the parent class
class Patient:
    __name: str
    __bill_amount: float
    kind = "Regular Patient"
    def __init__(self,name,bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_name(self,name):
        self.__name = name
    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount
    def display_patient_type(self):
        self.patient_type = "Patient Type: Regular Citizen"
        return patient_type
    def calculate_bill(self):
        print(f"Patient Name: {self.__name}\nPatient Type: {patient_type}\nOriginal Bill: {self.__bill_amount}\nFinal Bill: {self.__bill_amount}")

# Creating the child classes

class PhilHealthAgent(Patient):
    def display_patient_type(self):
        patient_type = "Patient Type: Senior Citizen"
        return patient_type
    def calculate_bill(self):
        original_bill = self.get_bill_amount()
        final_bill = original_bill * 0.85
        print(f"Patient Name: {self.__name}\nPatient Type: {patient_type}\nOriginal Bill: {self.__bill_amount}\nFinal Bill: {self.__bill_amount}")
    
class Senior(Patient):
    def display_patient_type(self):
        patient_type = "Patient Type: Senior Citizen"
        return patient_type
    def calculate_bill(self):
        original_bill = self.get_bill_amount()
        final_bill = original_bill * 0.80
        print(f"Patient Name: {self.__name}\nPatient Type: {patient_type}\nOriginal Bill: {self.__bill_amount}\nFinal Bill: {self.__bill_amount}")

# Creating the objects

normal_dude = Patient("Juan Dela Cruz",15000)
philhealth_dude = Senior("Maria Santos",15000)
old_dude = PhilHealthAgent("Pedro Reyes",15000)

print("Hospital Billing System\n-----------------------")
normal_dude.calculate_bill()

philhealth_dude.calculate_bill()

old_dude.calculate_bill()

