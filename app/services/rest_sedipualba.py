def crear_ciudadano_rest(payload):
    url = f'{base_url}/api/ciudadano/new'
    return requests.post(url, json=payload, headers=get_headers())