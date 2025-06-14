class Developer:
  def __init__(self, name, languege, experience):
    self.name = name
    self.languege = languege
    self.experience = experience

  def into(self):
    return f"Name: {self.name}, Language: {self.languege}, Experience: {self.experience} years"

def main():
  youcef = Developer("Youcef", "Python", 5)
  print(youcef.into())
  # Output: Name: Youcef, Language: Python, Experience: 5 years
  print(f"{youcef.name} is a developer with {youcef.experience} years of experience in {youcef.languege}.")

  youcef.experience = 11
  print(f"Nom, after 6 years {youcef.name} is a developer with {youcef.experience} years of experience in {youcef.languege}.")

  ahmed = Developer("Ahmed", "JavaScript", 3)
  print(ahmed.into())
  # Output: Name: Ahmed, Language: JavaScript, Experience: 3 years
  print(f"{ahmed.name} is a developer with {ahmed.experience} years of experience in {ahmed.languege}.")
  return

if __name__ == "__main__":
  main()