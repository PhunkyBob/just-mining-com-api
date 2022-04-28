from just_mining_com_api import JustMining


if __name__ == '__main__':
    API_KEY = input("Enter your API key: ")
    jm = JustMining(API_KEY)

    masternodes = jm.masternodes()
    print(f"Masternodes: {len(masternodes)}")
    print(masternodes)

    clouds = jm.clouds()
    print(f"Clouds: {len(clouds)}")
    print(clouds)

    # cloud_id = 'CLOUD_ID'
    # cloud = jm.clouds(cloud_id)
    # print(f"Cloud {cloud_id}:")
    # print(cloud)

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
