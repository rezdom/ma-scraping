import json, requests
import magnit.config as config

def get_shop_code(url: str, latitude: float, logitude: float):
    response = requests.get(url.format(lat=latitude, long=logitude), headers=config.HEADERS)
    code = response.json()["shops"][0]["xml_id"]
    return code

def get_products_data(url: str, data: dict):
    response = requests.post(url, headers=config.HEADERS, json=data)
    return response.json()

def load_data(path:str):
    data = config.DATA
    code = get_shop_code(config.URL_FOR_ADDRESS, config.LAT, config.LONG)
    data["stores"][0]["code"] = code
    summary_data = 0
    steps = 0
    cards = []
    while (summary_data < 100 and steps < 16):
        print(f"magnit's page {steps} | {summary_data}")
        products = get_products_data(config.URL_FOR_PRODUCTS, data)["items"]
        summary_data += len(products)
        steps += 1
        for i in range(len(products)):
            cards.append({"id":products[i]["id"],
                          "name":products[i]["name"],
                          "regular price":products[i]["promotion"]["oldPrice"]/100 if products[i]["promotion"]["oldPrice"] is not None else products[i]["price"]/100,  
                          "promo price":products[i]["price"]/100 if products[i]["promotion"]["oldPrice"] is not None else None, 
                          "brand":None})
        data["offset"] += data["limit"]
    with open(path, 'a', encoding='utf-8') as f:
            json.dump(cards, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    load_data("magnit/magnit_result.json")