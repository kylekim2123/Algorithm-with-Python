# 1928. Base64 Decoder

import base64

results = list()
for t in range(1, int(input()) + 1):
    base64_string = input()
    decoded_base64_string = base64.b64decode(base64_string).decode("ascii")
    results.append(f'#{t} {decoded_base64_string}')

for result in results:
    print(result)