# Baby Jail

Python character / regex based filtered can be easily bypassed using strings that are not normalised.

```python
>>>'𝘧𝘭𝘢𝘨'=="flag"
False
>>>'f' in '𝘧𝘭𝘢𝘨'
False
```

However when python executes the eval function it by defaults normalizes that command before running.

So something like '𝘧𝘭𝘢𝘨' should give the flag.

Flag:pearl{it_w4s_t00_e4sy}
