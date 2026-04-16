# Otimização de Imagens em Python

Este projeto é um script simples em Python para otimizar imagens. Ele converte imagens de vários formatos (JPG, PNG, BMP, TIFF) para WebP, redimensiona se necessário para um tamanho máximo de 1920x1920 pixels, e salva com qualidade de 80%.

## Pré-requisitos

- Python 3.6 ou superior
- Biblioteca Pillow (PIL)

## Instalação

1. Clone ou baixe o repositório.
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

1. Coloque as imagens a serem otimizadas na pasta `input/imagens/plantas/` (ou subpastas).
2. Execute o script:

   ```bash
   python main.py
   ```

3. As imagens otimizadas serão salvas na pasta `output/imagens/plantas/` com o mesmo nome, mas em formato WebP.

## Estrutura do Projeto

- `main.py`: Script principal para otimização de imagens.
- `requirements.txt`: Lista de dependências Python.
- `input/`: Pasta para imagens de entrada.
- `output/`: Pasta para imagens otimizadas.

## Configurações

Você pode ajustar as constantes no início do `main.py`:

- `MAX_WIDTH` e `MAX_HEIGHT`: Tamanho máximo da imagem.
- `QUALITY`: Qualidade da compressão (0-100).
- `INPUT_FOLDER` e `OUTPUT_FOLDER`: Pastas de entrada e saída.

## Licença

Este projeto é de código aberto e pode ser usado livremente.