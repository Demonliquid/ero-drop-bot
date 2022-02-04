# %%
import pandas as pd


# %%
class TokenHolder:
    def process(self):
        token_holders = pd.read_csv("ero_holders.csv")
        useful_columns = ["address", "balance"]
        token_holders = token_holders[useful_columns]
        token_holders["balance"] = token_holders["balance"].astype(float)
        token_holders["balance"] = token_holders["balance"] / 1000000000000000000
        token_holders.rename(columns={"balance": "token_balance"}, inplace=True)
        return token_holders


class OriginHolder:
    def process(self):
        origin_holders = pd.read_csv("origin_holders.csv")
        useful_columns = ["address", "balance"]
        origin_holders = origin_holders[useful_columns]
        origin_holders["balance"] = origin_holders["balance"].astype(int)
        origin_holders.rename(columns={"balance": "origin_balance"}, inplace=True)

        return origin_holders


class XmasHolder:
    def process(self):
        xmas_holders = pd.read_csv("xmas_holders.csv")
        useful_columns = ["address", "balance"]
        xmas_holders = xmas_holders[useful_columns]
        xmas_holders["balance"] = xmas_holders["balance"].astype(int)
        xmas_holders.rename(columns={"balance": "xmas_balance"}, inplace=True)
        return xmas_holders


class Collection1Holder:
    def process(self):
        coll1_holders = pd.read_csv("collection1_holders.csv")
        useful_columns = ["address", "balance"]
        coll1_holders = coll1_holders[useful_columns]
        coll1_holders["balance"] = coll1_holders["balance"].astype(int)
        coll1_holders.rename(columns={"balance": "coll1_balance"}, inplace=True)
        return coll1_holders


class Collection2Holder:
    def process(self):
        coll2_holders = pd.read_csv("collection2_holders.csv")
        useful_columns = ["address", "balance"]
        coll2_holders = coll2_holders[useful_columns]
        coll2_holders["balance"] = coll2_holders["balance"].astype(int)
        coll2_holders.rename(columns={"balance": "coll2_balance"}, inplace=True)
        return coll2_holders


# %%
token = TokenHolder().process()
origin = OriginHolder().process()
xmas = XmasHolder().process()
collection1 = Collection1Holder().process()
collection2 = Collection2Holder().process()

# %%
origin_join = pd.merge(token, origin, on="address", how="left")
xmas_join = pd.merge(origin_join, xmas, on="address", how="left")
collection1_join = pd.merge(xmas_join, collection1, on="address", how="left")
final_join = pd.merge(collection1_join, collection2, on="address", how="left")
# %%
final_join.head()

# %%
