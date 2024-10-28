import firebase_admin
from firebase_admin import credentials, firestore
import json
import streamlit as st

# Use the following when deploy to streamlit####################
# Load Firebase credentials from Streamlit secrets
firebase_credentials_json = st.secrets["firebase"]["FIREBASE_CREDENTIALS"]

# Parse the credentials
firebase_credentials = json.loads(firebase_credentials_json)

# Initialize Firebase
cred = credentials.Certificate(firebase_credentials)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
##############################################################
# Initialize Firestore client
db = firestore.client()

#%%
# Zakah-Expenses database

# Function to add a document to the "zakah-pay" collection
def insert_period(name, date, transaction, value, comment):
    doc_ref = db.collection("zakah-pay").document(name)  # Using 'name' as the document ID
    doc_ref.set({
        "key": name,
        "date": date,
        "transaction": transaction,
        "value": value,
        "comment": comment
    })

# Function to fetch all documents in the "zakah-pay" collection
def fetch_all_periods():
    """Fetches all documents in the zakah-pay collection"""
    docs = db.collection("zakah-pay").stream()
    return [doc.to_dict() for doc in docs]

# Function to get a single document from the "zakah-pay" collection by name
def get_period(name):
    """Fetches a single document from zakah-pay by name"""
    doc = db.collection("zakah-pay").document(name).get()
    return doc.to_dict() if doc.exists else None

# Function to delete a document from the "zakah-pay" collection by name
def delete_period(name):
    """Deletes a document from zakah-pay by name"""
    db.collection("zakah-pay").document(name).delete()

# Function to get all period names from the "zakah-pay" collection
def get_all_periods():
    items = fetch_all_periods()
    return [item["name"] for item in items] if items else []

#%%
# User database functions using the "users-zakah" collection
def insert_user(username, name, password):
    """Inserts a user document into the users-zakah collection"""
    doc_ref = db.collection("users-zakah").document(username)
    doc_ref.set({
        "key": username,
        "name": name,
        "password": password
    })
    return doc_ref.get().to_dict()

def fetch_all_users():
    """Fetches all user documents from users-zakah collection"""
    docs = db.collection("users-zakah").stream()
    return [doc.to_dict() for doc in docs]

def get_user(username):
    """Fetches a user document from users-zakah by username"""
    doc = db.collection("users-zakah").document(username).get()
    return doc.to_dict() if doc.exists else None

def update_user(username, updates):
    """Updates a user document in the users-zakah collection"""
    db.collection("users-zakah").document(username).update(updates)

def delete_user(username):
    """Deletes a user document from the users-zakah collection"""
    db.collection("users-zakah").document(username).delete()

#%%
# Families database who benefit from the zakah program
def insert_family(name, category, payment, date, phone, comment):
    doc_ref = db.collection("families-zakah").document(name)  # Using 'name' as the document ID
    doc_ref.set({
        "key": name,
        "category": category,
        "payment": payment,
        "date": date,
        "phone": phone,
        "comment": comment
    })

# Function to fetch all documents in the "families-zakah" collection
def fetch_all_families():
    """Fetches all documents in the families-zakah collection"""
    docs = db.collection("families-zakah").stream()
    return [doc.to_dict() for doc in docs]

# Function to get a single document from the "families-zakah" collection by name
def get_family(name):
    """Fetches a single document from families-zakah by name"""
    doc = db.collection("families-zakah").document(name).get()
    return doc.to_dict() if doc.exists else None

# Function to delete a document from the "families-zakah" collection by name
def delete_family(name):
    """Deletes a document from families-zakah by name"""
    db.collection("families-zakah").document(name).delete()

# Function to get all period names from the "zakah-pay" collection
def get_all_families():
    items = fetch_all_periods()
    return [item["name"] for item in items] if items else []

#%%
