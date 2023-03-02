# Envio de e-mail
Envio  Automático de E-mail utilizando Python.

```python 
import os
import smtplib
from email.message import EmailMessage

# Configurações de login (e-mail e senha)
email = 'SEU E-MAIL'
senha = 'SUA SENHA'

# Criação da mensagem de e-mail
mensagem = EmailMessage()
mensagem['Subject'] = 'Lembrete, estudar para a prova'
mensagem['From'] = email
mensagem['To'] = 'E-MAIL DE DESTINO'
mensagem.set_content('Olá, venho lembrá-lo de estudar para a prova de estatística')

# Envio da mensagem de e-mail
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, senha)
        smtp.send_message(mensagem)
        print("E-mail enviado com sucesso!")
except Exception as e:
    print("Não foi possível enviar o e-mail: ", e)
