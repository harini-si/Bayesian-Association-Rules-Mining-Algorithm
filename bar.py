import csv
import itertools

"""prompt user to enter support and confidence values in percent"""

support = int(input("Please enter support value in %: "))
confidence = int(input("Please enter confidence value in %: "))

"""Compute candidate 1-itemset"""
C1 = {}
"""total number of transactions contained in the file"""
transactions = 0
D = []
T = []
with open("data/breast-cancer.txt", "r") as f:
    for line in f:
        T = []
        transactions += 1
        for word in line.split():
            T.append(word)
            if word not in C1.keys():
                C1[word] = 1
            else:
                count = C1[word]
                C1[word] = count + 1
        D.append(T)


"""Compute frequent 1-itemset"""
L1 = []
for key in C1:
    if (100 * C1[key] / transactions) >= support:
        list = []
        list.append(key)
        L1.append(list)

"""apriori_gen function to compute candidate k-itemset, (Ck) , using frequent (k-1)-itemset, (Lk_1)"""


def apriori_gen(Lk_1, k):
    length = k
    Ck = []
    for list1 in Lk_1:
        for list2 in Lk_1:
            count = 0
            c = []
            if list1 != list2:
                while count < length - 1:
                    if list1[count] != list2[count]:
                        break
                    else:
                        count += 1
                else:
                    if list1[length - 1] < list2[length - 1]:
                        for item in list1:
                            c.append(item)
                        c.append(list2[length - 1])
                        if not has_infrequent_subset(c, Lk_1, k):
                            Ck.append(c)
                            c = []
    return Ck


"""function to compute 'm' element subsets of a set S"""


def findsubsets(S, m):
    return set(itertools.combinations(S, m))


"""has_infrequent_subsets function to determine if pruning is required to remove unfruitful candidates (c) using the Apriori property, with prior knowledge of frequent (k-1)-itemset (Lk_1)"""


def has_infrequent_subset(c, Lk_1, k):
    list = []
    list = findsubsets(c, k)
    for item in list:
        s = []
        for l in item:
            s.append(l)
        s.sort()
        if s not in Lk_1:
            return True
    return False


"""frequent_itemsets function to compute all frequent itemsets"""


def frequent_itemsets():
    k = 2
    Lk_1 = []
    Lk = []
    L = []
    count = 0
    transactions = 0
    for item in L1:
        Lk_1.append(item)
    while Lk_1 != []:
        Ck = []
        Lk = []
        Ck = apriori_gen(Lk_1, k - 1)
        for c in Ck:
            count = 0
            transactions = 0
            s = set(c)
            for T in D:
                transactions += 1
                t = set(T)
                if s.issubset(t) == True:
                    count += 1
            if (100 * count / transactions) >= support:
                c.sort()
                Lk.append(c)
        Lk_1 = []
        for l in Lk:
            Lk_1.append(l)
        k += 1
        if Lk != []:
            L.append(Lk)

    return L


data = []

"""generate_association_rules function to mine and print all the association rules with given support and confidence value"""
header = ["A", "B", "support", "confidence", "bayesian confidence", "bayesian lift"]
with open("data/output.csv", "w", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(header)


def generate_association_rules():
    s = []
    r = []
    length = 0
    count = 1
    inc1 = 0
    inc2 = 0
    inc3 = 0
    num = 1
    m = []
    L = frequent_itemsets()
    for list in L:
        for l in list:
            length = len(l)
            count = 1
            while count < length:
                s = []
                r = findsubsets(l, count)
                count += 1
                for item in r:
                    inc1 = 0
                    inc2 = 0
                    s = []
                    m = []

                    for i in item:
                        s.append(i)
                    for T in D:
                        if set(s).issubset(set(T)) == True:
                            inc1 += 1
                            # print(set(s))
                            # print(set(T))
                        if set(l).issubset(set(T)) == True:

                            inc2 += 1
                            # print(l)

                    if 100 * inc2 / inc1 >= confidence:
                        for index in l:
                            if index not in s:
                                m.append(index)
                        # print(set(m))

                        inc3 = 0
                        inc4 = 0
                        for T in D:
                            setp = set(s).union(set(m))
                            # find the number of items in a set

                            L = len(setp)

                            if set(setp).issubset(set(T)) == True:
                                inc3 += 1
                            if set(m).issubset(set(T)) == True:
                                inc4 += 1

                        # bayesian confidence
                        bc = ((inc3 / inc1) ** L) * 100
                        # bayesian lift
                        bl = (bc / inc4) * len(D) / 100
                        print(
                            "Rule#  %d : %s ==> %s %d %d %d %f"
                            % (
                                num,
                                s,
                                m,
                                100 * inc2 / len(D),
                                100 * inc2 / inc1,
                                bc,
                                bl,
                            )
                        )
                        num += 1
                        data = [s, m, 100 * inc2 / len(D), 100 * inc2 / inc1, bc, bl]
                        with open("data/output.csv", "a", encoding="UTF8") as f:
                            writer = csv.writer(f)

                            # write the data
                            writer.writerow(data)


generate_association_rules()


print("--------------------------------------------------------")
