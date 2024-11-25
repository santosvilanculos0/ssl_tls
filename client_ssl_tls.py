# cliente_ssl.py
import socket
import ssl


def criar_cliente_ssl():
    # Configuração do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configuração do contexto SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations("server.crt")
    context.check_hostname = False  # Desabilita verificação de hostname para teste

    try:
        # Conecta ao servidor
        ssl_socket = context.wrap_socket(client_socket, server_hostname="localhost")
        ssl_socket.connect(("localhost", 8443))

        print("Conectado ao servidor!")
        print("Digite suas mensagens (digite 'sair' para encerrar):")

        while True:
            try:
                # Recebe input do usuário
                message = input("Mensagem: ")

                if message.lower() == "sair":
                    print("Encerrando conexão...")
                    break

                # Envia mensagem
                ssl_socket.send(message.encode())

                # Recebe resposta
                response = ssl_socket.recv(1024).decode()
                print(f"Resposta do servidor: {response}")

            except Exception as e:
                print(f"Erro ao enviar/receber mensagem: {e}")
                break

        # Fecha conexão
        ssl_socket.close()

    except Exception as e:
        print(f"Erro na conexão: {e}")


if __name__ == "__main__":
    criar_cliente_ssl()
