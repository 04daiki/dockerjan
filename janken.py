import random

def janken(player_hand):
    hands = ["グー", "チョキ", "パー"]
    computer_hand = random.choice(hands)

    print(f"相手の手は{computer_hand}です。")

    if player_hand == computer_hand:
        print("あいこです。")
    elif (player_hand == "グー" and computer_hand == "チョキ") or \
         (player_hand == "チョキ" and computer_hand == "パー") or \
         (player_hand == "パー" and computer_hand == "グー   "):
        print("あなたの勝ちです！")
    else:
        print("あなたの負けです。")

if __name__ == "__main__":
    while True:
        player_hand = input("じゃんけん！ グー、チョキ、パーのいずれかを入力してください（終了する場合はq）：")
        if player_hand == "q":
            break
        janken(player_hand)