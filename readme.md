# Django & Stripe Integration 
Payment gateway integration with django backend and stripe as the payment gateway


## Setting up
- Create a virtual environment and install dependencies
- Create a .env file in `stripedjango` directory
- Copy the contents of .env-example file and add the Stripe API keys 


## Images
![](./screenshots/home.png)

## Development Environment 
- For frontend we are using tailwind-css with typical html/css/js setup (no frameworks used yet)

### Steps 
- Clone this repository & and move into the repository
- Install python3 (you may have it already)
- Create a virtual environment 
```bash
python3 -m venv venv
```
- Activate venv with `source ./venv/scripts/activate`
- Install dependencies 
```bash
pip install -r requirements.txt
```
- Install tailwind with npm 
```
npm install
```
- now do the django thing 
```
python3 manage.py makemigrations 
python3 manage.py migrate 
python3 manage.py runserver
```
- out of those three commands you can figure it out which one is "running the server" the rest 2 are used to create tables and setup the database.


## Contributing 
- Create issues before working a pull request, discuss it and then we can start working 
- This code is free for use under Apache License Version 2.0
