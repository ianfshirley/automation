import re


with open("assets/potential-contacts.txt", "r") as f:
    text_from_file = f.read()


# regex patterns

phone_pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


# Format the phone numbers

phone_numbers = re.findall(phone_pattern, text_from_file)
# remove duplicates
non_duplicate_phone_numbers = list(dict.fromkeys(phone_numbers))
# sort in ascending order
sorted_phone_numbers = sorted(non_duplicate_phone_numbers)
# remove non-numerical characters
joined_phone_numbers = [re.sub('[^0-9]', '', num) for num in sorted_phone_numbers]
# insert hyphens to separate the phone numbers into this format: xxx-xxx-xxxx
formatted_phone_numbers = []
for num in joined_phone_numbers:
  formatted_phone_numbers.append(num[:3] + "-" + num[3:6] + "-" + num[6:])
# insert new line between each phone number
phone_nums_to_print = '\n'.join(formatted_phone_numbers)

# format emails

email_addresses = re.findall(email_pattern, text_from_file)
# remove duplicates
non_duplicate_email_addresses = list(dict.fromkeys(email_addresses))
# sort in ascending order
sorted_email_addresses = sorted(non_duplicate_email_addresses)
# insert new line between each email address  
email_addys_to_print = '\n'.join(sorted_email_addresses)


# write to new files

with open("./assets/phone_numbers.txt", "w") as new_file:
  new_file.write(str(phone_nums_to_print))

with open("./assets/email_addresses.txt", "w") as new_file:
  new_file.write(str(email_addys_to_print))



