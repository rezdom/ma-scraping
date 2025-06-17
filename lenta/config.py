URL_FOR_PRODUCTS = "https://api.lenta.com/v1/catalog/items"

BODY = {
	"categoryId": 136,
	"filters": {
		"multicheckbox": [],
		"checkbox": [],
		"range": []
	},
	"sort": {
		"type": "popular",
		"order": "desc"
	},
	"limit": 26,
	"offset": 0
}

HEADERS = {
    "Content-Type": "application/json",
    "traceparent":"00-aaf698aaf5034e7fb592f1dae6b5c7e4-b6fc53e14f9440b7-01",
    "App-Version":"6.40.0",
    "Timestamp":"1750151172",
    "Qrator-Token":"ca908c54bb9ff4b8d77b47a7bc745ecb",
    "SessionToken":"062D7F34BCD7012C4703D42571CFB52F",
    "DeviceId":"A-2de0c747-2e9c-442f-9691-157475b03521",
    "X-Retail-Brand":"lo",
    "X-Platform":"omniapp",
    "Client":"android_16_6.40.0",
    "AdvertisingId":"ca6a4db8-bb73-41d2-9bbe-2aa3d5ca24c2",
    "User-Agent": "PostmanRuntime/7.44.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",

}