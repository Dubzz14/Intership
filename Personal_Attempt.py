import uuid

class HospitalRegistry:
    
    Hospital_registry = []

    def __init__(self, Doctor_name, Patient_name, age, sex, symptoms, Insurance_number, Appointment_time, Treatment_price, Outcome):
        self.Patient_ID = str(uuid.uuid4())
        self.Doctor_name = Doctor_name
        self.Patient_name = Patient_name
        self.age = age
        self.sex = sex
        self.symptoms = symptoms
        self.Insurance_number = Insurance_number
        self.Appointment_time = Appointment_time
        self.Treatment_price = Treatment_price
        self.Outcome = Outcome
        self.discharged = False


    def check_in(self):
        feel_ill = input(f"Does {self.Patient_name} feel ill?  (yes/no): ").lower()
        if feel_ill == "yes":
            print(f"{self.Patient_name}, you should fill in the form before seeing a doctor for treatment.")
            self.Patient_name = input("Enter your name: ")
            self.sex = input("Enter your sex: ")
            self.age = input("Enter your age: ")
            self.symptoms = input("Enter your symptoms (separated by commas): ").split(',')
            self.Insurance_number = input("Enter your Insurance number: ")

            self.Registry()
        else:
            print(f"{self.Patient_name} does not need to see a doctor right now.")
            

    def appointment(self):
        emergency_treatment = input("Were you brought in from Emergency?  (yes/no): ").lower()
        if emergency_treatment == "yes":
            print("We'll call a doctor to attend to you now.")
        else:
            print(f"{self.Patient_name}, your appointment has been booked for {self.Appointment_time} with Doctor {self.Doctor_name}")

        self.Registry()

    def discharge(self):
        if self.Outcome in ["Recovery", "Follow-up"]:
            self.discharged = True
            print(f"{self.Patient_name} has been discharged.")
            print(f"This is the price for your treatment: {self.Treatment_price}")
        else:
            self.discharged = False
            print("I'm sorry for your loss.")
            print(f"This is the price for your treatment: {self.Treatment_price}")
        
        self.Registry() 

    def Registry(self):
        found = False
        for entry in self.Hospital_registry:
            if entry ["Patient ID"] == self.Patient_ID:
                entry.update({"Doctor Name": self.Doctor_name, "Age": self.age, "Sex": self.sex, "Symptoms": self.symptoms, "Appointment time": self.Appointment_time, "Treatment Price": self.Treatment_price, "Outcome": self.Outcome})
                found = True
                break
        if not found:
            HospitalRegistry.Hospital_registry.append({"Patient ID": self.Patient_ID, "Doctor Name": self.Doctor_name, "Patient Name": self.Patient_name, "Age": self.age, "Sex": self.sex, "Symptoms": self.symptoms, "Insurance Number": self.Insurance_number, "Appointment time": self.Appointment_time, "Treatment Price": self.Treatment_price, "Outcome": self.Outcome})


Josh = HospitalRegistry('Daniel', 'Josh', 19, 'Male', ['Fever', 'Cough', 'Headache', 'Abdominal Pain'], 223345567, "2025-07-11 10:00AM", '50000', 'Follow-up')

Josh.check_in()
Josh.appointment()
Josh.discharge()

print("\n📋 Final Hospital Registry:")
for record in Josh.Hospital_registry:
    for key, value in record.items():
        print(f"{key}: {value}")
    print("-" * 30)
