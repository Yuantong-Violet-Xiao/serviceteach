amount = float(input("Please input your amount"))
fen = int(amount * 100)
yuan = fen // 100
remaining = fen % 100
jiao = remaining // 10
fen = remaining % 10
print (f"Your amount {amount:.2f} consists of")
print (f"{yuan:>4} yuan")
print (f"{jiao:>4} jiao")
input (f"{fen:>4} fen")