from collections import Counter

def main():
    list_new = ["a","a","b","b","c","c","c"]
    print(list(Counter(list_new))[0])
    print(list(Counter(list_new).values()))
    print(list(Counter(list_new).keys()))


main()
