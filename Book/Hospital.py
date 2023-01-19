days = int(input())
doctors = 7
treated_patient = 0
treated_patient_for_day = 0
untreated_patient = 0
untreated_patient_for_day = 0
for i in range(1, days + 1):
    if i % 3 == 0 and untreated_patient > treated_patient:
        doctors += 1
    patient = int(input())
    if patient < doctors:
        treated_patient_for_day = patient
    else:
        treated_patient_for_day = doctors
    treated_patient += treated_patient_for_day
    if patient > doctors:
        untreated_patient_for_day = patient - treated_patient_for_day
        untreated_patient += untreated_patient_for_day
print(f"Treated patients: {treated_patient}.")
print(f"Untreated patients: {untreated_patient}.")
