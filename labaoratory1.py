firstname = "Ken Louis"
middlename = "Queling"
lastname = "Lustre"
age = "18"
fn = firstname + " " + middlename + " " + lastname

print("Hello, my name is", fn, "I am", age, "Years old")

if (fn.isupper == True):
    print(fn)
else:
    new_full = fn.upper()
    print(new_full)