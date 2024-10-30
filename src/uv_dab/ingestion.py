from typing import Any

import requests
from dotenv import load_dotenv
from loguru import logger

from uv_dab.constants import VOLUME_PATH
from uv_dab.low_level_functions.utils import save_file

load_dotenv()
API_KEY = "r7ERdL1aEYKBW+S4kgbUAQ==kjLyAm6iKjeXGon6"
# os.getenv("API_KEY")


def download_data() -> dict[str, Any]:
    api_url = "https://api.api-ninjas.com/v1/facts"
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})
    if response.status_code == requests.codes.ok:
        logger.success("Data downloaded successfully")
        return response.text
    else:
        logger.info(f"Error: {response.status_code} {response.text}")


def main():
    data = download_data()
    save_file(path=VOLUME_PATH, data=data)


if __name__ == "__main__":
    main()
