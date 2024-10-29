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
