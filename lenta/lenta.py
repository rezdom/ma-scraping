import json, requests
import lenta.config as config

def get_products_data(url: str, data: dict):
    response = requests.post(url, json=data, headers=config.HEADERS)
    return response.json()

def load_data(path:str):
    data = config.BODY
    summary_data = 0
    steps = 0
    cards = []
    while (summary_data < 100 and steps < 16):
        print(f"lenta's page {steps} | {summary_data}")
        products = get_products_data(config.URL_FOR_PRODUCTS, data)["items"]
        summary_data += len(products)
        steps += 1
        for i in range(len(products)):
            cards.append({"id":products[i]["id"],
                          "name":products[i]["name"],
                          "regular price":products[i]["prices"]["priceRegular"]/100,  
                          "promo price":products[i]["prices"]["price"]/100, 
                          "brand":None})
        data["offset"] += data["limit"]
    with open(path, 'a', encoding='utf-8') as f:
            json.dump(cards, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    load_data("lenta/lenta_result.json")