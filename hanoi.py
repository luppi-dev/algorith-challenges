def tower_of_hanoi(n, source, aux, target): 
    if n == 1:
        print(f"Moved disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, aux)
    print(f"Moved disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, aux, source, target)
    
num_of_disk = 3;
tower_of_hanoi(num_of_disk, 'A', 'B', 'C')