# PoI App
Aplicação para marcar pontos de interese em uma imagem

## Requisitos
- Python 3
- pip
- [Opcional] conda

##Instalação
Para a instalação é recomendado que se tenha um ambiente virtual (por exemplo conda) já configurado e ativado. 

Instale as bibliotecas necessárias:
`pip install -r requirements.txt`

## Como usar
Para fazer uso da aplicação é necessário saber o caminho da imagem e, opcionalmente, definir um diretório onde salvar as marcações feitas.

`python poiapp.py <imagem> <diretório>`

Exemplo de uso:

`python poiapp.py imagem1.png marcacoes`

Após inicializado, uma janela será mostrada com a imagem.

Para **realizar uma marcação** clique com o botão esquerdo do mouse no local desejado.

### Menu de propriedades

Para exibir o menu de propriedades, pressione `CTRL+P`. Nesse menu há as seguintes opções de configuração:
- Salvar em arquivo as marcações exibidas;
- Apagar todas as marcações (apenas as marcações mostradas, não altera os arquivos salvos);
- Esconder temporariamente as marcações feitas.

### Como fechar
Para sair da aplicação, basta clicar no `X` da janela da aplicação ou pressionar a tecla `ESQ`.