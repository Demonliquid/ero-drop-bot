store_var_contract = w3.eth.contract(
   address=address,
   abi=contract_interface['abi'])

tx_hash = store_var_contract.functions.withdrawToken(0x..., 50).transact()
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
