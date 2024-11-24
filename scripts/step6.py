import itertools
import requests

if __name__ == '__main__':
    l = ["H","R","E","S","A","D","I","E","O","B","E","T","R"]
    base_url = "https://hackaton2024.useitapps.com/"

    for v in itertools.permutations(l):
        path = "-".join(v)
        try:
            # Genera la URL
            url = f"{base_url}{path}"
            print(path)
            # Realiza la solicitud GET
            response = requests.get(url)
            # Comprueba si el estado es 200
            if response.status_code == 200:
                print(f"¡Número encontrado! {path} devuelve 200")
                break
        except Exception as e:
            print(f"Error al procesar el número {path}: {e}")
            continue

