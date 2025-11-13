# language: pt
Funcionalidade: Acessar Mercado Livre e encontrar um notebook barato.
    Cenário: Encontrar notebook:
        Dado que o usuário está no Microsoft Edge e acessou o Mercado Livre na página de notebooks
        Quando o usuário ordenar por menor preço
        E listar os 5 notebooks mais baratos
        Então o sistema retornará a opção mais barata