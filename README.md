# Projeto Django - Autenticação com Usuários Pré-Cadastrados

Este é um projeto em Django que permite os usuários (3 atualmente criados artificialmente) criar lutadores e golpes para esses lutadores para coloca-los no banco de dados. É permitido editar e remover lutadores e golpes. Cada usuário só pode criar 2 lutadores, mas quantos golpes quiserem.
O projeto usa Supabase como banco de dados remoto e Koyeb para o deploy.

![Screenshot do Site](projeto_lutadores/staticfiles/Screenshot_typesouls2.jpg "Screenshot do projeto")

### Desenvolvedores
Matheus - Sistemas de Informação

João Marcos - Sistemas de Informação

Isaac - Sistemas para internet

#### Tecnologias
-HTML

-CSS

-Javascript

-Python

-Django

-Supabase (banco de dados remoto usando PostgreSQL)

-Koyeb (para deploy)

#### Ambiente de desenvolvimento
-VS Code

-Pixlr(Para criação da logo)

-Github
  
##  Requisitos

- Python 3.10 ou superior
- Django 5.2.1
- Whitenoise 6.9.0 (para lidar com arquivos estáticos fora de ambiente de desenvolvimento)

##  Como rodar o projeto

1. **Clone ou extraia o projeto em uma pasta**
2. **Abra o terminal na pasta do projeto**
3. **Crie um ambiente virtual**:
   ```bash
   py -m venv venv
   ```
4. **Ative o ambiente virtual**:

   - PowerShell:
   ```bash
   .\venv\Scripts\Activate.ps1
   ```

   - CMD:
   ```bash
   .\venv\Scripts\activate
   ```

5. **Instale o Django**:
   ```bash
   pip install django
   ```
6. **Instale o Whitenoise**:
   ```bash
   pip install whitenoise
   ```

7. **Crie as migrações**:
   ```bash
   py manage.py makemigrations
   ```

7. **Faça as migrações**:
   ```bash
   py manage.py migrate
   ```

8. **Inicie o servidor**:
   ```bash
   py manage.py runserver
   ```

9. **Acesse o site**:
- 🔗 [Acessar site](https://yucky-noreen-sou-aluno-2ab614ec.koyeb.app)
## 👤 Usuários cadastrados

| Usuário             |Senha |
|---------------------|------|
| Homem_existente     | 123  |
| Homem_inexistente   | 123  |
| Homem_torta         | 123  |

##  Segurança

- O site é envolvido de um middleware customizado de autenticação que verifica se o usuário está autenticado em cada chamada de documento.
- Login obrigatório para acessar qualquer parte do site, atualmente só tem 3 logins, sem possibilidade de registrar mais.

#### Referências e créditos
- ChatGPT(Auxílio no desenvolvimente e criação de algumas imagens)

- Bootstrap 3: Framework CSS para layout e componentes.


---
Projeto entregue para a disciplina de [Desenvolvimento de Software para a Web](http://github.com/andreainfufsm/elc1090-2025a) em 2025a
