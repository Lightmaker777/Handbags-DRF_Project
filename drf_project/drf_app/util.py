# drf_app/util.py
import requests

def get_brand_description(brand_name, description):
    url = "https://brand-description.p.rapidapi.com/brand-description"

    # Set up query parameters
    query_params = {"name": brand_name, "description": description}

    headers = {
        "X-RapidAPI-Key": "b6d8fc5d92mshff2a486382bc8d3p177f0djsn4af3fde4f5f7",  # Replace with your actual API key
        "X-RapidAPI-Host": "brand-description.p.rapidapi.com",
    }

    try:
        response = requests.get(url, headers=headers, params=query_params)

        if response.status_code == 200:
            # Request was successful
            brand_description = response.json()
            return brand_description
        else:
            # Handle unsuccessful response
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print(f"Error: {e}")
