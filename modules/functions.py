from math import sqrt,gcd,pow
__all__ = ["squareCount","replaceAllBorno"]
async def squareCount(messageContent):
    squarehead = "pozdro squarehead <:squareheadirl:717345147011989534>"
    squareError = "spierdalaj kolasty"
    square = messageContent.replace('square ','')
    args = square.split(' ')
    while args[0] == '':
        args.remove(args[0])
    if len(args) != 3:
        return squareError
    squareMax = max(len(args[0]),len(args[1]))
    squareMax = max(squareMax,len(args[2]))
    if squareMax > 10:
        return squareError
    try:
        a = int(args[0])
        b = int(args[1])
        c = int(args[2])
    except ValueError:
        return squareError
    if a == 0:
        try:
            c = -c
            div = gcd(c,b)
            return f"To nie jest kwadratowe chuju ale ma rozwiązanie:\n{-c//div}/{b//div}\n{squarehead}"
        except ZeroDivisionError:
            return squareError
    mp = dict()
    delta = b*b-4*a*c
    if delta<0:
        return f"Brak rozwiązań - ujemna delta\n{squarehead}"
    elif delta == 0:
        return f"Jedno rozwiązanie: x= {(-b)//(2*a)}\n{squarehead}"
    else:
        sqr = int(sqrt(delta))
        if pow(sqr,2) == delta:
            x1 = -b + sqr
            x2 = -b - sqr
            divide_1 = gcd(x1,2*a)
            divide_2 = gcd(x2,2*a)
            ans_x1 = 0
            if 2*a/divide_1 == 1:
                ans_x1 = x1//divide_1
            else:
                ans_x1 = f"{x1//divide_1}/{2*a//divide_2}"
            if 2*a/divide_2 ==1:
                ans_x2 = x2//divide_2
            else:
                ans_x2 = f"{x2//divide_1}/{2*a//divide_2}"
            return f"Delta: {delta}\nPierwiastek delty: {sqr} \nDwa rozwiązania:\nx1= {ans_x1} \nx2= {ans_x2}\n{squarehead}"
        else:
            ans_delta = delta
            for i in range(2,sqr+2):
                if delta == 1:
                    break
                while delta % i == 0:
                    try:
                        mp[i] += 1
                    except:
                        mp[i] = 1
                    finally:
                        delta //= i
            remainder = 1
            if delta !=1:
                remainder *= delta
            coefficient = 1
            for i in mp:
                if (mp[i]%2):
                    remainder *= i
                coefficient *= int(pow(i,mp[i]//2))
            if coefficient == 1:
                ans_sqrt = f"sqrt({remainder})"
            else:
                ans_sqrt = f"{coefficient} sqrt({remainder})"
            b = -b
            divide_1 = int(gcd(b,2*a))
            divide_1 = int(gcd(divide_1,coefficient))
            divide_2 = int(gcd(b,2*a))
            divide_2 = int(gcd(divide_2,coefficient))
            if 2*a//divide_1==1:
                if coefficient/divide_1==1:
                    ans_x1 = f"{b//divide_1} + sqrt({remainder})"
                else:
                    ans_x1 = f"{b//divide_1} + {coefficient//divide_1} sqrt({remainder})"
            else:
                if coefficient//divide_1==1:
                    ans_x1 = f"({b//divide_1} + sqrt({remainder}) / {2*a//divide_1}"
                else:
                    ans_x1 = f"({b//divide_1} + {coefficient//divide_1}sqrt({remainder}) / {2*a//divide_1}"
            if 2*a//divide_2==1:
                if coefficient // divide_2==1:
                    ans_x2 = f"{b//divide_2} - sqrt({remainder})"
                else:
                    ans_x2 = f"{b//divide_2} - {coefficient//divide_2} sqrt({remainder})"
            else:
                if (coefficient / divide_2 == 1):
                    ans_x2 = f"({b//divide_2} - sqrt({remainder})) / {2*a//divide_2}"
                else:
                    ans_x2 = f"({b//divide_2} - {coefficient//divide_2} sqrt({remainder})) / {2*a//divide_2}"
        return f"Delta: {ans_delta}\nPierwiastek z delty: {ans_sqrt}\nx1= {ans_x1}\nx2= {ans_x2}\n{squarehead}"


def replaceAllBorno(msg):
    while "borno" in msg:
        msg = msg.replace("borno","")
    while "powiedz" in msg:
        msg = msg.replace("powiedz","")
    return (msg if msg != [] and msg.split() != [] else "nie")