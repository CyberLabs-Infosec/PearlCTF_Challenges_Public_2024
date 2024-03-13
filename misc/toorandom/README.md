## Too random

category : `misc`

type : `on demand`

flag: `pearl{r4nd0m_15_n0t_50_r4nd0m}`

author:`kannaya`

From the given code we can know that we need to find the 1000000th number in the series inorder to obtain the flag . For that we need to obtain the state of the random number generator to find that number.

```py

import requests
import re
from randcrack import RandCrack

url = 'https://toorandom-e6e18b03da9a29f1.ctf.trailblaze.space/dashboard'

numbers = []

for _ in range(624):
    response = requests.get(url)
    match = re.search(r'Number : (\d+)', response.text)
    
    if match:
        number = int(match.group(1))
        print(number)
        numbers.append(number)

```

So for that first we made request to the server and each time we stored the number it is giving to us .

```py

rc = RandCrack()

for random_number in numbers:
    rc.submit(random_number)

```

in this solution we used a module in python called RandCrack . In this it will provide the state of the random number generator from the 625th number after taking the 624 numbers produced by it in sequence. We then gave the randcrack those numbers as input and then we got the state of the random .

```py

for i in range(999376):
    print(f"{rc.predict_getrandbits(32)}")

```

here once after we got the state of the generator we are generating the remaining numbers in order to find the 100000th number.

Unfortunately, due to an oversight in the code I authored, an unintended solution was discovered. It appears that by directly accessing the /flagkeeper directory, the flag can be obtained. This was not the intended method for obtaining the flag, and I apologize for any confusion this may have caused.

