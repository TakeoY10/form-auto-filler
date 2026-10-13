# QuickForm Auto-Filler

Utilitário em Python desenvolvido para automação e produtividade no preenchimento manual e repetitivo de formulários através de atalhos globais de teclado (*hotkeys*).

O projeto foi projetado para funcionar de forma transparente, sem conflitos com atalhos nativos de navegadores baseados em Chromium (Brave, Chrome, Edge) e otimizado para layouts de teclado **80% (TKL)**.

---

## Tecnologias e Bibliotecas Utilizadas

- **Python 3.15+**
- **`keyboard`**: Escuta e captura de eventos globais de teclado no nível do sistema operacional.
- **`PyAutoGUI` & `pyperclip`**: Manipulação do clipboard e injeção de comandos de colagem (`Ctrl+V`) com suporte total a acentuação e caracteres especiais (UTF-8).
- **Windows Batch Scripting (`.bat`)**: Automação de inicialização com elevação automática de privilégios de Administrador via PowerShell.

---

## Estrutura do Repositório

```text
form-auto-filler/
│
├── Automacao.py              # Script principal em Python
├── automacao.bat             # Script de inicialização automática como Administrador
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do projeto
```

---

## ⌨️ Mapeamento de Atalhos Configurados

| Atalho | Campo Preenchido |
| :--- | :--- |
| `Shift + F1` | **Nome Completo** |
| `Shift + F2` | **E-mail** |
| `Shift + F4` | **Nome de Usuário** |
| `Ctrl + F1` | **Telefone / WhatsApp** |
| `Ctrl + F2` | **CPF** |
| `Ctrl + Shift + P` | **CEP (Código Postal)** |
| `Esc` | **Encerrar a aplicação** |

---

##  Como Executar o Projeto

### Pré-requisitos
- Sistema Operacional **Windows 10/11**
- **Python 3.10+** instalado no sistema.

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/TakeoY10/form-auto-filler.git
   cd form-auto-filler
   ```

2. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execução Direta (1-Clique):**
   - Dê um duplo clique no arquivo `automacao.bat`. O script pedirá autorização de **Administrador** e iniciará a aplicação automaticamente no terminal.

---

## Desafios Técnicos Solucionados

- **Gestão de Caracteres Especiais:** Uso de cópia direta para o *clipboard* (`pyperclip`) seguida de injeção (`Ctrl+V`), evitando erros de digitação em teclados ABNT2.
- **Eliminação de Conflitos de Navegador:** Mapeamento feito para contornar atalhos nativos em navegadores (como `Ctrl+F5` ou `Ctrl+F3`), garantindo estabilidade no Brave Browser e Google Chrome.
