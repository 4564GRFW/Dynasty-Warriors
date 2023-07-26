import time
import random

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return self.name

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)
        self.level = 1
        self.exp = 0
        self.inventory = {}
        self.is_dead = False

    def add_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity

    def remove_item(self, item, quantity=1):
        if item.name in self.inventory:
            if self.inventory[item.name] >= quantity:
                self.inventory[item.name] -= quantity
                return True
            else:
                return False
        else:
            return False

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def delay_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.3)

def show_inventory(player):
    print("\n你的背包：")
    for item_name, quantity in player.inventory.items():
        print(f"{item_name}: {quantity}个")

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 查看角色状态")
    print("2. 查看背包")
    print("3. 探险")
    print("4. 完成任务")
    print("5. 自由交易")
    print("6. PK")
    print("7. 退出游戏")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3/4/5/6/7）："))
            if 1 <= choice <= 7:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def show_character_status(player):
    print(f"\n{name}等级：{player.level}")
    print(f"生命值：{player.health}")
    print(f"攻击力：{player.attack}")
    print(f"经验值：{player.exp}/{player.level * 100}")

def explore(player):
    delay_print("\n你踏上了三国历险的旅程。")
    encounter = random.choice(["monster", "item", "nothing"])
    
    if encounter == "monster":
        monster_attack(player)
    elif encounter == "item":
        collect_item(player)
    else:
        delay_print("这片区域看起来平静无事。")

def monster_attack(player):
    delay_print("\n突然，一只敌对角色出现在你面前！")
    enemy = Character("敌对角色", random.randint(50, 100), random.randint(10, 30))
    while player.health > 0 and not player.is_dead:
        delay_print(f"\n你的生命值：{player.health}  敌对角色的生命值：{enemy.health}")
        player.attack_enemy(enemy)
        if enemy.health <= 0:
            delay_print("你击败了敌对角色！")
            player.exp += 50
            break
        else:
            delay_print("敌对角色反击了！")
            player.enemy_attack(enemy)

    if player.is_dead:
        delay_print("你被敌对角色击败了，游戏结束。")

def collect_item(player):
    item = random.choice(item_list)
    quantity = random.randint(1, 5)
    player.add_item(item, quantity)
    delay_print(f"你发现了{item.name} x {quantity}。")

def trade_items(player1, player2):
    print(f"\n欢迎来到交易所，{player1.name}和{player2.name}！")
    show_inventory(player1)
    show_inventory(player2)

    item_name = input(f"{player1.name}，请输入你要交易的道具名字：")
    if item_name not in player1.inventory:
        delay_print(f"{player1.name}没有该道具，无法交易。")
        return

    quantity = int(input(f"{player1.name}，请输入你要交易的{item_name}数量："))
    if player1.inventory[item_name] < quantity:
        delay_print(f"{player1.name}没有足够的{item_name}，无法交易。")
        return

    price = int(input(f"{player2.name}，请输入你愿意出售{item_name}的价格："))
    if price <= 0:
        delay_print(f"{player2.name}价格必须为正整数。")
        return

    total_cost = price * quantity
    if total_cost > player2.inventory.get("铜板", 0):
        delay_print(f"{player2.name}没有足够的铜板，无法交易。")
        return

    player1.remove_item(Item(item_name), quantity)
    player1.add_item(Item(item_name), quantity)
    player1.inventory["铜板"] += total_cost
    player2.remove_item(Item(item_name), quantity)
    player2.inventory["铜板"] -= total_cost

    delay_print(f"交易完成！{player1.name}交易了{quantity}个{item_name}，支付了{total_cost}个铜板。")
    show_inventory(player1)
    show_inventory(player2)

def pk(player1, player2):
    print(f"\n{player1.name}和{player2.name}开始PK！")
    while player1.health > 0 and player2.health > 0:
        delay_print(f"\n{player1.name}的生命值：{player1.health}  {player2.name}的生命值：{player2.health}")
        player1.attack_enemy(player2)
        if player2.health <= 0:
            delay_print(f"{player1.name}击败了{player2.name}，获得了胜利！")
            player1.exp += 100
            player2.is_dead = True
            break
        else:
            delay_print(f"{player2.name}反击了{player1.name}！")
            player2.attack_enemy(player1)
        if player1.health <= 0:
            delay_print(f"{player2.name}击败了{player1.name}，获得了胜利！")
            player2.exp += 100
            player1.is_dead = True
            break

    if player1.is_dead and player2.is_dead:
        delay_print("双方打平，游戏结束。")
    elif player1.is_dead:
        delay_print(f"{player1.name}被击败，游戏结束。")
    elif player2.is_dead:
        delay_print(f"{player2.name}被击败，游戏结束。")

def select_other_player(player):
    print("请选择其他玩家进行交易或PK：")
    for i, p in enumerate(players):
        if p != player:
            print(f"{i+1}. {p.name}")
    while True:
        try:
            choice = int(input("请输入玩家编号："))
            if 1 <= choice <= len(players):
                return players[choice - 1]
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def play_game():
    player_name = input("请输入你的角色名字：")
    player = Player(player_name)
    
    item_list = [
        Item("铜板", "普通的铜板"),
        Item("木材", "用于建造的木材"),
        Item("食物", "补充生命值的食物"),
        Item("藏宝图", "寻找宝藏的地图")
    ]

    delay_print(f"欢迎来到《三国历险》游戏，{player_name}！")
    delay_print("你将在这片神奇的世界中历险。")

    while True:
        players = [player]  # 将当前玩家添加到玩家列表中，以便选择其他玩家进行交易或PK
        for i in range(2):  # 在示例中只添加两个其他玩家，你可以根据需要增加更多玩家
            players.append(Player(f"玩家{i+1}"))

        show_character_status(player)
        action = choose_action()

        if action == 1:
            show_character_status(player)
        elif action == 2:
            show_inventory(player)
        elif action == 3:
            explore(player)
        elif action == 4:
            complete_task(player)
        elif action == 5:
            other_player = select_other_player(player)
            if other_player:
                trade_items(player, other_player)
        elif action == 6:
            other_player = select_other_player(player)
            if other_player:
                pk(player, other_player)
        elif action == 7:
            delay_print("谢谢你玩《三国历险》游戏，再见！")
            exit()

if __name__ == "__main__":
    play_game()
