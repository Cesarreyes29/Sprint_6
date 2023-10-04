import configuration
import requests
import data
import json


# Función post nuevos usuarios
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body);
if response.status_code == 201:

    auth_token = response.json().get("authToken") #En la función post_new_user agrego estraer el token del nuevo usario

print(response.status_code)
print(response.json())

# Función Post Nuevo Kit


def post_new_client_kit(kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + auth_token; #Aquí uso la variable donde se guardo el token para los headers
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  json=kit_body, headers=headers_dict)


response_post = post_new_client_kit(data.kit_body, auth_token);
if response_post.status_code == 201:
    print(json.dumps(response_post.json()))
else:
    print(f'Error: {response_post.status_code}')
