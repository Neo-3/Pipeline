# Pipeline

Este repositório é um orquestrador que integra vários módulos desenvolvidos por alunos de Ciência da Computação da equipe 3, do 5º período do Cesar School no primeiro semestre de 2020 para a NeoEnergia.

## Instruções de ambiente

Este repositório trata-se de um orquestrador que contém outros repositórios git como submódulos, cada módulo possui o seu versionamento de maneira independente, siga os passos para a instalação

### Requisitos

Será necessário um computador com pelo menos 4 gb de memória RAM e ter instalado o Python3, recomendável também o uso de virtualEnv.

### Clone o repositório

Clone o repositório com o comando:

> \$ git clone --recurse-submodules git@github.com:Neoenergia-3/Pipeline.git

Então navegue até o repositório com:

> cd Pipeline

### Inicie um ambiente virtual

Crie um ambiente virtual com o comando:

> python3 -m venv ./venv

Então ative este ambiente com:

> source venv/bin/activate

### Instale as dependências

Instale as dependências com o comando:

> pip install -r requirements.txt

## Instruções de execução

A Pipeline Neo3 funciona como uma ferramenta CLI que recebe como parâmetro o step da pipeline que o usuário deseja executar ou executa a mesma de maneira completa.

### Executando a pipeline inteira

Para executar todos os passos da pipeline execute o comando:

> python main.py --full

**nota**: Após o passo de image clustering será necessário uma ação manual do operador, ao qual precisará classificar as imagens consideradas como "bons exemplos" já pré separadas em clusters, salvando em um diretório chamado _"selected/1"_, bem como os "maus exemplos" em um diretório chamado _"selected/0"_, tais instruções são exibidas no terminal.

### Executando o Image Crawler

Image Crawler é o serviço responsável por realizar o download de imagens do Google através de pesquisas no Google Image, este serviço simula um robô e obtém até 300 imagens de cada campo pesquisado.

para executar somente o image crawler execute o comando:

> python main.py --image-crawler

Nesta pipeline estamos pesquisando pelos seguintes termos:

> ["analog electric meter", "analog electricity meter", "electricity meter", "electric meter", "energy meter", "medidor de energia", "medidor de energia analogico", "medidor de energia eletrica"]

ao terminar sua execução, este serviço salva as imagens baixadas na pasta "downloads"
