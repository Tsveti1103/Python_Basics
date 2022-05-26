days = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7
treated_patients_for_day = 0
for days_count in range(1, days + 1):
    patients_count = int(input())
    if days_count % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patients_count <= doctors:
        treated_patients += patients_count
    else:
        treated_patients_for_day = doctors
        treated_patients += treated_patients_for_day
        untreated_patients += patients_count - treated_patients_for_day

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
