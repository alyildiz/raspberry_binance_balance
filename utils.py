def get_capital(client):
    futures_account = client.futures_account()
    for asset in futures_account["assets"]:
        if asset["asset"] == "USDT":
            return str(round(float(asset["marginBalance"]), 2))


def get_current_positions(client):
    futures_account = client.futures_account()
    current_positions = [
        f"{x['symbol']} - {round(float(x['unrealizedProfit']),2)}$"
        for x in futures_account["positions"]
        if float(x["positionAmt"]) > 0
    ]
    return current_positions


def get_value(i, len_word, word_to_print, pixel_length):
    if i < len_word:
        position = 0
        val = len_word - i - 1
        to_print = word_to_print[val:]

    elif i >= pixel_length:
        position = i - len_word + 1
        val = len_word - (i - pixel_length) - 1
        to_print = word_to_print[:val]

    else:
        position = i - len_word + 1
        val = i
        to_print = word_to_print

    return position, to_print
