import requests
import json

class GophishAutomation:
    def __init__(self, api_key, base_url="http://localhost:3948/api/v1/"):
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        self.base_url = base_url

    def get_campaigns(self):
        """Gophish üzerinden yürütülen kampanyaları listeler ve raporlar."""
        try:
            response = requests.get(f"{self.base_url}campaigns", headers=self.headers)
            if response.status_code == 200:
                print("[+] Kampanyalar başarıyla çekildi:")
                print(json.dumps(response.json(), indent=4))
            else:
                print(f"[-] Hata Kodu: {response.status_code} - Yanıt: {response.text}")
        except Exception as e:
            print(f"[-] Bağlantı hatası: {e}")

if __name__ == "__main__":
    # Gophish panelinden alacağın API anahtarını buraya ekleyebilirsin
    API_KEY = "GOPHISH_API_ANAHTARINI_YAZALIM"
    manager = GophishAutomation(API_KEY)
    
    print("[*] Gophish Python Otomasyon Betiği Başlatıldı...")
    # manager.get_campaigns()
