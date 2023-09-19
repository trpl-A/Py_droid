
class Mathematics:
    # def isPrime(num):
    #     for z in range(2, num):
    #         if num % z == 0:
    #             # print("composite")
    #             print(f"{num} is a composite number")
    #             break

    #         else:
    #             return True                


    def isMultiple(pmultiple, num):
        if pmultiple % num == 0:
            return True
        else:
            return False


    def isFactor(pfactor, num):
        if num % pfactor == 0:
            return True
        else:
            return False

# *********************************************


# a = Mathematics.isFactor(21, 440)
# print(a)
