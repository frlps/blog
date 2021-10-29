# blog

Para a matéria de Projeto Integrador da Univesp, 4 semestre de 2021.

 Equipe:    
            **Alexandre;
            **Fabio Souza;
            **Fabio Borges;
            **Gustavo;
            **marcio;
            **Rodrigo.

Tecnologias empregadas:
    **1-Python (linguagem);
    **2-Flask (microframework web);
    **3-Jinja (Manipulação GUI);
    **4-Bootstrap (framework open para estilo e responsividade - biblis css);
    **5-HTML, CSS e JS (view, estilo e dinâmica);
    **6-SQLite (Banco de dados);
    **7-SQLAlchemy (Fazer mapeamento objeto relacional).


------------------------------------------------------------------




Clonar os repositório em: 


conda activate blog 

ou:


Criar o ambiente virtual, indo até a pasta raiz do repositório e rodar:
    No windows:
        python -m venv /
        \Scripts\Activate.ps1

    No Linux:
        venv/bin/activate

python -m pip install --upgrade pip

Para utilizar o projeto deve-se primeiramente criar um ambiente virtual e rodar o 'requirements.txt' usando:
    pip install -r requirements.txt

Criar as variáveis de ambiente:
    No Windows: 
        Set-Content -Path FLASK_APP -Value 'app'
        Set-Content -Path FLASK_ENV -Value 'development'
        Set-Content -Path BASIC_AUTH_USERNAME -Value 'seuUsuario' (DEPOIS)
        Set-Content -Path BASIC_AUTH_PASSWORD -Value 'suaSenha' (DEPOIS)

        teste com:
            Set-Location Env:
                ls
                    e veja de estão lá

            Sair de Env - 

    No Linux:
        export FLASK_APP=app
        export FLASK_ENV=development
        export BASIC_AUTH_USERNAME=seuUsuario (DEPOIS)
        export BASIC_AUTH_PASSWORD=suaSenha (DEPOIS)

Link para arquivos bootstrap: https://www.techwithtim.net/tutorials/flask/adding-bootstrap/

Para criar o banco de dados: python .\init.db.py no pronpt de comando 
