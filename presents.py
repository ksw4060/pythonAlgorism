from pprint import pprint


def solution(friends, gifts):
    friends = sorted(set(friends))
    give_cnt = {friend: 0 for friend in friends}  # 준 횟수
    receive_cnt = {friend: 0 for friend in friends}  # 받은 횟수
    present_cnt = {friend: 0 for friend in friends}  # 선물 지수
    next_month_cnt = {friend: 0 for friend in friends}  # 다음달에 받는 횟수
    gr_records = {
        friend: {other: [0, 0] for other in set(friends) - {friend}}
        for friend in friends
    }  # 주고 받는 횟수 기록 : 딕셔너리 - 초기화

    for gift in gifts:
        giver, receiver = gift.split(" ")
        give_cnt[giver] += 1
        receive_cnt[receiver] += 1
        gr_records[giver][receiver][0] += 1
        gr_records[receiver][giver][1] += 1
        # 주고 받는 횟수 기록
    # pprint(gr_records)
    give_cnt_list = list(give_cnt.values())
    receive_cnt_list = list(receive_cnt.values())
    present_cnt_list = list(present_cnt.values())
    present_cnt_list = [
        give_cnt_list[i] - receive_cnt_list[i] for i in range(len(friends))
    ]
    present_cnt = {friend: present_cnt_list[i] for i, friend in enumerate(friends)}

    for i in range(len(friends) - 1):
        friend = friends[i]
        others = friends[i + 1 :]
        for other in others:
            AtoB = gr_records[friend][other][0]  # A 가 B 에게 준 것
            BtoA = gr_records[friend][other][1]  # A 가 B 에게 받은 것
            if AtoB > BtoA:
                next_month_cnt[friend] += 1
            elif AtoB < BtoA:
                next_month_cnt[other] += 1
            elif AtoB == BtoA:
                if present_cnt[friend] > present_cnt[other]:
                    next_month_cnt[friend] += 1
                elif present_cnt[friend] < present_cnt[other]:
                    next_month_cnt[other] += 1
                else:
                    next_month_cnt[other] += 0
    # print(next_month_cnt)
    answer = max(list(next_month_cnt.values()))

    return answer
