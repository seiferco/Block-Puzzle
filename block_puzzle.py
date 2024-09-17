def b_place_num_ways(n):

    if n < 0:
        return 0
    
    if n == 0:
        return 1

    else:
        return b_place_num_ways(n - 1) + b_place_num_ways(n - 2)
    

def place_num_ways(n, dict):

    if n < 0:
        return 0
    
    if n == 0:
        return 1
     
    if n in dict:
        return dict[n]

    else:
        dict[n] = place_num_ways(n - 1, dict) + place_num_ways(n - 2, dict)
    
    return dict[n]
    


def main():

    dict = {}
    n = 4
    ans = b_place_num_ways(n)

    print(f"Num ways: {ans}")
main()