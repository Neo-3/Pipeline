# Pipeline

Este repositório é um orquestrador que integra vários módulos desenvolvidos por alunos de Ciência da Computação da equipe 3, do 5º período do Cesar School no primeiro semestre de 2020 para a NeoEnergia.

## Instruções de ambiente

Este repositório trata-se de um orquestrador que contém outros repositórios git como submódulos, cada módulo possui o seu versionamento de maneira independente, siga os passos para a instalação

### Requisitos

Será necessário um computador com pelo menos 4 gb de memória RAM e ter instalado o Python3, recomendável também o uso de virtualEnv.

Você também irá precisar baixar um chromedriver compatível com a sua versão do Google Chrome e o seu sistema operacional, por padrão o repositório conta com um chromedriver para MacOS versão 83.0.4103.116, se este não for compatível com seu ambiente, baixe um chrome driver em:

> https://chromedriver.chromium.org/downloads

### Clone o repositório

Clone o repositório com o comando:

> git clone --recurse-submodules git@github.com:Neoenergia-3/Pipeline.git

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

### Executando o Image Clustering

Este passo da pipeline tem como objetivo auxiliar o operador a identificar mais facilmente exemplos de boas imagens de medidores e outras imagens, agrupando-as.

Execute somente o image clustering com o comando:

> python main.py --image-clustering

**nota**: ao final da execução deste passo, será necessário um procedimento manual de separação dos exemplos de imagem, siga as instruções do terminal.

### Executando o Image Data Augmentation

Este passo da pipeline tem como objetivo aumentar a quantidade de imagens nas bases, bem como já separar alguns exemplos de imagens que serão utilizados para treinar os classificadores e outros que serão utilizados para testar.

Para executar somente o Image Data Augmentation execute o comando:

> python main.py --image-data-augmentation

Atualmente para cada imagem original são geradas mais 4 imagens realizando pequenas alterações no brilho, rotação, zoom e operando inversões.

70% das imagens são separadas para treino e 30% para teste.

### Executando o Image Data Set

Este passo da pipeline tem como objetivo gerar um arquivo csv com as bases de teste e de treino, somente utilizando as features com maior correlação com o problema em questão, já pré mapeadas anteriormente.

Para executar somente o Image Data Set digite:

> python main.py --image-data-set

### Executando o Image Classifier

Este passo executa os modelos de machine learning selecionados pela equipe, afim de obter um modelo com melhor acurácia para o problema em questão.

> python main.py --image-classifier

Atualmente foram testados 4 classificadores, o KNN, a Regressão Logística, o Random Forest e o CatBoost.

O classificador com melhor desempenho foi o CatBoost com 93.45985401459855% de acurácia.
