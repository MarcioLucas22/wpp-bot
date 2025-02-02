# wpp-bot

**wpp-bot** é uma aplicação desenvolvida em Python que automatiza o envio de mensagens via WhatsApp. O projeto utiliza uma planilha Excel para gerenciar os números de telefone destinatários e scripts para processar e enviar mensagens personalizadas.

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada no desenvolvimento da aplicação.
- **Bibliotecas Python**: Para manipulação de arquivos Excel (como `pandas` ou `openpyxl`) e integração com o WhatsApp.

## 📂 Estrutura do Projeto

- **app.py**: Script principal que executa a aplicação, gerenciando o fluxo de envio de mensagens.
- **utils.py**: Contém funções auxiliares para manipulação de dados e integração com APIs.
- **telefones.xlsx**: Arquivo Excel que armazena os números de telefone e informações relevantes para o envio das mensagens.
- **requirements.txt**: Lista de dependências necessárias para a execução do projeto.

## ⚙️ Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/MarcioLucas22/wpp-bot.git
   cd wpp-bot
   ```

2. **Crie um ambiente virtual e ative-o:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `telefones.xlsx`:**
   - Insira os números de telefone e outras informações pertinentes no arquivo `telefones.xlsx`.

5. **Execute a aplicação:**
   ```bash
   python app.py
   ```

## 📬 Contato

Para dúvidas ou suporte, entre em contato através do [GitHub de MarcioLucas22](https://github.com/MarcioLucas22).

---

Desenvolvido com ❤️ para automatizar tarefas e facilitar a comunicação via WhatsApp.
