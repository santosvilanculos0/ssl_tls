# servidor_ssl.py
import socket
import ssl


def criar_servidor_ssl():
    # Configuração do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8443))
    server_socket.listen(5)

    # Configuração do contexto SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("server.crt", "server.key")

    print("Servidor iniciado. Aguardando conexões...")

    while True:
        try:
            # Aceita conexões
            client_socket, addr = server_socket.accept()
            print(f"Conexão recebida de {addr}")

            # Wrap do socket com SSL
            ssl_socket = context.wrap_socket(client_socket, server_side=True)

            while True:
                try:
                    # Recebe dados
                    data = ssl_socket.recv(1024).decode()
                    if not data:
                        print("Cliente desconectado.")
                        break

                    print(f"Mensagem recebida: {data}")

                    # Envia resposta
                    response = f"Servidor recebeu: {data}"
                    ssl_socket.send(response.encode())

                except Exception as e:
                    print(f"Erro na comunicação: {e}")
                    break

            # Fecha conexão
            ssl_socket.close()

        except Exception as e:
            print(f"Erro na conexão: {e}")
            continue


if __name__ == "__main__":
    criar_servidor_ssl()
