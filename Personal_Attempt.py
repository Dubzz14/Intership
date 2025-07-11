class HospitalRegistry:
    def __init__(self, Doctor_name, Patient_name, age, sex, symptoms,Insurance_number, Appointment_time, Treatment_price, Outcome):
        self.Doctor_name = Doctor_name
        self.Patient_name = Patient_name
        self.age = age
        self.sex =sex
        self.symptoms = symptoms
        self.Insurance_number = Insurance_number
        self.Appointment_time = Appointment_time
        self.Treatment_price = Treatment_price
        self.Outcome = Outcome
        self.discharged = False
        self.Hospital_registry = []

    def check_in(self):
        feel_ill = input(f"Does {self.Patient_name} feel ill?  (yes/no): ").lower()
        if feel_ill == "yes":
            print(f"{self.Patient_name}, you should fill in the form before seeing a doctor for treatment.")
            self.Patient_name = input("Enter your name: ")
            self.sex = input("Enter your sex: ")
            self.age = input("Enter your age: ")
            self.symptoms = input("Enter your symptoms (separated by commas): ").split(',')
            self.Insurance_number = input("Enter your Insurance number: ")
        else:
            print(f"{self.Patient_name} does not need to see a doctor right now.")
            

    def appointment(self, Appointment_time, Doctor_name, Patient_name):
        emergency_treatment = input("Were you brought in from Emergency?  (yes/no): ").lower()
        if emergency_treatment == "yes":
            print("We'll call a doctor to attend to you now.")
        else:
            print(f"{Patient_name}, your appointment has been booked for {Appointment_time} with Doctor {Doctor_name}")


    def discharge(self, Patient_name, Treatment_price, Outcome):
        if Outcome in ["Recovery", "Follow-up"]:
            self.discharged = True
            print(f"{Patient_name} has been discharged.")
            print(f"This is the price for your treatment: {Treatment_price}")
        else:
            self.discharged = False
            print("I'm sorry for your loss.")
            print(f"This is the price for your treatment: {Treatment_price}")
        

    def Registry(self, Doctor_name, Patient_name, age, sex, symptoms,Insurance_number, Appointment_time, Treatment_price, Outcome):
        self.Hospital_registry.append({"Doctor Name": Doctor_name, "Patient Name": Patient_name, "Age": age, "Sex": sex, "Symptoms": symptoms, "Insurance Number": Insurance_number, "Appointment time": Appointment_time, "Treatment Price": Treatment_price, "Outcome": Outcome})


Josh = HospitalRegistry('Daniel', 'Josh', 19, 'Male', ['Fever', 'Cough', 'Headache', 'Abdominal Pain'], 223345567, "2025-07-11 10:00AM", '50000', 'Follow-up')

print(Josh.check_in())
print(Josh.appointment(Josh.Appointment_time, Josh.Doctor_name, Josh.Patient_name))
print(Josh.discharge(Josh.Patient_name, Josh.Treatment_price, Josh.Outcome))
Josh.Registry(Josh.Doctor_name, Josh.Patient_name, Josh.age, Josh.sex, Josh.symptoms, Josh.Insurance_number, Josh.Appointment_time, Josh.Treatment_price, Josh.Outcome)
print(Josh.Hospital_registry)