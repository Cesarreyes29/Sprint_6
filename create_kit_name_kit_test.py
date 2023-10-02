import sender_stand_request
import data


# esta función cambia los valores en el parámetro "Name"
def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro Name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor Name requerido
    return current_body

#Función para respuestas positivas
def positive_assert(name):
    # La versión actualizada se guarda en la variable "kit_body"
    kit_body = get_kit_body(name)
    # El resultado de la solicitud relevante se guarda en la variable "name_response"
    name_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.auth_token)

    # Comprueba si el código de estado es 201
    assert name_response.status_code == 201