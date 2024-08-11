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
