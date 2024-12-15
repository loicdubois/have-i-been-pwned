import hashlib
import requests
import csv
import argparse

def check_password_leak(password):
    # Get the SHA-1 hash of the password
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # The API will return a list of hashes that match the first 5 characters of the hash
    url = "https://api.pwnedpasswords.com/range/" + sha1_password[:5]
    response = requests.get(url)
    
    if response.status_code == 200 and sha1_password[5:] in response.text:
        print(f"Password '{password}' has been leaked.")
    # else:
    #     print(f"Password '{password}' is safe.")

def check_passwords_from_csv(file_path, password_column):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            password = row[password_column]
            check_password_leak(password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if passwords have been leaked.")
    parser.add_argument("input", help="Password or path to a CSV file containing passwords.", type=str, default="")
    parser.add_argument("--csv", help="Flag to indicate that the input is a CSV file.", action="store_true")
    parser.add_argument("--csv-column", help="Column number containing the passwords.", type=int, default=0)
    
    args = parser.parse_args()
    
    if args.csv:
        check_passwords_from_csv(args.input, args.csv_column)
    else:
        check_password_leak(args.input)