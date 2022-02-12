import re
import shutil

def phone_validator():
  content = open('assets/potential-contacts.txt', 'r').read()
  with open('phone_numbers.txt', 'w+') as f:
    phone_numbers = re.findall(r'[0-9-+x.()]{7,}', content)
    formatted_numbers = []
    for number in phone_numbers:
      numbers = number.replace(".", "").replace("-", "").replace("(", "").replace(")", "").replace("+", "")
      if len(numbers) > 10:
        formatted_numbers.append(numbers[:3] + "-" + numbers[3:6]+"-" + numbers[6:10])
      elif len(numbers) < 7:
        formatted_numbers.append("206" + "-" + numbers[0:3]+"-" + numbers[3:7])
    formatted_numbers.sort()
    
    for n in formatted_numbers: 
      f.write(n + "\n")
  
  
def email_validator():
  content = open('assets/potential-contacts.txt', 'r').read()
  with open('emails.txt', 'w+') as f:
    emails = re.findall(r'\S+@\S+', content)
    emails.sort()
    for n in emails: 
      f.write(n + "\n")

email_validator()
phone_validator()
  