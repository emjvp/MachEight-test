def task_pair_integers(num_list, objective_val):
    pair_list = list()

    for i in num_list:
        if objective_val - i in num_list:
            pair_list.append([i, objective_val - i])

    return pair_list


def main():
    pair_list = task_pair_integers([1,9,5,0,20,-4,12,16,7], 12)                        
    print(pair_list)


if __name__ == "__main__":
    main()