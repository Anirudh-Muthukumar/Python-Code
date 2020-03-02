def TowerOfHanoi(n, from_disk, to_disk, extra_disk):
    # Base case
    if n==1:
        print("Move disk 1 from " + from_disk + " to " + to_disk)
        return
    
    # Move disk from from_disk to extra_disk
    TowerOfHanoi(n-1, from_disk, extra_disk, to_disk)

    print("Move disk " + str(n) + " from " + from_disk + " to " + to_disk)

    # Move disk from extra_disk to to_disk
    TowerOfHanoi(n-1, extra_disk, to_disk, from_disk)


if __name__ == '__main__':
    n = 4
    TowerOfHanoi(n, 'A', 'C', 'B')