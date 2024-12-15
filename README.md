# have-i-been-pwned

Check if passwords have been leaked using the free password API from [haveibeenpwned.com](haveibeenpwned.com)

## Usage
```
usage: check_passwords.py [-h] [--csv] [--csv-column CSV_COLUMN] input
```

You can either pass a plain-text password or a CSV file
```
python3 check_passwords.py 12345678
Password '12345678' has been leaked.
```

```
python3 check_passwords.py --csv --csv-column 0 ~/exported_password.csv 
Password '12345678' has been leaked.
Password 'password' has been leaked.
```
