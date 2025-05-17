# Projeto Django - Lutadores com Login

Sistema com autenticação onde cada usuário pode criar até 2 lutadores com atributos editáveis.

## Funcionalidades
- Registro e login de usuários (apenas letras, até 8 caracteres)
- Criação de até 2 lutadores por usuário
- Edição de status (força, agilidade, resistência)

## Como usar
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Acesse `/registro/` para criar um usuário e `/login/` para acessar o sistema.
