# Envio de e-mail
Envio  Automático de E-mail utilizando Python.

```python 

import os 
import smtplib
from email.message import EmailMessage

#Configuração de login (e-mail e senha )

EMAIL = 'SEU E-MAIL'
SENHA = 'SUA SENHA'

# criação do e-mail 

MENSAGEM = EmailMessage()
MENSAGEM['Subject'] = 'Lembrete, estudar para prova'
MENSAGEM['From'] = 'SEU E-MAIL'
MENSAGEM['To'] ='E-MAIL DE DESTINO'
MENSAGEM.set_content('Olá, venho lemprar para estudar para prova de estatística')

#Enviar o e-mail 
with smtplib.SMTP_SSL('smtp.provedordeemail, 465') as smtp:
    smtp.login(SEU E-MAIL, SUA SENHA )
    smtp.send_message(MENSAGEM)
    
