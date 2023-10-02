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

#Función para respuestas negativas
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)

    name_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.auth_token)
    assert name_response.status_code == 400


# Prueba 1. Creación de un nuevo kit
# El parámetro "Name" contiene un caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("A")

# Prueba 2. Creación de un nuevo kit
# El parámetro "Name" contiene 511 caracteres
def test_create_kit_511_letters_in_name_get_succes_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3. Creación de un nuevo kit
# El parámetro "Name" contiene cero caracteres
def test_create_kit_0_letters_in_name_get_fail_response():
    negative_assert_code_400("")

# Prueba 4. Creación de un nuevo kit
# El parámetro "Name" contiene 512 caracteres
def test_create_kit_512_letters_in_name_get_fail_response():
    negative_assert_code_400(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5. Creación de un nuevo kit
# El parámetro "Name" contiene caracteres especiales
def test_create_kit_special_character_in_name_get_succes_response():
    positive_assert("\"№%@\",")

# Prueba 6. Creación de un nuevo kit
# El parámetro "Name" contiene un espacio
def test_create_kit_space_in_name_get_succes_response():
    positive_assert("A aa")

# Prueba 7. Creación de un nuevo kit
# El parámetro "Name" contiene números
def test_create_kit_numbers_in_name_get_succes_response():
    positive_assert("123")