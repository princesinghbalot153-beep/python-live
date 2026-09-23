# ============================================
#   मेरा पहला Python Program
#   इसमें सब कुछ है जो अब तक सीखा
# ============================================

# ---------- 1. Function: नमस्ते ----------
def namaste(naam):
    print("नमस्ते,", naam, "! 🙏")


# ---------- 2. Function: Calculator ----------
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "0 से भाग नहीं होता!"
        return a / b
    else:
        return "गलत operation"


# ---------- 3. Function: Even / Odd ----------
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


# ---------- 4. Function: Table ----------
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# ---------- 5. Function: Age checker ----------
def age_check(umar):
    if umar >= 60:
        return "Senior citizen"
    elif umar >= 18:
        return "Adult"
    else:
        return "Minor"


# ============================================
#                मुख्य program
# ============================================

print("=" * 40)
print("       मेरा पहला Python Program")
print("=" * 40)

# --- भाग 1: नमस्ते ---
print("\n[1] नमस्ते function:")
namaste("आरव")
namaste("सीता")

# --- भाग 2: Variable और Data Type ---
print("\n[2] Variable और Data Type:")
naam = "राहुल"        # string
umar = 25             # integer
height = 5.8          # float
student = True        # boolean

print("naam   :", naam,    "→ type:", type(naam).__name__)
print("umar   :", umar,    "→ type:", type(umar).__name__)
print("height :", height,  "→ type:", type(height).__name__)
print("student:", student, "→ type:", type(student).__name__)

# --- भाग 3: Calculator ---
print("\n[3] Calculator:")
print("10 + 5 =", calculator(10, 5, "+"))
print("10 - 5 =", calculator(10, 5, "-"))
print("10 * 5 =", calculator(10, 5, "*"))
print("10 / 5 =", calculator(10, 5, "/"))
print("10 / 0 =", calculator(10, 0, "/"))

# --- भाग 4: Even / Odd ---
print("\n[4] Even / Odd:")
for num in [3, 8, 15, 20]:
    print(f"{num} → {even_odd(num)}")

# --- भाग 5: Table ---
print("\n[5] Table of 7:")
table(7)

# --- भाग 6: Age checker ---
print("\n[6] Age Checker:")
for u in [12, 25, 65]:
    print(f"उम्र {u} → {age_check(u)}")

print("\n" + "=" * 40)
print("        Program खत्म! ✅")
print("=" * 40)
