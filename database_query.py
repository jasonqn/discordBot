import pymongo
import config
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the Oauth class
clientObj = config.Oauth()

# Get the database connection from the Oauth class
client = clientObj.databaseCONN()

# Access the dnd database and the login collection
db = client.dnd
collection = db.login

# Sample document to insert
user_details = {
    "user_id": "123456789",
    "username": "example_user"
}

# Insert the document into the collection
result = collection.insert_one(user_details)

# Print the result of the insertion
print(f"Inserted document with id: {result.inserted_id}")
