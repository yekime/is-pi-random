# is-pi-random
## **Are the digits of pi random?**

  ![image](https://user-images.githubusercontent.com/56771911/173252966-3d55c281-0fab-44fb-a80b-1f19281f3cc4.png)<br>
### Beautiful, poetic, and pure conjecture. <br>
$\pi$ is indeed an infinite, non-repeating decimal, but so are the following:
- 0.1234567891011121314...
- 0.1010010001000010000...
- 0.1223334444555556666...

<br>None of these are random, and you most definitely are not going to find the next winning lottery number in any of these sequences. If we want to discuss the validity of the quote's claims, we need to find a more robust method of <br><br>
$\pi$ can't be random, as they have fixed, determined digits, and we are able to calculate every single one. It makes more sense to ask whether $\pi$ is a [normal number](https://en.wikipedia.org/wiki/Normal_number). If it is, then the quote above is accurate due to the [infinite monkey theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem#:~:text=The%20infinite%20monkey%20theorem%20states,an%20infinite%20number%20of%20times).<br>
### Setup:
1 million digits of $\pi$ stored as ASCII should be roughly 1 MB (1 byte per character, 1024 B $\times$ 1024 B $\approx$ 1 MB).
While not an excessive amount of data to store in this repo, a simple API request makes this a lot easier.
```
NUM_DIGITS = 1000000
URL = "https://uploadbeta.com/api/pi/"
response = requests.get(f"{URL}/?cached&n={NUM_DIGITS}")
```
Make sure you have Python and pip, and run ```pip install -r requirements.txt```

## Test 1: 

| Figure 1                                                                                                           | Analysis                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| ![Figure_1](https://user-images.githubusercontent.com/56771911/173251186-a2a10ae7-df9d-48bc-9984-b9bd21ba3b1a.png) | Chi squared statistic: 5.511 <br> p-value: 0.788<br>Time taken: 0.479s <br><br> Thus, digits seem equally distributed. |


## Test 2:
| Figure 2                                                                                                           | Analysis                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| ![Figure_2](https://user-images.githubusercontent.com/56771911/173251188-0f45291b-154e-41e8-922f-848a94a83da6.png) | Chi squared statistic: 94.26  <br>p-value: 0.616<br>Time taken: 0.776s <br><br> Thus, digits seem independent of its neighbors. |

## Test 3:
| Figure 3                                                                                                           | Analysis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Figure_3](https://user-images.githubusercontent.com/56771911/173251189-c3579f52-c606-43e3-8521-4af8990eb0ee.png) | T Stat:         : 0.123  p-value: 0.900 <br>T Stat:         : 0.811    p-value: 0.417<br>T Stat:         : -0.0911  p-value: 0.927<br>T Stat:         : -0.772   p-value: 0.440<br>T Stat:         : -0.766   p-value: 0.444<br>T Stat:         : -1.19   p-value: 0.234<br>T Stat:         : 1.51      p-value: 0.132<br>T Stat:         : 0.665    p-value: 0.506<br>T Stat:         : 0.0487   p-value: 0.961<br>T Stat:         : -0.352  p-value: 0.724<br><br>Thus, space between identical digits is ~10. |

### Conclusion:
These tests do not, in any sense, prove the random distribution of the digits of $\pi$. <br><br>It does however show one statistical interpretation of it: close enough
