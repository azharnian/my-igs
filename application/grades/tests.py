# IMPORT NECESSARY MODULE AND RUN USING PYTEST
# RUN TESTING : pytest tests.py
# REPORT YOUR TESTING IN FOLDER reports : pytest --html=reports/report-<module/route-name>.html

# EXAMPLE - SIMPLE FUNCTION / MODULE TESTING
# from math import sqrt
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# def test_prime():
#     assert is_prime(2) == True
#     assert is_prime(3) == True
#     assert is_prime(4) == False
#     assert is_prime(5) == True
#     assert is_prime(6) == False
#     assert is_prime(7) == True
#     assert is_prime(8) == False
#     assert is_prime(9) == False
#     assert is_prime(10) == False

#EXAMPLE - ROUTE TESTING
# test_app.py
# from application import create_app
# import pytest
# app = create_app()

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     client = app.test_client()
#     yield client

# def test_home_route(client):
#     response = client.get('/')
#     assert response.status_code == 200

# def test_another_route(client):
#     response = client.get('/another')
#     assert response.status_code == 200
#     assert b'Some expected content' in response.data

#EXAMPLE - MODEL TESTING
# test_app.py
# import pytest
# from application import create_app
# app = create_app()
# from application.achievements.models import *

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#     client = app.test_client()

#     with app.app_context():
#         db.create_all()

#     yield client

# def test_index_route(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b'Hello, World!' in response.data

# def test_user_model(client):
#     # Create a user
#     user = User(username='test_user')
#     user.save()

#     # Retrieve the user
#     retrieved_user = User.query.filter_by(username='test_user').first()
    
#     # Test that the user was successfully added to the database
#     assert retrieved_user is not None
#     assert retrieved_user.username == 'test_user'
