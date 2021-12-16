import requests
import json

def characters():
    response = requests.get("http://hp-api.herokuapp.com/api/characters")
    if response.status_code != 200:
        return False
    characters = response.json()
    return characters

def students():
    response = requests.get("http://hp-api.herokuapp.com/api/characters/students")
    if response.status_code != 200:
        return False
    h_students = response.json()
    return h_students

def staff():
    response = requests.get("http://hp-api.herokuapp.com/api/characters/staff")
    if response.status_code != 200:
        return False
    h_staff = response.json()
    return h_staff

def characters_classified(house):
    response = requests.get(f"http://hp-api.herokuapp.com/api/characters/house/{house}")
    if response.status_code != 200:
        return False
    h_classified = response.json()
    return h_classified