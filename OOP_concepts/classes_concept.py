class Developer:
  developers_count = 0 # thisis a static variable shared by all instances

  #constructor
  def __init__(self, name, languege, experience):
    self.name = name
    self.languege = languege
    self.experience = experience
    Developer.developers_count += 1  # Increment the count of developers

  @staticmethod
  def validate_email(email):
    return "@" in email and "." in email.split("@")[-1]

  def into(self):
    return f"Name: {self.name}, Language: {self.languege}, Experience: {self.experience} years"

  def evaluate(self, compared_to):
    if self.experience < compared_to:
      return "Junior Developer"
    elif compared_to <= self.experience < compared_to +10:
      return "Mid-level Developer"
    else:
      return "Senior Developer"

class SeniorDeveloper(Developer):
  def __init__(self, name, language, experience, company):
    super().__init__(name, language, experience)
    self.company = company

  def into(self):
    return f"{super().into()}, Company: {self.company}"

  def anounce(self):
    return f"{self.name} is a Senior Developer at {self.company} with {self.experience} years of experience in {self.languege}."

def main():
  youcef = Developer("Youcef", "Python", 5)
  print(youcef.into())
  # Output: Name: Youcef, Language: Python, Experience: 5 years
  print(f"{youcef.name} is a developer with {youcef.experience} years of experience in {youcef.languege}.\n")
  print(f"Total developers: {Developer.developers_count} developers.")

  youcef.experience = 11
  print(f"Nom, after 6 years {youcef.name} is a developer with {youcef.experience} years of experience in {youcef.languege}.")

  print(f"{youcef.name} is a {youcef.evaluate(5)} compared to a developer with 5 years of experience.\n")

  ahmed = Developer("Ahmed", "JavaScript", 3)

  print(f"But now we have total developers: {Developer.developers_count} developers.")
  print(ahmed.into())
  # Output: Name: Ahmed, Language: JavaScript, Experience: 3 years
  print(f"{ahmed.name} is a developer with {ahmed.experience} years of experience in {ahmed.languege}.")

  # a demonstration of the static method
  email = ("youcefabdellani@gmail.com", "fefe")

  for e in email: print(f"{e} is a {"valid" if Developer.validate_email(e) else "invalid"} email")

  super_developer = SeniorDeveloper("Super Youcef", "Python", 10, "Groups360")

  print(f"this is an into for {super_developer.name}:\n{super_developer.into()}")

  print(super_developer.anounce())

  return

if __name__ == "__main__":
  main()