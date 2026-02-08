from twilio.rest import Client

# IMPORTANTE: Para usar este código, você precisa criar uma conta na Twilio,
# pegar seu SID e Token no console e configurar o WhatsApp Sandbox.

# Credenciais (Substitua pelos seus dados reais antes de rodar localmente)
conta_sid = "SEU_SID_AQUI"
token_twillio = "SEU_TOKEN_AQUI"
client = Client(conta_sid, token_twillio)

# Envio da mensagem
# O número 'from_' é o padrão do Twilio Sandbox.
# O número 'to' deve ser o número que enviou o 'join' para o Sandbox.
message = client.messages.create(
    from_="whatsapp:+14155238886", 
    to="whatsapp:+5511900000000", # Substitua pelo número de destino
    body="⚠️ ALERTA DE SEGURANÇA ⚠️\nBom dia, companheiro. Seu sistema foi acessado remotamente. Te hackeei! ;)"
)

print(f"Mensagem enviada! SID: {message.sid}")