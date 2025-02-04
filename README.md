
# 🧮 Calculadora Tkinter

Uma **calculadora simples** desenvolvida com **Python** e **Tkinter**. A interface gráfica permite realizar operações matemáticas básicas com uma experiência de usuário limpa e intuitiva.

## 🚀 Funcionalidades

- **Operações matemáticas básicas**: Soma, subtração, multiplicação e divisão.
- **Limpar tela**: Botão "C" para apagar a expressão na tela.
- **Calcular resultado**: Botão "=" para calcular a expressão inserida.
- **Interface amigável**: Design simples e moderno utilizando o Tkinter.

## 📦 Como executar

### Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

### Passos para rodar o projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/calculadora-tkinter.git
   ```

2. **Entre no diretório do projeto**:
   ```bash
   cd calculadora-tkinter
   ```

3. **Execute o arquivo Python**:
   ```bash
   python calculadora.py
   ```

## 💻 Como funciona

- **Tkinter**: A interface gráfica é criada usando a biblioteca Tkinter, que fornece uma maneira fácil de criar interfaces de usuário no Python.
- **Função `on_click`**: Responsável por gerenciar os cliques nos botões. Ela executa ações de acordo com o botão pressionado: adicionar números, operadores, calcular o resultado ou limpar a tela.
- **Avaliação de Expressão**: A expressão matemática inserida pelo usuário é avaliada utilizando a função `eval()`. Caso a expressão seja inválida, uma mensagem de erro será exibida.
- **Cores e Design**: A interface conta com um fundo azul gradiente e botões coloridos para uma melhor experiência visual.

## 📸 Exemplo de uso

1. Ao executar o programa, você verá a interface da calculadora.
2. Digite uma expressão matemática como `5 + 3 * 2`.
3. Pressione o botão "=" para calcular o resultado.
4. Se precisar, clique em "C" para limpar a tela e inserir uma nova expressão.

## 🎨 Layout da Interface

A interface possui um layout simples com:

- Um **campo de entrada** na parte superior para exibir a expressão e o resultado.
- **Botões** dispostos em 4 linhas, incluindo números de 0 a 9, operações e um botão de limpar ("C") e de resultado ("=").

## 🔧 Como contribuir

Se você quiser contribuir para melhorar este projeto, sinta-se à vontade para fazer um **fork** e enviar um **pull request**!

## 📜 Licença

Este projeto está licenciado sob a <p align="center"><img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000"></p>

---
