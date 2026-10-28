alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
codes = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morse = dict(zip(codes.split(), alphabet))
message = '-.-. -.-- -... . .-. / ... . -.-. ..- .-. .. - -.-- / .. ... / . ...- . .-. -.-- --- -. . ... / .-. . ... .--. --- -. ... .. -... .. .-.. .. - -.--'
words = ["".join(morse[group] for group in word.split())
         for word in message.split("/")]
print("_".join(words))
