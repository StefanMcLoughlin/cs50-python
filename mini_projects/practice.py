coin = input("Welcher Coin ist dein Favorit? ").lower()

if coin == "btc" or coin == "bitcoin":
    print("Der Klassiker")
elif coin == "sol" or coin == "solana":
    print("Solana Ecosystem")
elif coin == "doge" or coin == "dogecoin":
    print("Meme Power")
else:
    print("Interessante Wahl")