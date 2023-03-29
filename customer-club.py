"""
Created by Sorena Nemati(A illiterate)
ساخته شده توسط سورنا نعمتی(یک بی سواد)
"""
# .این فایل برای ثبت شماره ها و نام ها در فایل باشگاه مشتریان است
# This file is for registering numbers and names in the customer club file.
moshtari_ha = open(file="moshtari_ha.txt" , mode="a")
while True:
    name = input("Enter name: ")
    # برای گرفتن نام مشتری ها
    # To get customer names
    tell = input("Enter tell: ")
    # برای گرفتن شماره ی تلفن مشتری ها
    # To get customer phone numbers
    moshtari_ha.write("\n" + name + ": ")
    # اضافه کردن نام مشتری به فایل باشگاه مشتری ها
    # Add customer name to customer club file
    moshtari_ha.write(tell)
    # اضافه کردن شماره ی مشتری به فایل باشگاه مشتری ها
    # Add the customer number to the customer club file
    print("-" * 100)
    continue_while = input("do you want continue work?(y/n) ")
    # برای ادامه دادن یا ندادن کار
    # To continue or not to work
    if "n".lower() in continue_while:
        print("-" * 100)
        break
    elif "y".lower() in continue_while:
        print("-" * 100)
        continue