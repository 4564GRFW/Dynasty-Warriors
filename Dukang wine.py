import time

class Player:
    def __init__(self, name):
        self.name = name

class Creator:
    def __init__(self, name):
        self.name = name

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_dialog(player, creator):
    delay_print(f"欢迎来到《杜康酒的诞生》游戏，{player.name}！")
    delay_print(f"{creator.name}：欢迎，我是杜康酒的创造者。你对杜康酒的故事感兴趣吗？")

    response = input("你想了解更多关于杜康酒的信息吗？(是/否): ").strip().lower()
    if response == "是":
        delay_print(f"{creator.name}：很好，杜康酒是中国传统的美酒之一，有着悠久的历史。")
        delay_print(f"{creator.name}：它的制作过程包括发酵、蒸馏和陈酿，每个步骤都有其独特的技巧。")
        delay_print(f"{creator.name}：杜康酒以其独特的风味和香气而闻名，是中国文化的重要组成部分。")

        choice = input("你想了解关于制作过程的更多信息吗？(是/否): ").strip().lower()
        if choice == "是":
            delay_print(f"{creator.name}：当然，杜康酒的制作过程非常复杂。首先，要选用优质的麦子和水，经过发酵产生酒精。")
            delay_print(f"{creator.name}：然后，将酒精进行蒸馏，去除杂质，提炼出更纯净的液体。")
            delay_print(f"{creator.name}：最后，把液体放入橡木桶中进行陈酿，使其逐渐变得更加丰富和醇香。")

    else:
        delay_print(f"{creator.name}：好的，如果有兴趣随时问我关于杜康酒的问题。")

def main():
    player_name = input("请输入你的名字：")
    player = Player(player_name)
    creator = Creator("杜康酒创造者")

    start_dialog(player, creator)

if __name__ == "__main__":
    main()
