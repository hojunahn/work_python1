import random

class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy):
        damage_dealt = random.randint(0, self.damage)
        enemy.hp -= damage_dealt
        print(f"{self.name}가 {enemy.name}를 공격하여 {damage_dealt}의 피해를 입혔습니다.")

    def use_potion(self):
        potion_amount = random.randint(10, 30)
        self.hp = min(self.max_hp, self.hp + potion_amount)
        print(f"{self.name}이(가) 물약을 사용하여 {potion_amount}의 체력을 회복했습니다.")

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def attack(self, player):
        damage_dealt = random.randint(0, self.damage)
        player.hp -= damage_dealt
        print(f"{self.name}가 {player.name}를 공격하여 {damage_dealt}의 피해를 입혔습니다.")

class Potion:
    def __init__(self, name, healing_amount):
        self.name = name
        self.healing_amount = healing_amount

    def use(self, player):
        player.hp += self.healing_amount
        print(f"{player.name}이(가) {self.name}을(를) 사용하여 {self.healing_amount}의 체력을 회복했습니다.")

def main():
    player = Player("플레이어", 100, 20)
    enemy = Enemy("적", 100, 10)
    potion = Potion("물약", 20)

    print("전투를 시작합니다!")

    while player.is_alive() and enemy.is_alive():
        action = input("공격하려면 'a', 물약을 사용하려면 'p'를 입력하세요: ")
        if action == 'a':
            player.attack(enemy)
            enemy.attack(player)
        elif action == 'p':
            potion.use(player)
            enemy.attack(player)

        print(f"{player.name}의 체력: {player.hp}")
        print(f"{enemy.name}의 체력: {enemy.hp}")
        print()

    if player.is_alive():
        print("적을 처치했습니다! 게임 클리어!")
    else:
        print("플레이어가 전투에서 패배했습니다.")

if __name__ == "__main__":
    main()