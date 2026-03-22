import httpx

async def get_phone_api(phone_number:str):
    clean_phone = "".join(filter(str.isdigit, phone_number))
    url = "http://localhost:5000/api/v2/numbers"
    payload = {
        "number": clean_phone
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url,json=payload,timeout=20.0)
            print(f"DEBUG: Status {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print("DEBUG: Успешно! Данные получены.")
                return data
            else:
                print(f"DEBUG Error Body: {response.text}")
                return {"error": f"Ошибка {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}
        