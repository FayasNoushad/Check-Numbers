```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/Check-Numbers/blob/main/LICENSE
```

---

## Installation

```
pip install Check-Numbers
```

---

## Usage

### Check Zero

```py
from check_numbers import is_zero


print(is_zero(0))
# => True
print(is_zero(1))
# => False
print(is_zero(-1))
# => False
```

### Check Positive

```py
from check_numbers import is_positive


print(is_positive(1))
# => True
print(is_positive(0))
# => False
print(is_positive(-1))
# => False
```

### Check Negative

```py
from check_numbers import is_negative


print(is_negative(-1))
# => True
print(is_negative(0))
# => False
print(is_negative(1))
# => False
```

### Check Odd

```py
from check_numbers import is_odd


print(is_odd(1))
# => True
print(is_odd(0))
# => False
print(is_odd(2))
# => False
```

### Check Even

```py
from check_numbers import is_even


print(is_even(2))
# => True
print(is_even(0))
# => False
print(is_even(1))
# => False
```

### Check Prime

```py
from check_numbers import is_prime


print(is_prime(5))
# => True
print(is_prime(0))
# => False
print(is_prime(1))
# => False
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
