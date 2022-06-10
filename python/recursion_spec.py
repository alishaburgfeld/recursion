# def bottle_song(num):
#     if num==2:
#         print(f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottle of beer on the wall.")
#         bottle_song(num-1)
#     if num ==1:
#         print(f"{num} bottle of beer on the wall, {num} bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

#     if num > 2:
#         print(f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottles of beer on the wall.")
#         bottle_song(num-1)

# print(bottle_song(10))



# def factorial(num):
#     if num==0:
#         return 1
#     else:
#         return factorial(num-1) * num

# print(factorial(5))



def palindrome(string,start=0):
    end=len(string)-1
    if len(string) ==0 or len(string) == 1:
        return True
    if string[start]==string[end]:
        return palindrome(string[start+1:end])
    else:
        return False

print(palindrome("kayaek"))


# def roman_num(num):
#     answer=""
#     map= {
#         "M": 1000,
#         "CM": 900,
#         "D": 500,
#         "CD": 400,
#         "C": 100,
#         "XC": 90,
#         "L": 50,
#         "XL": 40,
#         "X": 10,
#         "IX": 9,
#         "V": 5,
#         "IV": 4,
#         "I": 1,
#     }

#     for let map in key:

