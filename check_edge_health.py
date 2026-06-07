import requests
import time

# URL do seu laboratório local mapeado no arquivo hosts
# URL = "http://borda.operadora.com:8080/metrics"
URL = "http://127.0.0.1:80/metrics"

def check_cluster_health():
    print(f"Iniciando monitoramento em: {URL}\n")
    try:
        # Medindo o tempo que o Ingress + Nginx levam para responder
        start_time = time.time()
        headers = {'Host': 'borda.operadora.com'}  # Garantindo que o Host header esteja correto
        response = requests.get(URL, headers=headers, timeout=5)
        end_time = time.time()
        
        latency = (end_time - start_time) * 1000 # Convertendo para milissegundos
        
        if response.status_code == 200:
            print(f"🟢 [SUCCESS] Status: {response.status_code} | Latência: {latency:.2f}ms")
            # Procura a métrica de conexões ativas no texto recebido
            if "Active connections" in response.text:
                active_line = [line for line in response.text.split('\n') if "Active connections" in line]
                print(f"📊 {active_line[0]}")
        else:
            print(f"🟡 [WARNING] Cluster respondeu com código de erro: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"🔴 [CRITICAL] Falha catastrófica ao conectar na Borda! Erro: {e}")

if __name__ == "__main__":
    check_cluster_health()