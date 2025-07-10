def solution(participant, completion):
    participant_count = {}
    answer = ""
    for person in participant:
        participant_count[person] = participant_count.get(person, 0) + 1
    for person in completion:
        participant_count[person] = participant_count.get(person, 0) - 1
    for k, v in participant_count.items():
        if v > 0:
            answer = k
            return answer
    return answer