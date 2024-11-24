import requests

# Configura el rango de números que deseas probar
start = 0
end = 9999

# URL base
base_url = "https://hackaton2024.useitapps.com/"

# Lista para almacenar los números con status 200
successful_numbers = []

# Realiza las solicitudes en el rango especificado
for number in range(start, end + 1):
    try:
        # Genera la URL
        url = f"{base_url}{number}"

        # Realiza la solicitud GET
        response = requests.get(url)
        # Comprueba si el estado es 200
        if response.status_code == 200:
            print(f"¡Número encontrado! {number} devuelve 200")
            successful_numbers.append(number)
    except Exception as e:
        print(f"Error al procesar el número {number}: {e}")
        continue

# Muestra todos los números exitosos
print("Números con status 200:")
print(successful_numbers)