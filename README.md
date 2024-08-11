# Cursos 

Claro! Aqui está um resumo das plataformas **freeCodeCamp**, **Cognitive Class** e **Data Science Academy**, e sua relevância no ensino de Machine Learning:

---

### freeCodeCamp
**freeCodeCamp** é uma plataforma gratuita que oferece cursos interativos em diversas áreas de tecnologia, incluindo machine learning. Seus cursos são práticos e acessíveis para iniciantes.

- **Link de acesso**: [freeCodeCamp](https://www.freecodecamp.org/)

### Cognitive Class
**Cognitive Class** é uma plataforma gratuita da IBM que oferece cursos em ciência de dados e machine learning, com foco em habilidades práticas.

- **Link de acesso**: [Cognitive Class](https://cognitiveclass.ai/)

### Data Science Academy
**Data Science Academy** oferece cursos online em ciência de dados e inteligência artificial, com uma abordagem prática e interativa.

- **Link de acesso**: [Data Science Academy](https://www.datascienceacademy.com.br/)

---

Espero que isso ajude! Se precisar de mais alguma coisa, estou à disposição. 😊

Source: Conversation with Copilot, 8/11/2024
(1) Data Science Academy. https://www.datascienceacademy.com.br/.
(2) Data Science Certification Training, Courses and Classes Online. https://www.datascienceacademy.io/.
(3) Learn Data Science and AI Online | DataCamp. https://www.datacamp.com/.
(4) Data Science Courses | Learn Data Science Online | Udacity. https://www.udacity.com/school/data-science.



# A documentação do código em si se encontra nos deployments, segue link [https://venysssssssssss.github.io/projeto-senai-ml/]

# Tutorial de Instalação do pip, Poetry e pyenv no Windows e Linux

## Sumário
1. [Instalação do pip](#instalação-do-pip)
    - [Windows](#pip-no-windows)
    - [Linux](#pip-no-linux)
2. [Instalação do Poetry](#instalação-do-poetry)
    - [Windows](#poetry-no-windows)
    - [Linux](#poetry-no-linux)
3. [Instalação do pyenv](#instalação-do-pyenv)
    - [Windows](#pyenv-no-windows)
    - [Linux](#pyenv-no-linux)
4. [Introdução](#introdução)
5. [Verificando e Ativando a Versão do Python com pyenv](#verificando-e-ativando-a-versão-do-python-com-pyenv)
6. [Gerenciando Dependências com Poetry](#gerenciando-dependências-com-poetry)
7. [Boas Práticas](#boas-práticas)

---

## Instalação do pip

O `pip` é o gerenciador de pacotes padrão do Python. Aqui estão as instruções para instalá-lo no Windows e Linux.

### pip no Windows

1. **Verifique se o Python está instalado**:
    - Abra o terminal (cmd) e digite:
    ```bash
    python --version
    ```
    - Se o Python estiver instalado, o número da versão será exibido. Caso contrário, baixe e instale o Python a partir do site oficial: [Python.org](https://www.python.org/downloads/).

2. **Instale o pip**:
    - O `pip` geralmente vem instalado com o Python. Caso precise reinstalá-lo:
    ```bash
    python -m ensurepip --upgrade
    ```

3. **Verifique a instalação do pip**:
    ```bash
    pip --version
    ```

### pip no Linux

1. **Atualize o gerenciador de pacotes**:
    - Para distribuições baseadas em Debian (Ubuntu, Mint, etc.):
    ```bash
    sudo apt update
    ```
    - Para distribuições baseadas em Red Hat (Fedora, CentOS, etc.):
    ```bash
    sudo dnf check-update
    ```

2. **Instale o pip**:
    - Para distribuições baseadas em Debian:
    ```bash
    sudo apt install python3-pip
    ```
    - Para distribuições baseadas em Red Hat:
    ```bash
    sudo dnf install python3-pip
    ```

3. **Verifique a instalação do pip**:
    ```bash
    pip3 --version
    ```

---

## Instalação do Poetry

O `Poetry` é um gerenciador de dependências para Python que simplifica a configuração de ambientes e a gestão de pacotes.

### Poetry no Windows

1. **Instale o Poetry**:
    - Abra o terminal (cmd ou PowerShell) e execute:
    ```bash
    curl -sSL https://install.python-poetry.org | python -
    ```

2. **Adicione o Poetry ao PATH**:
    - Verifique o caminho de instalação exibido ao final do processo.
    - Adicione o caminho do executável do `Poetry` à variável de ambiente `PATH` através das configurações do sistema.

3. **Verifique a instalação**:
    ```bash
    poetry --version
    ```

### Poetry no Linux

1. **Instale o Poetry**:
    - Abra o terminal e execute:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. **Adicione o Poetry ao PATH**:
    - O instalador geralmente adiciona o `Poetry` ao `PATH` automaticamente. Caso contrário, adicione manualmente ao `.bashrc` ou `.zshrc`:
    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    ```

3. **Verifique a instalação**:
    ```bash
    poetry --version
    ```

---

## Instalação do pyenv

O `pyenv` é uma ferramenta útil para gerenciar várias versões do Python em um único sistema.

### pyenv no Windows

1. **Pré-requisitos**:
    - Instale o `git` no Windows: [Git para Windows](https://gitforwindows.org/).
    - Instale o `Visual Studio Build Tools`: [Build Tools para Visual Studio 2019](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

2. **Instale o pyenv**:
    - Use o `pyenv-win`, uma versão do `pyenv` adaptada para Windows:
    ```bash
    git clone https://github.com/pyenv-win/pyenv-win.git %USERPROFILE%\.pyenv
    ```

3. **Adicione o pyenv ao PATH**:
    - Adicione as seguintes variáveis de ambiente ao `PATH`:
    ```
    %USERPROFILE%\.pyenv\pyenv-win\bin
    %USERPROFILE%\.pyenv\pyenv-win\shims
    ```

4. **Verifique a instalação**:
    ```bash
    pyenv --version
    ```

### pyenv no Linux

1. **Pré-requisitos**:
    - Instale dependências necessárias:
    ```bash
    sudo apt update
    sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
    ```

2. **Instale o pyenv**:
    - Clone o repositório do `pyenv` no diretório home:
    ```bash
    curl https://pyenv.run | bash
    ```

3. **Configure o ambiente**:
    - Adicione as linhas abaixo ao seu `.bashrc` ou `.zshrc`:
    ```bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```

4. **Recarregue o shell**:
    ```bash
    source ~/.bashrc
    ```

5. **Verifique a instalação**:
    ```bash
    pyenv --version
    ```

---

## Conclusão

Após seguir os passos acima, você terá o `pip`, `Poetry` e `pyenv` instalados e configurados corretamente no seu sistema, tanto no Windows quanto no Linux. Agora você está pronto para gerenciar seus ambientes Python e dependências com eficiência!

## Introdução

Se você está trabalhando em um projeto que já utiliza o `pyenv` e o `Poetry`, é importante entender como essas ferramentas interagem e como utilizá-las corretamente para gerenciar versões do Python e dependências. Este guia vai te mostrar como verificar e ativar a versão correta do Python com o `pyenv` e como gerenciar dependências e ambientes virtuais usando o `Poetry`.

## Verificando e Ativando a Versão do Python com pyenv

O `pyenv` permite gerenciar múltiplas versões do Python em um sistema, o que é particularmente útil para projetos que exigem versões específicas.

1. **Verifique a versão de Python utilizada pelo projeto**:
    - Normalmente, o projeto especifica a versão do Python em um arquivo `.python-version` ou diretamente no `pyproject.toml` (caso o `Poetry` esteja configurado para isso).
    - Para verificar a versão configurada, execute:
    ```bash
    cat .python-version
    ```
    - Ou, caso esteja especificado no `pyproject.toml`, procure pela seção `[tool.poetry.dependencies]`:
    ```toml
    [tool.poetry.dependencies]
    python = "^3.9"
    ```

2. **Ative a versão correta do Python**:
    - Com o `pyenv`, ative a versão correta:
    ```bash
    pyenv install 3.9.6 # Se a versão ainda não estiver instalada
    pyenv local 3.9.6
    ```
    - Isso garante que todos os comandos Python executados dentro do diretório do projeto utilizem a versão especificada.

3. **Verifique a versão ativa**:
    - Certifique-se de que a versão correta está ativa:
    ```bash
    python --version
    ```

## Gerenciando Dependências com Poetry

O `Poetry` facilita a gestão de dependências e ambientes virtuais, centralizando as configurações em um único arquivo, o `pyproject.toml`.

1. **Instale as dependências do projeto**:
    - O arquivo `pyproject.toml` no diretório do projeto lista todas as dependências necessárias. Para instalá-las, execute:
    ```bash
    poetry install
    ```
    - Isso cria automaticamente um ambiente virtual com as dependências listadas e configuradas.

2. **Ative o ambiente virtual**:
    - Para trabalhar dentro do ambiente virtual criado pelo `Poetry`, ative-o com:
    ```bash
    poetry shell
    ```
    - Agora, todos os comandos executados (como `python`, `pip`, etc.) usarão o ambiente virtual gerado pelo `Poetry`.

3. **Adicionando novas dependências**:
    - Para adicionar uma nova dependência ao projeto:
    ```bash
    poetry add nome-da-dependência
    ```
    - Isso atualiza automaticamente o `pyproject.toml` e o `poetry.lock`.

4. **Removendo dependências**:
    - Para remover uma dependência:
    ```bash
    poetry remove nome-da-dependência
    ```
    - O `Poetry` atualizará os arquivos de configuração e removerá a dependência do ambiente virtual.

5. **Atualizando dependências**:
    - Para garantir que todas as dependências estejam na última versão permitida pelas restrições no `pyproject.toml`:
    ```bash
    poetry update
    ```

## Boas Práticas

Aqui estão algumas boas práticas para trabalhar com `pyenv` e `Poetry` em projetos existentes:

1. **Sempre verifique a versão do Python**:
    - Antes de começar a trabalhar em um projeto, verifique se a versão correta do Python está ativa usando o `pyenv`. Isso evita problemas de compatibilidade.

2. **Mantenha o ambiente virtual ativado**:
    - Utilize o ambiente virtual criado pelo `Poetry` para garantir que as dependências sejam consistentes com as do projeto.

3. **Utilize o comando `poetry lock`**:
    - Sempre que adicionar ou remover uma dependência, utilize o comando `poetry lock` para garantir que o arquivo `poetry.lock` esteja atualizado.

4. **Documente as versões**:
    - Mantenha o arquivo `pyproject.toml` bem documentado, incluindo as versões das dependências e a versão do Python, para facilitar a manutenção e colaboração no projeto.

---

## Conclusão

Ao seguir essas instruções, você poderá utilizar de maneira eficiente o `pyenv` para gerenciar versões do Python e o `Poetry` para gerenciar dependências em um ambiente de projeto existente. Isso garante que você tenha um ambiente consistente e configurado corretamente, permitindo um desenvolvimento fluido e sem complicações.

