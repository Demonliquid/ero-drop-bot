# %%
import pandas as pd
import requests
from collections import Counter


# %%
def collection1_add_ids(coll1):
    for address in coll1["address"]:
        try:
            condicion = coll1["address"] == address
            coll1.loc[condicion, "coll1_ids"] = ",".join(coll1_add_columns(address))
        except:
            pass


def collection2_add_ids(coll2):
    for address in coll2["address"]:
        try:
            condicion = coll2["address"] == address
            coll2.loc[condicion, "coll2_ids"] = ",".join(coll2_add_columns(address))
        except:
            pass


def coll1_add_columns(holder_address):
    account_nft_balance = get_coll1_NFT_balance(holder_address)
    nfts_user_currently_has = get_coll1_nft_ids_holders(account_nft_balance)

    return nfts_user_currently_has


def coll2_add_columns(holder_address):
    account_nft_balance = get_coll2_NFT_balance(holder_address)
    nfts_user_currently_has = get_coll2_nft_ids_holders(account_nft_balance)

    return nfts_user_currently_has


def get_coll1_NFT_balance(holder_address):
    bscscan_api_key = "T6R9ZY3EPH1D7MRH2X3V8VW6WRK6F4YH2F"
    coll1_contract = "0xb0dfe92fc62b48611716dc9fa0d3a2187c1c854d"
    url = f"https://api.bscscan.com/api?module=account&action=tokennfttx&contractaddress={coll1_contract}&address={holder_address}&page=1&offset=100&startblock=0&endblock=999999999&sort=asc&apikey={bscscan_api_key}"
    response = requests.get(url)
    data = response.json()
    return data["result"]


def get_coll2_NFT_balance(holder_address):
    bscscan_api_key = "T6R9ZY3EPH1D7MRH2X3V8VW6WRK6F4YH2F"
    coll2_contract = "0x4502eb52a587d58b339576dbe3b09f96aeb54dd1"
    url = f"https://api.bscscan.com/api?module=account&action=tokennfttx&contractaddress={coll2_contract}&address={holder_address}&page=1&offset=100&startblock=0&endblock=999999999&sort=asc&apikey={bscscan_api_key}"
    response = requests.get(url)
    data = response.json()
    return data["result"]


def get_coll1_nft_ids_holders(account_nft_balance):
    all_nft_transaction_ids = []
    for nft in account_nft_balance:
        if nft["tokenSymbol"] == "ECLC":
            all_nft_transaction_ids.append(nft["tokenID"])
    nft_count = Counter(all_nft_transaction_ids)
    nfts_user_currently_has = []
    for nft_id in nft_count:
        if nft_count[nft_id] % 2 != 0:
            nfts_user_currently_has.append(nft_id)
    return nfts_user_currently_has


def get_coll2_nft_ids_holders(account_nft_balance):
    all_nft_transaction_ids = []
    for nft in account_nft_balance:
        if nft["tokenSymbol"] == "ECLC2":
            all_nft_transaction_ids.append(nft["tokenID"])

    nft_count = Counter(all_nft_transaction_ids)

    nfts_user_currently_has = []
    for nft_id in nft_count:
        if nft_count[nft_id] % 2 != 0:
            nfts_user_currently_has.append(nft_id)
    return nfts_user_currently_has


# %%
coll1 = pd.read_csv(r"collection1_holders.csv")
coll2 = pd.read_csv(r"collection2_holders.csv")

# %%
collection1_add_ids(coll1)
collection2_add_ids(coll2)

# %%
coll1
# %%
