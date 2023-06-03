from hashlib import sha256

HASHING_ALGORITHMS = {
    "SHA_256": sha256
}

def encode_string(string: str, algorithm: type) -> str:
    return algorithm(string.encode()).hexdigest()


def check_password(u_input: str, algorithm: type) -> bool:
    PASSWORD = encode_string("LIGMA")
    return([True if (PASSWORD == encode_string(u_input, algorithm)) else False])


def call_manager(command: dict, string: str):
    if command == encode_string:
        encode_string(string, "sha256")
    if command == check_password:
        check_password(string, "sha256")
