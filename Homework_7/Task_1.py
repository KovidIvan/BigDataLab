raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE " 

user_data = raw_user_record.split(';')

strip_data = [s.strip() for s in user_data]

strip_data[0] = "UID-" + strip_data[0]

strip_data[1] = strip_data[1].replace('_', ' ').title()

strip_data[2] = strip_data[2].upper()

strip_data[3] = strip_data[3].lower()

result = " | ".join(strip_data)

print(result)
