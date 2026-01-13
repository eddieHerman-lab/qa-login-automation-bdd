# language: pt

Funcionalidade: Autenticação no SauceDemo
    Como um usuário do e-commerce
    Quero realizar login no sistema
    Para acessar a lista de produtos

    Cenário: Login com sucesso
        Dado que estou na página de login do "https://www.saucedemo.com/"
        Quando preencho o campo de usuário com "standard_user"
        E preencho o campo de senha com "secret_sauce"
        E clico no botão de entrar
        Então devo ser redirecionado para a vitrine de produtos

    Cenário: Tentativa de login com senha inválida
        Dado que estou na página de login do "https://www.saucedemo.com/"
        Quando preencho o campo de usuário com "standard_user"
        E preencho o campo de senha com "senha_errada_teste"
        E clico no botão de entrar
        Então devo visualizar a mensagem de erro "Epic sadface: Username and password do not match"