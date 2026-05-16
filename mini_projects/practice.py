Coin = input("Welcher Coin ist dein Favorit? ")
match Coin:
    case "BTC" | "Bitcoin":
        print("Der Klassiker")
    case "SOL" | "Solana":
        print("Solana Ecosystem")
    case "DOGE" | "Dogecoin":
        print("Meme Power")
    case _:
        print("Interessante Wahl")