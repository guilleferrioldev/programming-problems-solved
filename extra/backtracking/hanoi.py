def hanoi(n, from_rod, to_rod, aux_rod):
    # Base case: there is only one disk
    if n == 1:
        print(f"Mover disco 1 de {from_rod} a {to_rod}")
        return

    # Recursive movement of n-1 disks from the source post to the auxiliary post
    # using the target post as an auxiliary 
    hanoi(n - 1, from_rod, aux_rod, to_rod)
    
    print(f"Mover disco {n} de {from_rod} a {to_rod}")
    
    # Recursive movement of n-1 discs from the auxiliary post to the target post
    # using the source post as an auxiliary
    hanoi(n - 1, aux_rod, to_rod, from_rod)


def main(n):
    hanoi(n, 'A', 'C', 'B')
    
if __name__ == "__main__" :
    n = 3  # Number of disks
    main(n)
