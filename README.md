# my-igs

## Installation

0. You must ppdate Python into 3.12.0 version

   Download here : https://www.python.org/downloads/

1. HTTPS Clone the repository:

   
   ```bash
   git clone https://github.com/azharnian/my-igs.git
   
2. or SSH Clone the repository:
   ```bash
   git clone git@github.com:azharnian/my-igs.git 
   

3. Change into the directory
    ```bash
    cd your-flask-app


4. Create environtment
    ```bash
    python -m venv venv

5. Activate On Bash Windows

    ```bash
    source venv\Scripts\activate

6. Or Activate On Mac/Linux

    ```bash
    source venv/bin/activate

7. Update your pip

    ```bash
    pip install --upgrade pip

8. Install the required depedencies

    ```bash
    pip install -r requirements.txt

9. Create .env file in folder project

    ```bash
    touch .env

10. Ask code owner for .env content and configuration

11. Run the app

    ```bash
    python app.py

12. Or run using flask

    ```bash
    flask run


## Database Update

If the database / model had been updated or there were some changes, please do the database migration.

0. Run Migration

    ```bash
    flask db migrate -m "Your message about changes"
    flask db upgrade