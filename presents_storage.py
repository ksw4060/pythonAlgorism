from pprint import pprint


def solution(friends, gifts):
    score_friends = {friend: 0 for friend in friends}
    # print(score_friends)

    gr_records = {
        friend: {other: [0, 0] for other in set(friends) - {friend}}
        for friend in friends
    }
    # pprint(gr_record)
    for gift in gifts:
        giver, receiver = gift.split(" ")
        # score_friends[giver] += 1
        gr_records[giver][receiver][0] += 1
        gr_records[receiver][giver][1] += 1
        # print(gr_record)
    pprint(gr_records)
    for gr_record in gr_records.keys():
        for person in gr_records[gr_record].keys():
            give, receive = gr_records[gr_record][person]

            if give > receive:
                score_friends[person] += 1
    print(score_friends)
    max_score = max(score_friends.values())
    if max_score == 0:
        return 0

    count_max_score = sum(1 for score in score_friends.values() if score == max_score)

    # 예측된 선물 받을 친구들에게 선물 수 계산
    predicted_gifts = max_score + 1 if count_max_score > 1 else max_score

    return predicted_gifts


"""
1. 기록이 있을때 a->b : 5 , b->a : 3
    - 많이 준 사람 a: 다음 달에 하나 받는다 (b->a)
2. 기록이 없거나, 주고 받은 수가 같을 때
    - a->b : 5 , b->a : 3 , a->b : 0 , b->a : 0
        1) 선물 지수 = 준 횟수 - 받은 횟수 : 더 적은 사람에게 받는다. (받은게 준거보다 많다.)

    # for friend in set(friends):
    #     others = set(friends) - set(friend)
    #     print("전체 친구들")
    #     pprint(set(friends))
    #     print("그 중에 나는?")
    #     pprint(set(friend))
    #     print("나 제외하고 다른 사람은?")
    #     pprint(others)
    #     gr_record[friend] = {}
    #     for other in others:
    #         gr_record[friend][other] = [0,0]

"""
