import csv

# List of dictionaries
data = {
        "I0":{
            7: ['MCB TRIP', 'SUB-M + NF03', '3'],
            6: ['Q0 NOT OPEN', 'SUB-M + NF03', '2'],
            5: ['Q0 CLOSE', 'SUB-M + NF03', '2'],
            4: ['Q0 TRIP', 'SUB-M + NF03', '3'],
            3: ['U/V RELLAY NOT INCOMMING OPERATED', 'SUB-M + NF03', '2'],
            2: ['LUAC MCCB&MCB TRIP', 'SUB-M + NF03', '3'],
            1: ['', '', '0'],
            0: ['', '', '0'],
        }
        "I1":{
            7: ['DOOR OPEN', 'SUB-M', '1'],
            6: ['FIRE ALARM', 'SUB-M + FIRE ALARM', '3'],
            5: ['', '', '0'],
            4: ['', '', '0'],
            3: ['', '', '0'],
            2: ['', '', '0'],
            1: ['', '', '0'],
            0: ['', '', '0'],
        }
        "I2": {
            7: ['INVERTER FAIL', 'SUB-M + INVERTER', '3'],
            6: ['INVERTER OFF', 'SUB-M + INVERTER', '2'],
            5: ['SBS NOT OPERATION', 'SUB-M + INVERTER', '2'],
            4: ['MAINS NOT NORMAL', 'SUB-M + INVERTER', '2'],
            3: ['BATT NOT OK', 'SUB-M + INVERTER', '2'],
            2: ['AC FAIL', 'SUB-M + BATTERY CHARGER', '3'],
            1: ['DC HIGH', 'SUB-M + BATTERY CHARGER', '3'],
            0: ['ERTH FAULT', 'SUB-M + BATTERY CHARGER', '3'],
        }
        "I3" {
            7: ['WEAK BATTERY', 'SUB-M + BATTERY CHARGER', '3'],
            6: ['DC LOW', 'SUB-M + BATTERY CHARGER', '3'],
            5: ['TEMPERTURE HIGH', 'SUB-M + BATTERY CHARGER', '3'],
            4: ['REACTIFIER FAIL', 'SUB-M + BATTERY CHARGER', '3'],
            3: ['MCCB LOAD', 'SUB-M + BATTERY CHARGER', '2'],
            2: ['CURRENT NOT LIMIT TOTAL', 'SUB-M + BATTERY CHARGER', '2'],
            1: ['MCCB BATTERY', 'SUB-M + BATTERY CHARGER', '2'],
            0: ['', '', '0'],
        }
        "I4" {
            7: ['RELAY FAULTY / PROTECTION DC SUPPLY FAIL', 'SUB-M + JT1', '3'],
            6: ['TCS RELAY NOT OPERATED', 'SUB-M + JT1', '2'],
            5: ['LOCKOUT OPERATION', 'SUB-M + JT1', '2'],
            4: ['OC/EF/SEF PROTECTION TRIP', 'SUB-M + JT1', '3'],
            3: ['MOTOR DC SUPPLY FAIL', 'SUB-M + JT1', '3'],
            2: ['LOCAL POSITION', 'SUB-M + JT1', '2'],
            1: ['REMOTE POSITION', 'SUB-M + JT1', '2'],
            0: ['LINE ES NOT CLOSE', 'SUB-M + JT1', '2'],
        }
        "I5" {
            7: ['LINE ES OPEN', 'SUB-M + JT1', '3'],
            6: ['CB CLOSE POSITION', 'SUB-M + JT1', '2'],
            5: ['CB OPEN POSITION', 'SUB-M + JT1', '2'],
            4: ['NOT CB IN SERVICE', 'SUB-M + JT1', '2'],
            3: ['CB SPRING DISCHARGE', 'SUB-M + JT1', '2'],
            2: ['TR BUCH TRIP', 'SUB-M + JT1', '3'],
            1: ['TRB OIL TEMPTRIP', 'SUB-M + JT1', '3'],
            0: ['MECH TRIP FROM LV SIDE', 'SUB-M + JT1', '3'],
        }
        "I6" {
            7: ['RELAY FAULTY / PROTECTION DC SUPPLY FAIL', 'SUB-M + JT2', '3'],
            6: ['TCS RELAY NOT OPERATED', 'SUB-M + JT2', '2'],
            5: ['LOCKOUT OPERATION', 'SUB-M + JT2', '2'],
            4: ['OC/EF/SEF PROTECTION TRIP', 'SUB-M + JT2', '3'],
            3: ['MOTOR DC SUPPLY FAIL', 'SUB-M + JT2', '3'],
            2: ['LOCAL POSITION', 'SUB-M + JT2', '2'],
            1: ['REMOTE POSITION', 'SUB-M + JT2', '2'],
            0: ['LINE ES NOT CLOSE', 'SUB-M + JT2', '2'],
        }
        self.I7 = {
            7: ['LINE ES OPEN', 'SUB-M + JT2', '3'],
            6: ['CB CLOSE POSITION', 'SUB-M + JT2', '2'],
            5: ['CB OPEN POSITION', 'SUB-M + JT2', '2'],
            4: ['NOT CB IN SERVICE', 'SUB-M + JT2', '2'],
            3: ['CB SPRING DISCHARGE', 'SUB-M + JT2', '2'],
            2: ['TR BUCH TRIP', 'SUB-M + JT2', '3'],
            1: ['TRB OIL TEMPTRIP', 'SUB-M + JT2', '3'],
            0: ['MECH TRIP FROM LV SIDE', 'SUB-M + JT2', '3'],
        }
        self.I8 = {
            7: ['RELAY FAULTY / PROTECTION DC SUPPLY FAIL', 'SUB-M + JL1+J', '3'],
            6: ['TCS RELAY NOT OPERATED', 'SUB-M + JL1+J', '2'],
            5: ['LOCKOUT OPERATION', 'SUB-M + JL1+J', '2'],
            4: ['OC/EF/SEF PROTECTION TRIP', 'SUB-M + JL1+J', '3'],
            3: ['MOTOR DC SUPPLY FAIL', 'SUB-M + JL1+J', '3'],
            2: ['LOCAL POSITION', 'SUB-M + JL1+J', '2'],
            1: ['REMOTE POSITION', 'SUB-M + JL1+J', '2'],
            0: ['LINE ES NOT CLOSE', 'SUB-M + JL1+J', '2'],
        }
        self.I9 = {
            7: ['LINE ES OPEN', 'SUB-M + JL1+J', '3'],
            6: ['CB CLOSE POSITION', 'SUB-M + JL1+J', '2'],
            5: ['CB OPEN POSITION', 'SUB-M + JL1+J', '2'],
            4: ['NOT CB IN SERVICE', 'SUB-M + JL1+J', '2'],
            3: ['CB SPRING DISCHARGE', 'SUB-M + JL1+J', '2'],
            2: ['CONTROL DC SUPPLY FAIL', 'SUB-M + JL1+J', '3'],
            1: ['VT FUSE FAIL', 'SUB-M + JL1+J', '3'],
            0: ['VT MCB FAIL', 'SUB-M + JL1+J', '3'],
        }
}

# CSV file path
csv_file = 'data.csv'

# Flatten the dictionaries into a list of rows
rows = []
for key, inner_dict in data.items():
    for inner_key, inner_values in inner_dict.items():
        row = [key, inner_key] + inner_values
        rows.append(row)

# List of fieldnames (column headers)
fieldnames = ['Dictionary', 'Index', 'Value1', 'Value2', 'Value3']

# Write the data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(fieldnames)

    # Write the data rows
    writer.writerows(rows)

print(f"Data has been written to '{csv_file}'.")
