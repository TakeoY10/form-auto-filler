import keyboard
import pyautogui
import pyperclip

# ==============================================================================
# CONFIGURAÇÃO DE DADOS (Substitua pelos seus dados antes de rodar)
# ==============================================================================
MEUS_DADOS = {
    "nome": "Seu Nome Completo",
    "email": "seu.email@exemplo.com",
    "usuario": "seu_usuario",
    "telefone": "11999999999",
    "cpf": "000.000.000-00",
    "cep": "00000-000"
}

pyautogui.PAUSE = 0.1

def digitar_texto(texto):
    """
    Copia o texto para a área de transferência e cola (Ctrl+V).
    Garante suporte completo a acentuação e caracteres especiais em UTF-8.
    """
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')

# ==============================================================================
# FUNÇÕES DE PREENCHIMENTO
# ==============================================================================
def preencher_nome():
    digitar_texto(MEUS_DADOS["nome"])
    print("[✔] Nome colado!")

def preencher_email():
    digitar_texto(MEUS_DADOS["email"])
    print("[✔] E-mail colado!")

def preencher_usuario():
    digitar_texto(MEUS_DADOS["usuario"])
    print("[✔] Usuário colado!")

def preencher_telefone():
    digitar_texto(MEUS_DADOS["telefone"])
    print("[✔] Telefone colado!")

def preencher_cpf():
    digitar_texto(MEUS_DADOS["cpf"])
    print("[✔] CPF colado!")

def preencher_cep():
    digitar_texto(MEUS_DADOS["cep"])
    print("[✔] CEP colado!")

def main():
    print("=" * 55)
    print(" AUTOMACÃO ATIVA (FORM AUTO-FILLER)")
    print("=" * 55)
    print(" [Shift + F1]    -> Digita o NOME")
    print(" [Shift + F2]    -> Digita o E-MAIL")
    print(" [Shift + F4]    -> Digita o USUÁRIO")
    print(" [Ctrl + F1]     -> Digita o TELEFONE")
    print(" [Ctrl + F2]     -> Digita o CPF")
    print(" [Ctrl+Shift+P]  -> Digita o CEP")
    print(" [Esc]           -> Encerrar o programa")
    print("=" * 55)

    # Mapeamento limpo de atalhos globais
    keyboard.add_hotkey('shift+f1', preencher_nome)
    keyboard.add_hotkey('shift+f2', preencher_email)
    keyboard.add_hotkey('shift+f4', preencher_usuario)
    keyboard.add_hotkey('ctrl+f1', preencher_telefone)
    keyboard.add_hotkey('ctrl+f2', preencher_cpf)
    keyboard.add_hotkey('ctrl+shift+p', preencher_cep)

    keyboard.wait('esc')

if __name__ == '__main__':
    main()