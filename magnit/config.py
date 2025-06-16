LAT = 55.72874956177661 # Moscow coordinates
LONG = 37.691169069335444

URL_FOR_ADDRESS = "https://middle-api.magnit.ru/shops/v1/shop_by_point?x={lat}&y={long}"
URL_FOR_PRODUCTS = "https://middle-api.magnit.ru/recoms/v1/recommendations"

HEADERS = {
    "Content-Type": "application/json; charset=UTF-8",
    "x-app-version": "8.57.0",
    "x-device-id": "52ed5851-1f00-31bc-aabb-9a8e0132e716",
    "x-device-platform": "Android",
    "x-platform-version": "36",
    "x-device-tag": "6D6DCB9C-DF4F-4286-B753-8A03B1A01AFE_F1135163-A14D-484B-8EF5-E7C9BA815FDC",
    "sentry-trace": "64318aeba9304ae88d30368ae28ce100-3e697cc464324e89",
    "baggage": "sentry-environment=production,sentry-public_key=6d4cfb7c8887ad7d38f6d3182a75acda,sentry-release=ru.tander.magnit%408.57.0%2B1149074,sentry-trace_id=64318aeba9304ae88d30368ae28ce100",
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "okhttp/4.12.0"
}

DATA = {
    "catalogType": "2",
    "limit": 100,
    "offset": 0,
    "service": "express",
    "stores": [
        {
            "catalogType": "2",
            "code": None,
            "service": "express"
        },
        {
            "catalogType": "3",
            "code": "shop_group_location_111977_distr",
            "service": "apteka"
        }
    ],
    "type": "main"
}