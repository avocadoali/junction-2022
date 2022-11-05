{'atr': 
    {'atr': '3B 6E 00 00 80 31 80 66 B0 84 0C 01 6E 01 83 00 90 00', 
    'atrFlag': False, 
    'atrID': ''}, 


'name': 'CARD/S-E VISA DB ONL ACP  ', 
'number': '43 18 71 19 91 39 94 79', 
'effectiveDate': '28/11/2016', 
'expirationDate': '30/11/2019', 
'currency': 'Euro', 
'country': 'The Republic of Finland', 
'log': [
    {'amount': '0.01', 'date': '09/09/2021', 'currency': 'Euro'}, {'amount': '0.55', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.11', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '5.55', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.01', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.11', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.01', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.06', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '1.23', 'date': '19/02/2021', 'currency': 'Euro'}, {'amount': '30.00', 'date': '16/01/2020', 'currency': 'Euro'}]}



# flask-template


Flask backend boilerplate code template

## Setup

1. Clone this repo into a directory
2. Create a virtual environment

```shell
python3 -m venv <NAME_OF_ENVIRONMENT>
```

3. Activate virtual environment

```shell
source <NAME_OF_ENVIRONMENT>/bin/activate
```

4. Install requirements

```shell
pip3 -r install requirements.txt
```

5. Start dev server

```shell
pip3 -m flask run
```

- http://127.0.0.1:5000 should display the Hello World message
- http://127.0.0.1:5000/YOUR_NAME should display a greeting message

## Usage

- always activate virtual environment when installing packages etc
- save packages in requirements.txt using `pip freeze > requirements.txt`
