import os 
import smtplib
from email.message import EmailMessage

#Configuração de login (e-mail e senha )

EMAIL = 'SEU E-MAIL'
SENHA = 'SENHA'

# criação do e-mail 

MENSAGEM = EmailMessage()
MENSAGEM['Subject'] = 'Lembrete, estudar para prova'
MENSAGEM['From'] = 'SEU E-MAIL'
MENSAGEM['To'] ='E-MAIL DE DESTINO'
MENSAGEM.set_content('Olá, venho lemprar para estudar para prova de estatística')

#Enviar o e-mail 
with smtplib.SMTP_SSL('smtp.account.proton.me, 465') as smtp:
    smtp.login(andersoncomercial@pm.me,d011819237f9bf4644073241beb21df7 )
    smtp.send_message(MENSAGEM)