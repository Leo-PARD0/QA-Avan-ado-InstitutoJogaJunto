# language: pt
Funcionalidade: Enviar mensagem pelo whatsapp.
    Cenário: Logar no whatsapp
        Dado que o usuário está com o micronsoft edge aberto
        E com a página do whatsapp aberta
        Quando o usuário Logar
        E encontrar o grupo de mensagem
        Então a mensagem será editada e enviada