
from cryptographic import encode_string, check_password

def menu() -> None:
    print(
        "You have two choices:\n"
        "1. Encode a string\n"
        "2. Check if a string matches an encoding\n\n"

        "To access the choices follow this command:\n"
        "[command] [string] \n"
        "command = encode, match, quit\n"
    )


COMMANDS_PARAMETERLESS = {
    "menu": menu,
    "help": help,
}

COMMANDS_STRING_PARAMETER = {
    "encode": encode_string,
    "check_password": check_password
}

DEFAULT_ENCODING = "SHA_256"

def input_validation(u_input: str) -> None:
    if len(u_input) <= 0:
        return

def string_dissasembly(string: str):
    string_parts = string.split(' ')
    command = string_parts[0].strip().lower()
    expression = ''.join(string_parts[1:]) if len(string_parts) > 1 else None
    
    if command in COMMANDS_PARAMETERLESS.keys():
        call_func = COMMANDS_PARAMETERLESS[command]
        call_func()
    if command in COMMANDS_STRING_PARAMETER.keys():
        call_func = COMMANDS_STRING_PARAMETER[command]
        call_func(expression, "SHA_256")
    
def main(*args, **kwargs):
    while True:
        string_dissasembly(input("Input:"))

if __name__ == "__main__":
    main()
