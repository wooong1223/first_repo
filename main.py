def check_available():
    return 'It works!'

def split_odd_even(nums=[1, 2, 3, 4]):
    odds = []
    evens = []
    for i in nums:
        if i%2==0:
            evens.append(i)
        else:
            odds.append(i)
    return (odds,evens)

if __name__ == '__main__':
    print(split_odd_even())
