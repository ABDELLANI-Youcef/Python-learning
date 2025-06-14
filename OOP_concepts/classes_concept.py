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
  return

if __name__ == "__main__":
  main()