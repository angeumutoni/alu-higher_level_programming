class Patient:
  def __init__(self, id, name, age, gender, admission_date, condition):
    self.id = id
    self.name = name
    self.age= age
    self.gender = gender
    self.admission_date = admission_date
    self.condition = condition
  def get_details(self):
  return f"ID: {self.id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nAdmission Date:{self.admission_date}\nCondition: {self.condition}
  patient1 = Patient(1, "Allan MUGISHA", 20, "Male", "2024-01-09", "Marburg")
  patient2 = Patient(2, "Jesse Kisaale WALUSANSA", 25, "Male", "2024-10-12", "Headache")
  patient3 = Patient(3, "Chris HIRWA", 23, "Male", "2024-12-08", "Flu")
  patient4 = Patient(4, "Arsene KABASINGA", 30, "Male", "2024-10-12", "Bleeding knee")
  patient5 = Patient(5, "Allen KANSIME", 12, "Female", "2024-01-09", "Vaccination")
  patient6 = Patient(6, "Ines UMUHOZA", 25, "Female", "2024-10-12", "Headache")
  
patients = [patient1, patient2, patient3, patient4, patient5, patient6]
