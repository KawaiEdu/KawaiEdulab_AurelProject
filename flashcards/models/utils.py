import os, platform
APP_NAME = "FLASHCARDS TRAINER"
def ask(prompt):
    return input(prompt).strip()
def cls():
    os.system("cls"if platform.system()=="Windows" else "clear")
def banner(): 
        print("="*36); print(f"{APP_NAME:^36}"); print("="*36)
def confirm(msg="Yakin? (Y/N): "): 
    return input(msg).strip().lower() in ("y", "ya","yes", "yap")