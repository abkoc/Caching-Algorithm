import numpy as np
from collections import deque
popularity = deque([])
num_ref = np.zeros(100)
num_files = 0
sizes=np.zeros(100)
convergence = 0
give_up=[]
time=0
cache_files = []
T1 = deque([])
T2 = deque([])
T3 = deque([])
size_T1 = 100
size_T2 = 100
size_T3 = 100
run_start = 0


def cache_decision_sample(my_cache, file, file_size):
    if file not in my_cache.stored_files:
        # If the cache capacity is full,
        # remove the last accessed files from the cache until there is enough space for the new file.
        if my_cache.cache_size + file_size < my_cache.cache_capacity:
            my_cache.store_in_cache(file)
        else:
            while my_cache.cache_size + file_size > my_cache.cache_capacity:
                my_cache.remove_from_cache(min(my_cache.timestamp, key=my_cache.timestamp.get))
            my_cache.store_in_cache(file)

# You will fill inside this function for part 1. You can only use the information given in the arguments.
def cache_decision_part1(my_cache, file, file_popularity, file_sizes):
    if file not in my_cache.stored_files:
        if my_cache.cache_size + min(file_sizes) < my_cache.cache_capacity:
            sorted_popularity=sorted(file_popularity, reverse=True)
            sum=0
            cache_files = []
            for i in range(100):
                ind=np.where(file_popularity == sorted_popularity[i])
                if sum+file_sizes[ind]<my_cache.cache_capacity:
                    cache_files.append(ind)
                    sum+=file_sizes[ind]
            if file in cache_files:
                my_cache.store_in_cache(file)

# You will fill inside this function for part 2. You can only use the information given in the arguments.
def cache_decision_part2(my_cache, file, file_size):
    global num_ref
    global num_files
    global give_up
    global sizes
    global convergence
    global time
    global cache_files
    if my_cache.cache_size == 0:
        num_ref = np.zeros(100)
        num_files = 0
        print(num_files)
        sizes=np.zeros(100)
        convergence = 0
        give_up=[]
        time=0
        cache_files = []

    sizes[file]=file_size
    num_ref[file]+=1
    time+=1
    # print(time)
    # print('num_nonzero=',np.count_nonzero(num_ref))

    if np.count_nonzero(num_ref) != num_files:
        # print('convergence check')
        num_files = np.count_nonzero(num_ref)
        if num_files > 55:
            if np.sum(num_ref) > 4096:
                if np.sum(sizes[np.nonzero(num_ref)]) >= my_cache.cache_capacity:
                    convergence=1
        else:
            convergence=0
    # print('convergence=',convergence)
    # print(num_ref)
    # print('cache capacity',my_cache.cache_capacity)
    # print('cache size',my_cache.cache_size)
    # print('file=',file)
    # print('file size=',file_size)
    # print('file num_ref=',num_ref[file])
    # print('num_ref=',num_ref)
    if convergence == 1:
        if len(cache_files) == 0:
            sorted_popularity = sorted(num_ref, reverse=True)
            sum=0
            for i in range(100):
                ind=np.array(np.where(num_ref == sorted_popularity[i]))[0]
                # print(ind)
                for j in ind:
                    sum+=sizes[j]
                    if sum+sizes[j]<my_cache.cache_capacity:
                        cache_files.append(j)

        if file not in my_cache.stored_files:
            if file in cache_files:
                for j in my_cache.stored_files:
                    if j not in cache_files:
                        my_cache.remove_from_cache(j)
                    if my_cache.cache_size + file_size < my_cache.cache_capacity:
                        my_cache.store_in_cache(file)
                        break
    else:
        if file not in my_cache.stored_files:
        # If the cache capacity is full,
        # remove the last accessed files from the cache until there is enough space for the new file.
            if my_cache.cache_size + file_size < my_cache.cache_capacity:
                my_cache.store_in_cache(file)
                if file not in my_cache.stored_files:
                    print('cache capacity',my_cache.cache_capacity)
                    print('cache size',my_cache.cache_size)
                    print('file=',file)
                    print('file size=',file_size)

            elif file in give_up:
                pass
            else:
                # print('cache',my_cache.stored_files)
                num_ref_filtered=[num_ref[i] for i in np.arange(100) if i in my_cache.stored_files]
                # print('number of references of stored files=',num_ref_filtered)
                if num_ref[file]>=min(num_ref_filtered):
                    for i in np.arange(min(num_ref_filtered),max(num_ref_filtered),1):
                        z = [j for j in my_cache.stored_files if num_ref[j]==i]
                        while my_cache.cache_size + file_size > my_cache.cache_capacity:
                            # print('z=',z)
                            if len(z) == 0:
                                break
                            else:
                                # print('z',z)
                                my_cache.remove_from_cache(z[0])
                                # print('cache size after remove',z[0],my_cache.cache_size)
                                z = z[1:len(z)]
                                # print('new z',z)
                    if my_cache.cache_size + file_size < my_cache.cache_capacity:
                        my_cache.store_in_cache(file)
                    else:
                        give_up.append(file)

# You will fill inside this function for part 3. You can only use the information given in the arguments.
def cache_decision_part3(my_cache, file, file_size):
    global T1, T2, T3
    global run_start
    if run_start == 1:
        if my_cache.cache_size == 0:
            T1 = deque([])
            T2 = deque([])
            T3 = deque([])
            run_start = 0

    sizes[file]=file_size
    if file not in my_cache.stored_files:
        if file in T3:
            if my_cache.cache_size + file_size < my_cache.cache_capacity:
                my_cache.store_in_cache(file)
                run_start = 1
        else:
            if file in T2:
                T3.append(file)
            else:
                if file in T1:
                    T2.append(file)
                else:
                    T1.append(file)