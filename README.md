# Implementação de SSL/TLS no Python [5]

É como um chat seguro e criptografado entre dois programas, onde um espera mensagens (servidor) e o outro permite enviar mensagens (cliente).
A parte do SSL/TLS garante que todas as mensagens trocadas entre eles sejam criptografadas, tornando a comunicação segura

---

No diretório da aplicação execute o comando abaixo para criacao do arquivo de chave e certificado

```sh
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt
```

> - Cria um par de chaves (pública/privada) usando RSA
> - Gera um certificado digital autoassinado válido por 1 ano
> - Salva a chave privada em 'server.key'
> - Salva o certificado público em 'server.crt'

---

## Execução

```sh
python server_ssl_tls.py
```

Este comando:

- Inicia o servidor na porta 8443
- Fica aguardando conexões de clientes
- Quando um cliente conecta, fica pronto - para receber mensagens

```sh
python client_ssl_tls.py
```

Este comando:

- Inicia o programa cliente
- Tenta conectar ao servidor
- Permite que você digite mensagens pelo - teclado
- Envia suas mensagens para o servidor

---

## Servidor (servidor_ssl_tls.py)

- Cria um servidor seguro usando SSL/TLS
- Fica escutando na porta 8443
- Quando recebe uma conexão, aceita mensagens do cliente
- Para cada mensagem recebida, envia uma confirmação de volta
- Usa certificados para garantir que a comunicação seja criptografada

## Cliente (cliente_ssl_tls.py)

- Conecta-se ao servidor de forma segura usando SSL/TLS
- Permite que o usuário digite mensagens pelo teclado
- Envia cada mensagem digitada para o servidor
- Mostra a resposta que recebe do servidor
- Continua até que o usuário digite 'sair'
