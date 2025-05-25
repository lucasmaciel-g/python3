import os
import subprocess

def verificar_se_git():
    if not os.path.exists(".git"):
        print("🚫 Esta pasta não é um repositório Git.")
        return False
    print("✅ Esta pasta é um repositório Git.")
    return True

def obter_remote_origin():
    try:
        resultado = subprocess.check_output(["git", "remote", "-v"], stderr=subprocess.STDOUT)
        texto = resultado.decode("utf-8")
        linhas = texto.strip().split("\n")
        for linha in linhas:
            if "origin" in linha and "(fetch)" in linha:
                url = linha.split()[1]
                print(f"🔗 Origin encontrado: {url}")
                return url
        print("⚠️ Nenhum remoto 'origin' foi encontrado.")
        return None
    except subprocess.CalledProcessError:
        print("❌ Erro ao tentar acessar os remotes.")
        return None

def testar_conexao_com_gitHub(url):
    if url.startswith("https://github.com/") or url.startswith("git@github.com:"):
        print("🛰️ A URL parece válida para GitHub.")
        print("🔄 Tentando conexão com o GitHub remoto (git ls-remote)...")
        try:
            subprocess.check_output(["git", "ls-remote", url], stderr=subprocess.STDOUT)
            print("✅ Conexão com o GitHub verificada com sucesso.")
        except subprocess.CalledProcessError as e:
            print("🚫 Não foi possível acessar o repositório remoto.")
            print("📄 Detalhes:", e.output.decode("utf-8"))
    else:
        print("🚫 A URL do origin não parece ser do GitHub.")

if __name__ == "__main__":
    if verificar_se_git():
        origin_url = obter_remote_origin()
        if origin_url:
            testar_conexao_com_gitHub(origin_url)