# %%
from unicodedata import name
import requests
import pandas as pd
import datetime
import time


class TokenScanner:
    def __init__(self):
        self.get_eroverse_holders()

    def get_eroverse_holders(self):
        ero_holders = self.scrape_token()
        self.make_csv_file(ero_holders, "ero_holders")

    def make_csv_file(self, file, file_name):
        df = pd.DataFrame.from_records(file)
        df.to_csv(f"{file_name}.csv", index=True)
        return

    def scrape_token(self):
        page_number = 0
        all_ero_holders = []
        while True:
            paginated_holders = self.connect_with_paginated_holders(page_number)
            if not paginated_holders["items"]:
                return all_ero_holders
            all_ero_holders.extend(paginated_holders["items"])
            page_number += 1

    def connect_with_paginated_holders(self, page_number):
        chain_id = 56
        eroverse_token = "0x22cbd249e6c68712da6767f1077b28c87745fa6d"
        url = f"https://api.covalenthq.com/v1/{chain_id}/tokens/{eroverse_token}/token_holders/"
        params = {
            "key": "ckey_1dad0a3f1d16417bb9a340ffe2b",
            "page-number": page_number,
            "page-size": 2000,
        }
        paginated_holders = requests.get(url, params)

        return paginated_holders.json()["data"]


class Collection1Scanner:
    def __init__(self):
        self.get_eroverse_holders()

    def get_eroverse_holders(self):
        ero_holders = self.scrape_nft_collection_1()
        self.make_csv_file(ero_holders, "collection1_holders")

    def make_csv_file(self, file, file_name):
        df = pd.DataFrame.from_records(file)
        df.to_csv(f"{file_name}.csv", index=True)
        return

    def scrape_nft_collection_1(self):
        page_number = 0
        all_nft_collection_1_holders = []
        while True:
            paginated_NFT_coll1_holders = self.connect_with_paginated_NFT1(page_number)
            if not paginated_NFT_coll1_holders["items"]:
                return all_nft_collection_1_holders
            all_nft_collection_1_holders.extend(paginated_NFT_coll1_holders["items"])
            page_number += 1

    def connect_with_paginated_NFT1(self, page_number):
        chain_id = 56
        ero_nft_collection_1_contract = "0xb0dfe92fc62b48611716dc9fa0d3a2187c1c854d"
        url = f"https://api.covalenthq.com/v1/{chain_id}/tokens/{ero_nft_collection_1_contract}/token_holders/"
        params = {
            "key": "ckey_1dad0a3f1d16417bb9a340ffe2b",
            "page-number": page_number,
            "page-size": 2000,
        }
        paginated_holders = requests.get(url, params)
        return paginated_holders.json()["data"]


class Collection2Scanner:
    def __init__(self):
        self.get_eroverse_holders()

    def get_eroverse_holders(self):
        ero_holders = self.scrape_nft_collection_2()
        self.make_csv_file(ero_holders, "collection2_holders")

    def make_csv_file(self, file, file_name):
        df = pd.DataFrame.from_records(file)
        df.to_csv(f"{file_name}.csv", index=True)
        return

    def scrape_nft_collection_2(self):
        page_number = 0
        all_nft_collection_2_holders = []
        while True:
            paginated_NFT_coll2_holders = self.connect_with_paginated_NFT2(page_number)
            if not paginated_NFT_coll2_holders["items"]:
                return all_nft_collection_2_holders
            all_nft_collection_2_holders.extend(paginated_NFT_coll2_holders["items"])
            page_number += 1

    def connect_with_paginated_NFT2(self, page_number):
        chain_id = 56
        ero_nft_collection_1_contract = "0xb0dfe92fc62b48611716dc9fa0d3a2187c1c854d"
        url = f"https://api.covalenthq.com/v1/{chain_id}/tokens/{ero_nft_collection_1_contract}/token_holders/"
        params = {
            "key": "ckey_1dad0a3f1d16417bb9a340ffe2b",
            "page-number": page_number,
            "page-size": 2000,
        }
        paginated_holders = requests.get(url, params)
        return paginated_holders.json()["data"]


class XmasScanner:
    def __init__(self):
        self.get_eroverse_holders()

    def get_eroverse_holders(self):
        ero_holders = self.scrape_nft_xmas()
        self.make_csv_file(ero_holders, "xmas_holders")

    def make_csv_file(self, file, file_name):
        df = pd.DataFrame.from_records(file)
        df.to_csv(f"{file_name}.csv", index=True)
        return

    def scrape_nft_xmas(self):
        page_number = 0
        all_nft_xmas_holders = []
        while True:
            paginated_NFT_xmas_holders = self.connect_with_paginated_xmas(page_number)
            if not paginated_NFT_xmas_holders["items"]:
                return all_nft_xmas_holders
            all_nft_xmas_holders.extend(paginated_NFT_xmas_holders["items"])
            page_number += 1

    def connect_with_paginated_xmas(self, page_number):
        chain_id = 56
        ero_nft_xmas_contract = "0x40a7dc52386ee62d02054575bb66995251A70638"
        url = f"https://api.covalenthq.com/v1/{chain_id}/tokens/{ero_nft_xmas_contract}/token_holders/"
        params = {
            "key": "ckey_1dad0a3f1d16417bb9a340ffe2b",
            "page-number": page_number,
            "page-size": 2000,
        }
        paginated_holders = requests.get(url, params)
        return paginated_holders.json()["data"]


class OriginScanner:
    def __init__(self):
        self.get_eroverse_holders()

    def get_eroverse_holders(self):
        ero_holders = self.scrape_nft_origin()
        self.make_csv_file(ero_holders, "origin_holders")

    def make_csv_file(self, file, file_name):
        df = pd.DataFrame.from_records(file)
        df.to_csv(f"{file_name}.csv", index=True)
        return

    def scrape_nft_origin(self):
        page_number = 0
        all_nft_origin_holders = []
        while True:
            paginated_NFT_origin_holders = self.connect_with_paginated_origin(
                page_number
            )
            if not paginated_NFT_origin_holders["items"]:
                return all_nft_origin_holders
            all_nft_origin_holders.extend(paginated_NFT_origin_holders["items"])
            page_number += 1

    def connect_with_paginated_origin(self, page_number):
        chain_id = 56
        ero_nft_origin_contract = "0xBD35FC23132CA28f2C0e12f2e5EC85b1fCC4d6D9"
        url = f"https://api.covalenthq.com/v1/{chain_id}/tokens/{ero_nft_origin_contract}/token_holders/"
        params = {
            "key": "ckey_1dad0a3f1d16417bb9a340ffe2b",
            "page-number": page_number,
            "page-size": 2000,
        }
        paginated_holders = requests.get(url, params)
        return paginated_holders.json()["data"]


TokenScanner()
Collection1Scanner()
Collection2Scanner()
XmasScanner()
OriginScanner()
