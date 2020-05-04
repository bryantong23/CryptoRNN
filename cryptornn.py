import pandas as pd

main_df = pd.DataFrame()

ratios = ["BTC-USD", "LTC-USD", "ETH-USD", "BCH-USD"]
for ratio in ratios:
    dataset = "crypto_data/{}.csv".format(ratio)

    df = pd.read_csv(dataset, names = ["time", "low", "high", "open", "close", "volume"])
    #print(df.head())
    df.rename(columns = {"close": "{}_close".format(ratio), "volume": "{}_volume".format(ratio)}, inplace = True)

    df.set_index("time", inplace = True)
    df = df[["{}_close".format(ratio), "{}_volume".format(ratio)]]

    if (len(main_df)) == 0:
        main_df = df
    else:
        main_df = main_df.join(df)
