patients_list = {
    'ahmad irfan': {
        'phone_number': 123456789,
        'gender': 'male',
        'disease': 'fever'
    },
    'ahmad ikram': {
        'phone_number': 123456789,
        'gender': 'male',
        'disease': 'stomache'
    },
    'mohammad shukri': {
        'phone_number': 123456789,
        'gender': 'male',
        'disease': 'headache'
    }
}

for patient_name, patient_info in patients_list.items():
    print(f"{patient_name.title()}'s Information")

    for info, descriptions in patient_info.items():
        print(f"- {info}: {descriptions}")


    print("\n")