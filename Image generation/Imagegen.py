import requests

# Generate an image
prompt = "Ram Navami Card Design"
response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"Bearer sk-ncA7ITi7ljJIlNj4XTxdCV6MjBOLE62W3MxkLyDVmoDCfvZA",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": prompt,
        "output_format": "webp",
    },
)

if response.status_code == 200:
    with open("./image1.webp", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))