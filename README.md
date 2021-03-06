# Just-Mining-Com-API
Python wrapper for just-mining.com API. 

Official documentation: https://docs.just-mining.com/

## Install
`python -m pip install -U just-mining-com-api`

## Usage
```
from just_mining_com_api import JustMining

if __name__ == '__main__':
    API_KEY = 'MY_JUST_MINING_API_KEY'
    jm = JustMining(API_KEY)

    masternodes = jm.masternodes()
    print(f"Masternodes: {len(masternodes)}")
    print(masternodes)

    clouds = jm.clouds()
    print(f"Clouds: {len(clouds)}")
    print(clouds)

    cloud_id = 'CLOUD_ID'
    cloud = jm.clouds(cloud_id)
    print(f"Cloud {cloud_id}:")
    print(cloud)

    stackings = jm.stakings()
    print(f"Stackings: {len(stackings)}")
    print(stackings)

    currency_code = 'OSMO'
    stacking = jm.stakings(currency_code)
    print(f"Stacking {currency_code}:")
    print(stacking)

    lendings = jm.lendings()
    print(f"Lendings: {len(lendings)}")
    print(lendings)

    currency_code = 'USDT'
    lending = jm.lendings(currency_code)
    print(f"Lending {currency_code}:")
    print(lending)

    wallets = jm.wallets()
    print(f"Wallets: {len(wallets)}")
    print(wallets)

    wallet_addresses = jm.wallet_addresses()
    print(f"Wallet addresses: {len(wallet_addresses)}")
    print(wallet_addresses)

    operations = jm.operations()
    print(f"Operations: {len(operations)}")
    print(operations)

    operation_id = 'OPERATION_ID'
    operation = jm.operations(operation_id)
    print(f"Operation {operation}")
    print(operation)
```
