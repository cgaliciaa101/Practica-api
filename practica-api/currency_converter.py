import requests

class CurrencyConverter:
    #se inicia el objeto CurrencyConverter
    def __init__(self, api_key):
        self.api_key = api_key #se almacena la key de la api 
        self.url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/" #URL para las solicitudes de la API
        
        """_summary_
        Obtiene el tipo de cambio de una moneda a otra.

        Args:
            from_currency (str): Código de la moneda de origen (por ejemplo, 'USD').
            to_currency (str): Código de la moneda de destino (por ejemplo, 'EUR').

        Returns:
            El tipo de cambio como un número de punto flotante, o None si ocurre un error.
        """
    def get_exchange_rate(self, from_currency, to_currency): 
        response = requests.get(self.url + from_currency) # se envia la solicitud a la Api
        data = response.json() #convierte la respuesta
        if response.status_code == 200:#Estado de la peticion
            rates = data['conversion_rates']#Extrae el tipo de cambio
            return rates.get(to_currency, None)# Devuelve el tipo de cambio -destino
        else:
            print(f"Error: {data['error-type']}")

            return None