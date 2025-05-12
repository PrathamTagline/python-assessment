import re
pattern =  r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"

emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", "nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@exter123.123", "fake@fake123.fakercom"]
validEmail = []
for email in emails:
    if re.fullmatch(pattern,email):
        validEmail.append(email)

print(validEmail)