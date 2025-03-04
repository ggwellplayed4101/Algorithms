def shell_sort(list):
    gap = len(list) // 2

    while gap > 0:
        for i in range(gap, len(list)):
            temp = list[i]
            j = i - gap

            while j>=0 and temp < list[j]:
                list[j + gap] = list[j]
                j = j - gap 
            
            list[j + gap] = temp
        gap //= 2
        return list

        