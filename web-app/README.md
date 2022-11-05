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
