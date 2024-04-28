import yfinance as yf

def handler(event, context):
    print(event)

    currency_pair = "SGDMYR=X"

    live_data = yf.download(currency_pair, period="1d", interval="1m")

    print(live_data)

    sgd_myr = live_data["Close"].iloc[-1]

    print(f"SGD to MYR rate: {sgd_myr:.4f}")
    
    # send sns if larger then configured rate