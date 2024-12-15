# have-i-been-pwned

Check if passwords have been leaked using the free password API from [haveibeenpwned.com](haveibeenpwned.com).

## Setup
It is recommended to use a virtual environment, or [pyenv](https://github.com/pyenv/pyenv).
```
pip install -r requirements.txt
```

## Usage
```
usage: check_passwords.py [-h] [--csv] [--csv-column CSV_COLUMN] input
```

You can either pass a plain-text password:
```
python3 check_passwords.py 12345678
Password '12345678' has been leaked.
```

Or input a CSV file:
```
python3 check_passwords.py --csv --csv-column 0 ~/exported_password.csv 
Password '12345678' has been leaked.
Password 'password' has been leaked.
```
