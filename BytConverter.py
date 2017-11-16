# Work in Progress, by Thibaut Blain (nov.2017)

print("ACCEPTED UNIT INPUTS: ")
print("'b' as bit")
print("'B' as Byte")
print("'kB' as kilobyte")
print("'MB' as Megabyte")
print("'GB' as Gigabyte")
print("'TB' as Terabyte")
print("")

in_num = input("Source Value: ")
s_unit = str(input("Source Unit: "))
b = str("b")
B = str("B")
kB = str("kB")
MB = str("MB")
GB = str("GB")
TB = str("TB")

if s_unit in [b, B, kB, MB, GB, TB]:
    d_unit = str(input("In which unit do you want this value to be converted? : "))
    if d_unit in [b, B, kB, MB, GB, TB]:
        print("OK, Converting " + in_num + s_unit + " to " + d_unit + " ...")
        if s_unit == d_unit:
            print("That's the same; "+ in_num + s_unit + " = " + in_num + d_unit + " ...")
        elif s_unit == b:
            if d_unit == B:
                print("Result: ", (float(in_num) / 8), str(d_unit))
            elif d_unit == kB:
                print("Result: ", ((float(in_num) / 8)/1024), str(d_unit))
            elif d_unit == MB:
                print("Result: ", (((float(in_num) / 8)/1024)/1024), str(d_unit))
            elif d_unit == GB:
                print("Result: ", ((((float(in_num) / 8) / 1024) / 1024) / 1024), str(d_unit))
            elif d_unit == TB:
                print("Result: ", (((((float(in_num) / 8) / 1024) / 1024) / 1024) / 1024), str(d_unit))
        elif s_unit == B:
            if d_unit == b:
                print("Result: ", (float(in_num) * 8), str(d_unit))
            elif d_unit == kB:
                print("Result: ", (float(in_num) / 1024), str(d_unit))
            elif d_unit == MB:
                print("Result: ", ((float(in_num) / 1024 / 1024), str(d_unit)))
            elif d_unit == GB:
                print("Result: ", (((float(in_num) / 1024) / 1024) / 1024), str(d_unit))
            elif d_unit == TB:
                print("Result: ", ((((float(in_num) / 1024) / 1024) / 1024) / 1024), str(d_unit))
        elif s_unit == kB:
            if d_unit == b:
                print("Result: ", ((float(in_num) * 1024) * 8), str(d_unit))
            elif d_unit == B:
                print("Result: ", (float(in_num) * 1024), str(d_unit))
            elif d_unit == MB:
                print("Result: ", ((float(in_num) / 1024), str(d_unit)))
            elif d_unit == GB:
                print("Result: ", ((float(in_num) / 1024) / 1024), str(d_unit))
            elif d_unit == TB:
                print("Result: ", (((float(in_num) / 1024) / 1024) / 1024), str(d_unit))
        elif s_unit == MB:
            if d_unit == b:
                print("Result: ", (((float(in_num) * 1024) * 1024) * 8), str(d_unit))
            elif d_unit == B:
                print("Result: ", ((float(in_num) * 1024) * 1024), str(d_unit))
            elif d_unit == kB:
                print("Result: ", ((float(in_num) * 1024), str(d_unit)))
            elif d_unit == GB:
                print("Result: ", (float(in_num) / 1024), str(d_unit))
            elif d_unit == TB:
                print("Result: ", ((float(in_num) / 1024) / 1024), str(d_unit))
        elif s_unit == GB:
            if d_unit == b:
                print("Result: ", ((((float(in_num) * 1024) * 1024) * 1024) * 8), str(d_unit))
            elif d_unit == B:
                print("Result: ", (((float(in_num) * 1024) * 1024) * 1024), str(d_unit))
            elif d_unit == kB:
                print("Result: ", ((float(in_num) * 1024) * 1024), str(d_unit))
            elif d_unit == MB:
                print("Result: ", (float(in_num) * 1024), str(d_unit))
            elif d_unit == TB:
                print("Result: ", (float(in_num) / 1024), str(d_unit))
        elif s_unit == TB:
            if d_unit == b:
                print("Result: ", (((((float(in_num) * 1024) * 1024) * 1024) * 1024) * 8), str(d_unit))
            elif d_unit == B:
                print("Result: ", ((((float(in_num) * 1024) * 1024) * 1024) * 1024), str(d_unit))
            elif d_unit == kB:
                print("Result: ", ((((float(in_num) * 1024) * 1024) * 1024), str(d_unit)))
            elif d_unit == MB:
                print("Result: ", ((float(in_num) * 1024) * 1024), str(d_unit))
            elif d_unit == GB:
                print("Result: ", (float(in_num) * 1024), str(d_unit))
        print("")
        input("Press ENTER to exit")
    else: print("Bad Unit! Exiting...")
    exit()
else: print("Bad Unit! Exiting...")
exit()