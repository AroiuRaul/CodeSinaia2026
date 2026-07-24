import socket

HOST="127.0.0.1"
PORT=5555
KEY="parola"

def xor_transform(data:bytes, key:str) -> bytes:
    key_bytes= key.encode("utf-8")
    return bytes(byte ^ key_bytes[i % len(key_bytes)] for i, byte in enumerate(data))

def encrypt(text:str, key:str) -> bytes:
    return xor_transform(text.encode("utf-8"), key)

def descrypt(sdata:bytes, key:str) -> str:
    return xor_transform(sdata, key).decode("utf-8")

def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        message= "Where is John Wick?"
        client_socket.sendall(encrypt(message, KEY))
        print(f"{message}")

    encrypted_response= client_socket.recv(4096)
    print("DECIDED message:", descrypt(encrypted_response, KEY))
    if __name__ == "__main__":
        main()