def num_same_spaces(yesterday, today):
    yesterday_lst = list(yesterday)
    today_lst = list(today)

    match_count = 0

    # for y in yesterday_lst:
    #     for t in today_lst:
    #         if y == t:
    #             match_count += 1
    #             break

    for y in range(len(yesterday_lst)):
        if yesterday_lst[y] == today_lst[y]:
            match_count += 1



    return match_count

print(num_same_spaces("ACACCCCCC", "UCDBCCCCX"))
