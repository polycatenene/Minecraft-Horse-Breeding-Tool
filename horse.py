class Horse:
    def __init__(self, hp, jump, speed):
        self.hp = int(hp)
        self.jump = float(jump)
        self.speed = float(speed)
        self.id = None

    def get_attrs(self):
        return (self.hp, self.jump, self.speed)


class Stable:
    def __init__(self):
        self.horses = []
        self.min_hp = 15
        self.max_hp = 30
        self.min_jump = 1.086
        self.max_jump = 5.293
        self.min_speed = 4.8375
        self.max_speed = 14.5125

    def renumber(self):
        for i, h in enumerate(self.horses, 1):
            h.id = i

    def add_horse(self, hp, jump, speed):
        try:
            hp = int(hp)
            jump = float(jump)
            speed = float(speed)
        except:
            return False
        if not (self.min_hp <= hp <= self.max_hp and
                self.min_jump - 0.01 <= jump <= self.max_jump + 0.01 and
                self.min_speed - 0.01 <= speed <= self.max_speed + 0.01):
            return False
        self.horses.append(Horse(hp, jump, speed))
        self.renumber()
        return True

    def modify_horse(self, hid, attr, value):
        for h in self.horses:
            if h.id == hid:
                try:
                    if attr == "hp":
                        v = int(value)
                        if self.min_hp <= v <= self.max_hp:
                            h.hp = v
                            return True
                    elif attr == "jump":
                        v = float(value)
                        if self.min_jump - 0.01 <= v <= self.max_jump + 0.01:
                            h.jump = v
                            return True
                    elif attr == "speed":
                        v = float(value)
                        if self.min_speed - 0.01 <= v <= self.max_speed + 0.01:
                            h.speed = v
                            return True
                except:
                    return False
        return False

    def delete_by_id(self, hid):
        before = len(self.horses)
        self.horses = [h for h in self.horses if h.id != hid]
        self.renumber()
        return len(self.horses) < before

    def dominated(self, h):
        for o in self.horses:
            if o is not h and o.hp > h.hp and o.jump > h.jump and o.speed > h.speed:
                return True
        return False

    def delete_baka(self):
        before = len(self.horses)
        self.horses = [h for h in self.horses if not self.dominated(h)]
        self.renumber()
        return len(self.horses) < before

    def sort_by(self, attr):
        self.horses.sort(key=lambda h: getattr(h, attr), reverse=True)
        self.renumber()

    def sort_by_weight(self, w1, w2, w3):
        self.horses.sort(
            key=lambda h: h.hp * w1 + h.jump * w2 + h.speed * w3,
            reverse=True
        )
        self.renumber()

    def table(self, title="Stable Horses"):
        print(f"\n{title}")
        print("ID\tHP\tJUMP\tSPEED")
        print("-" * 30)
        for h in self.horses:
            print(f"{h.id:2d}\t{h.hp:2d}\t{h.jump:.2f}\t{h.speed:.2f}")
        print(f"Total: {len(self.horses)} horses\n")

    def show_baka(self):
        print("\nBaka Horses (Outperformed by others)")
        print("ID\tHP\tJUMP\tSPEED")
        print("-" * 30)
        output = False
        for h in self.horses:
            if self.dominated(h):
                print(f"{h.id:2d}\t{h.hp:2d}\t{h.jump:.2f}\t{h.speed:.2f}")
                output = True
        if not output:
            print("No baka horse found")
        print()

    def breed_predict(self, hid1, hid2):
        horse1 = None
        horse2 = None
        for h in self.horses:
            if h.id == hid1:
                horse1 = h
            if h.id == hid2:
                horse2 = h
        if not (horse1 and horse2):
            return False, "Horse ID not found\n"
        if horse1.id == horse2.id:
            return False, "Cannot breed the same horse\n"


        hp_min = (horse1.hp + horse2.hp + self.min_hp)/3
        hp_max = (horse1.hp + horse2.hp + self.max_hp)/3
        hp_av = (hp_max - hp_min)/2
        jump_strength_sum = jump_height_to_strength(horse1.jump) + jump_height_to_strength(horse1.jump)
        jump_min = jump_strength_to_height((jump_strength_sum + 0.4)/3)
        jump_max = jump_strength_to_height((jump_strength_sum + 1.0)/3)
        jump_av = jump_strength_to_height((jump_strength_sum + 0.7)/3)
        speed_min = (horse1.speed + horse2.speed + self.min_speed)/3
        speed_max = (horse1.speed + horse2.speed + self.max_speed)/3
        speed_av = (speed_max - speed_min)/2

        print(f"\nBreed Prediction: Horse{horse1.id} × Horse{horse2.id}")
        print("Parent Stats:")
        print(f"  Horse{horse1.id}: HP={horse1.hp}, JUMP={horse1.jump:.3f}, SPEED={horse1.speed:.3f}")
        print(f"  Horse{horse2.id}: HP={horse2.hp}, JUMP={horse2.jump:.3f}, SPEED={horse2.speed:.3f}")
        print("Offspring Possible Range:")
        print(f"  HP:     ({hp_min:.1f} -[{hp_av:.1f}]- {hp_max:.1f})")
        print(f"  JUMP:   ({jump_min:.3f} -[{jump_av:.3f}]- {jump_max:.3f})")
        print(f"  SPEED:  ({speed_min:.3f} -[{speed_av:.3f}]- {speed_max:.3f})\n")
        return True, ""


def help_text():
    print(
        "\n===== MC Horse Breeding Tool Commands =====",
        "add <hp> <jump> <speed>     - Add new horse (HP:15-30, JUMP(height):1.086≤x≤5.293, SPEED:4.8375≤x≤14.5125)",
        "show                        - Show all horses",
        "sort <hp|jump|speed>        - Sort by attribute (descending)",
        "weight <w1> <w2> <w3>       - Sort by weight (HP×w1 + JUMP×w2 + SPEED×w3)",
        "modify <id> <attr> <value>  - Modify horse attribute (attr: hp/jump/speed)",
        "show baka                   - Show horses dominated in all stats by others",
        "kill <id>                   - Delete horse by ID",
        "kill baka                   - Delete all baka horses",
        "breed <id1> <id2>           - Predict offspring stats",
        "save                        - Export add commands for next import",
        "height <jump_strength>      - Convert jump height to strength(0.4~1.0)",
        "strength <jump_height>      - Convert jump strength to height",
        "help                        - Show this help",
        "exit                        - Exit program",
        "==========================================\n",
        sep="\n  "
    )


def jump_strength_to_height(J: float) -> float:
    return (
        -0.1817584952 * J ** 3
        + 3.689713992 * J ** 2
        + 2.128599134 * J
        - 0.343930367
    )


def jump_height_to_strength(H: float) -> float:
    lo, hi = 0.4, 1.0
    for _ in range(16):
        mid = (lo + hi) / 2
        if jump_strength_to_height(mid) < H:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


stable = Stable()
help_text()
while True:
    cmd = input("> ").strip().split()
    if not cmd:
        continue

    match cmd:
        case ["add", hp, jump, speed]:
            if stable.add_horse(hp, jump, speed):
                print("add success\n")
            else:
                print("add failed\n")

        case ["sort", attr] if attr in ("hp", "jump", "speed"):
            stable.sort_by(attr)
            stable.table(title=f"Sorted by {attr} (Descending)")

        case ["show"]:
            stable.table()

        case ["modify", hid, attr, value]:
            try:
                hid = int(hid)
                if stable.modify_horse(hid, attr, value):
                    print("modify success\n")
                else:
                    print("modify failed\n")
            except:
                print("modify failed\n")

        case ["weight", w1, w2, w3]:
            try:
                w1, w2, w3 = float(w1), float(w2), float(w3)
                stable.sort_by_weight(w1, w2, w3)
                stable.table(title=f"Weighted Sort (HP×{w1} + JUMP×{w2} + SPEED×{w3})")
            except:
                print("weight failed\n")

        case ["show", "baka"]:
            stable.show_baka()

        case ["kill", "baka"]:
            if stable.delete_baka():
                print("All baka horses deleted\n")
            else:
                print("No baka horses to delete\n")

        case ["kill", hid]:
            try:
                hid = int(hid)
                if stable.delete_by_id(hid):
                    print(f"Horse {hid} deleted\n")
                else:
                    print(f"Horse {hid} not found\n")
            except:
                print("delete failed")

        case ["breed", hid1, hid2]:
            try:
                hid1, hid2 = int(hid1), int(hid2)
                success, msg = stable.breed_predict(hid1, hid2)
                if not success:
                    print(f"breed predict failed: {msg}\n")
            except:
                print("breed predict failed\n")

        case ["save"]:
            if stable.horses:
                print("\n===== Exported Add Commands =====")
                for horse in stable.horses:
                    print(f"add {horse.hp} {horse.jump:.2f} {horse.speed:.2f}")
                print("=================================\n")
            else:
                print("No horses in stable to export\n")

        case ["help"]:
            help_text()

        case ["exit"]:
            print("Exiting program\n")
            break

        case ["height", J]:
            try:
                J = float(J)
                if 0.4 <= J <= 1.0:
                    H = jump_strength_to_height(J)
                    print(f"Jump height: {H:.3f}\n")
                else:
                    print("Jump strength must be between 0.4 and 1.0\n")
            except:
                print("failed")

        case ["strength", H]:
            try:
                H = float(H)
                if 1.086 <= H <= 5.293:
                    J = jump_height_to_strength(H)
                    print(f"Jump strength: {J:.3f}\n")
                else:
                    print("Jump height must be between 1.086 and 5.293\n")
            except:
                print("failed\n")

        case _:
            print("invalid command\n")
