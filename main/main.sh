#!/bin/bash

#echo "Executando script em: $(pwd)"


# Ativa o ambiente virtual
source "$HOME/Documentos/learnings/smooth/high_python/main/.venv/bin/activate"


# Tenta executar o script Python e verifica se há erro
if  ! python3 $HOME/Documentos/learnings/smooth/high_python/main/run.py --start; then
    echo "Erro ao executar python3 main/run.py --start. Verificando instalação do Python..."

    # Verifica se o Python está instalado
    #if ! command -v python3 &> /dev/null; then
    #    install_python
    #fi
    
    # Tenta executar o script novamente após a instalação
    #echo "Tentando executar o script novamente..."
    #python3 $HOME/Documentos/learnings/smooth/high_python/main/run.py --start
fi
# Função para instalar o Python caso ele não esteja presente
install_python() {
    echo "Python não encontrado. Iniciando instalação..."

    # Atualiza a lista de pacotes e instala dependências
    sudo apt update
    sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev \
        libreadline-dev libffi-dev curl libsqlite3-dev wget

    # Baixa o código fonte do Python
    PYTHON_VERSION="3.12.0"
    wget "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz"

    # Extrai e compila o Python
    tar -xf "Python-${PYTHON_VERSION}.tgz"
    cd "Python-${PYTHON_VERSION}" || exit
    ./configure --enable-optimizations
    make -j 8  # Compilação com 8 threads
    sudo make altinstall

    # Limpeza de arquivos temporários
    cd ..
    rm -rf "Python-${PYTHON_VERSION}" "Python-${PYTHON_VERSION}.tgz"
    echo "Instalação do Python concluída."
}
