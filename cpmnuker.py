import requests
from time import sleep

BASE_URL: str = "https://cpmnuker.anasov.ly/v2/api"

class CPMNuker:

    def __init__(self) -> None:
        self.auth_token = None
    
    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        response = requests.post(f"{BASE_URL}/account_login", data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        response = requests.post(f"{BASE_URL}/account_register", data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")
    
    def delete(self):
        payload = { "account_auth": self.auth_token }
        requests.post(f"{BASE_URL}/account_delete", data=payload)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/get_data", data=payload)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/set_rank", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        response = requests.post(f"{BASE_URL}/set_money", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_id(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        response = requests.post(f"{BASE_URL}/set_id", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        response = requests.post(f"{BASE_URL}/set_name", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def delete_player_friends(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/delete_friends", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def maximize_drag_wins(self) -> bool:
        payload = {
            "account_auth": self.auth_token
        }
        response = requests.post(f"{BASE_URL}/maximize_drag_wins", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def complete_missions(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/complete_missions", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_apartments(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/unlock_apartments", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_slots(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/unlock_slots", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_brakes(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/unlock_brakes", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_wheels(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/unlock_wheels", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_clothes(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/unlock_equipments", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_cars(self) -> bool:
        response = requests.post(f"{BASE_URL}/unlock_cars")
        response_decoded = response.json()
        return response_decoded.get("ok")
