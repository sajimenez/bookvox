# bookvox
Find information about your favorite books

## How to use (Windows OS example)?

1. Clone this repo on your local machine:
    ```
    git clone https://github.com/sajimenez/bookvox.git
    ```

2. Create virtual environment inside the project's root folder:
    ```
    python -m venv venv
    ```

3. Activate virtual environment:
    ```
    venv\scripts\activate
    ```

4. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Create database:
    ```
    python manage.py migrate
    ```

6. Run web scraping command:
    ```
    python manage.py runscraper
    ```

7. Run development server:
    ```
    python manage.py runserver
    ```

8. Create a test user, for example:
    ```
    python manage.py createsuperuser
    ```

9. You are ready to consume our webservices!
