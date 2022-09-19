## Travis CI with PostgreSQL

### 1) Install Travis CI and select the GitHub repository
https://app.travis-ci.com/account/repositories

### 2) Clone and run the project

Clone the repository
```console
git clone https://github.com/alexdecastro/travis_ci_demo.git
```

Create and activate a virtual environment
```console
python -m venv env
source env/bin/activate
```

Install the Django and psycopg2 packages using requirements.txt
```console
pip install -r ./travis_ci_demo/requirements.txt
```

Run the project
```console
cd travis_ci_demo
python manage.py runserver
```
