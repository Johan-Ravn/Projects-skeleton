import pickle
from create_user import createUserFromInput

def DBInsert() -> None:
    user = str(createUserFromInput())  # Convert the user object to a string
    
    try:
        with open("src/DB/database.txt", "a") as file:
            file.write(user)
            file.write('\n')  # Add a new line after each user entry
        print("Data inserted successfully.")
    except IOError as error:
        print(f"Error occurred while inserting into the file: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

DBInsert()
