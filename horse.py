class Horse:
    def __init__(self, hp_, jump_, speed_):
        self.hp = int(hp_)
        self.jump = float(jump_)
        self.speed = float(speed_)
        self.id = None


class Stable:
    def __init__(self):
        self.horses = []
        self.min_hp = 15
        self.max_hp = 30
        self.min_jump = 1.086
        self.max_jump = 5.293
        self.min_speed = 4.8375
        self.max_speed = 14.5125
        self.factor = (1.0, 1.0, 1.0)
        self.target = False
        self.jump_strength_sum = 1.4

    def renumber(self):
        for i, h in enumerate(self.horses, 1):
            h.id = i

    def check(self, hp_, jump_, speed_):
        if not (self.min_hp <= hp_ <= self.max_hp and
                self.min_jump - 0.01 <= jump_ <= self.max_jump + 0.01 and
                self.min_speed - 0.01 <= speed_ <= self.max_speed + 0.01):
            return False
        return True

    def add_horse(self, hp_, jump_, speed_):
        try:
            hp_ = int(hp_)
            jump_ = float(jump_)
            speed_ = float(speed_)
        except Exception as e_:
            return False, f"Error: {e_}"
        if not self.check(hp_, jump_, speed_):
            return False, "Error: Invalid horse attributes"
        self.horses.append(Horse(hp_, jump_, speed_))
        self.renumber()
        return True, ""

    def modify_horse(self, hid_, attr_, value_):
        for h in self.horses:
            if h.id == hid_:
                try:
                    if attr_ == "hp":
                        v = int(value_)
                        if self.check(v, h.jump, h.speed):
                            h.hp = v
                            return True, ""
                    elif attr_ == "jump":
                        v = float(value_)
                        if self.check(h.hp, v, h.speed):
                            h.jump = v
                            return True, ""
                    elif attr_ == "speed":
                        v = float(value_)
                        if self.check(h.hp, h.jump, v):
                            h.speed = v
                            return True, ""
                except Exception as e_:
                    return False, f"Error: {e_}"
        return False, "Error: Invalid horse id"

    def delete_by_id(self, hid_):
        before = len(self.horses)
        self.horses = [h for h in self.horses if h.id != hid_]
        self.renumber()
        return len(self.horses) < before

    def dominated(self, h):
        for o in self.horses:
            if o is h: continue
            if ( o.hp >= h.hp and o.jump >= h.jump and o.speed >= h.speed) and not ( o.hp == h.hp and o.jump == h.jump and o.speed == h.speed):
                return True
        return False

    def delete_baka(self):
        before = len(self.horses)
        self.horses = [h for h in self.horses if not self.dominated(h)]
        self.renumber()
        return len(self.horses) < before

    def sort_by(self, attr_):
        old_ids = {h: h.id for h in self.horses}
        self.horses.sort(key=lambda h: getattr(h, attr_), reverse=True)
        self.renumber()
        self.table_with_change(old_ids, title=f"Sorted by {attr_} (Descending)")

    def sort_by_weight(self, w1_, w2_, w3_):
        old_ids = {h: h.id for h in self.horses}
        self.horses.sort(key=lambda h: h.hp * w1_ + h.jump * w2_ + h.speed * w3_, reverse=True)
        self.renumber()
        self.table_with_change(old_ids, title=f"Weighted Sort (HP×{w1_} + JUMP×{w2_} + SPEED×{w3_})")


    def table(self, title="Stable Horses"):
        print(f"\n{title}")
        print("ID\tHP\tJUMP\tSPEED")
        print("-" * 30)
        for h in self.horses:
            print(f"{h.id:2d}\t{h.hp:2d}\t{h.jump:.2f}\t{h.speed:.2f}")
        print(f"Total: {len(self.horses)} horses\n")
    def table_with_change(self, old_ids, title="Stable Horses"):
        print(f"\n{title}")
        print(f"{'ID':>2}  {'Δ':^4}   {'HP':>2}  {'JUMP':>6}  {'SPEED':>6}")
        print("-" * 36)

        for h in self.horses:
            old = old_ids.get(h, h.id)
            delta = old - h.id
            if delta > 0: dstr = f"+{delta} ↑"
            elif delta < 0: dstr = f"{delta} ↓"
            else: dstr = " 0   "
            print(f"{h.id:2d}  {dstr:^5}  {h.hp:2d}  {h.jump:6.2f}  {h.speed:6.2f}")
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

    def breed_predict(self, hid1_, hid2_):
        horse1 = None
        horse2 = None
        for h in self.horses:
            if h.id == hid1_:
                horse1 = h
            if h.id == hid2_:
                horse2 = h
        if not (horse1 and horse2):
            return False, "Horse ID not found\n"
        if horse1.id == horse2.id:
            return False, "Cannot breed the same horse\n"
        hp_min = (horse1.hp + horse2.hp + self.min_hp)/3
        hp_max = (horse1.hp + horse2.hp + self.max_hp)/3
        hp_av = (hp_max + hp_min)/2
        self.jump_strength_sum = jump_height_to_strength(horse1.jump) + jump_height_to_strength(horse2.jump)
        jump_min = jump_strength_to_height((self.jump_strength_sum + 0.4)/3)
        jump_max = jump_strength_to_height((self.jump_strength_sum + 1.0)/3)
        jump_av = jump_strength_to_height((self.jump_strength_sum + 0.7)/3)
        speed_min = (horse1.speed + horse2.speed + self.min_speed)/3
        speed_max = (horse1.speed + horse2.speed + self.max_speed)/3
        speed_av = (speed_max + speed_min)/2
        print(f"\nBreed Prediction: Horse{horse1.id} × Horse{horse2.id}")
        print("Parent Stats:")
        print(f"  Horse{horse1.id}: HP={horse1.hp}, JUMP={horse1.jump:.3f}, SPEED={horse1.speed:.3f}")
        print(f"  Horse{horse2.id}: HP={horse2.hp}, JUMP={horse2.jump:.3f}, SPEED={horse2.speed:.3f}")
        print("Offspring Possible Range:")
        print(f"  HP:     ({hp_min:.1f} -[{hp_av:.1f}]- {hp_max:.1f})")
        print(f"  JUMP:   ({jump_min:.3f} -[{jump_av:.3f}]- {jump_max:.3f})")
        print(f"  SPEED:  ({speed_min:.3f} -[{speed_av:.3f}]- {speed_max:.3f})\n")
        return (horse1, horse2), ""

    def probability(self, horse1, horse2):
        odds_hp = int(self.max_hp - (3 * self.target.hp - horse1.hp - horse2.hp) + 1)/(self.max_hp - self.min_hp + 1)
        odds_jump = (1.0 - (3 * jump_height_to_strength(self.target.jump) - self.jump_strength_sum))/0.6
        odds_speed = (self.max_speed - (3 * self.target.speed - horse1.speed - horse2.speed))/(self.max_speed - self.min_speed)
        print(" Probability calculation:",
              f"target HP{self.target.hp}: {odds_hp * 100:.3g}%" if odds_hp > 0.0
              else f"impossible to achieve target HP{self.target.hp}",
              f"target JUMP{self.target.jump:.3f}: {odds_jump * 100:.3g}%" if odds_jump > 0.0
              else f"impossible to achieve target JUMP{self.target.jump:.3f}",
              f"target SPEED{self.target.speed:.3f}: {odds_speed * 100:.3g}%" if odds_speed > 0.0
              else f"impossible to achieve target SPEED{self.target.speed:.3f}",
              f"Fully achieved: {odds_hp * odds_jump * odds_speed * 100:.3g}%\n"
              if all([odds_hp > 0.0, odds_jump > 0.0, odds_speed > 0.0]) else "impossible to achieve fully\n", sep='\n  ')


def help_text():
    print(
        "\n===== MC Horse Breeding Tool Commands =====",
        "add <hp> <jump> <speed>     - Add new horse (HP:15-30, JUMP(height):1.086≤x≤5.293, SPEED:4.8375≤x≤14.5125)",
        "show                        - Show all horses",
        "sort <hp|jump|speed>        - Sort by attribute (descending)",
        "weight <w1> <w2> <w3>       - Sort by weight (HP×w1 + JUMP×w2 + SPEED×w3)",
        "weight,                     - Sort by weight (factor)",
        "factor <w1> <w2> <w3>       - Set weight factors for weighted sort (Default (1, 1, 1))",
        "modify <id> <attr> <value>  - Modify horse attribute (attr: hp/jump/speed)",
        "show baka                   - Show horses dominated in all stats by others",
        "kill <id>                   - Delete horse by ID",
        "kill baka                   - Delete all baka horses",
        "target <hp> <jump> <speed>  - Set target horse parameters to calculate probability in breeding prediction",
        "breed <id1> <id2>           - Predict offspring stats",
        "save                        - Export add commands for next import",
        "height <jump_strength>      - Convert jump height to strength(0.4~1.0)",
        "strength <jump_height>      - Convert jump strength to height",
        "help                        - Show this help",
        "exit                        - Exit program",
        "==========================================\n", sep="\n  ")


def jump_strength_to_height(j: float) -> float:
    return -0.1817584952 * j ** 3 + 3.689713992 * j ** 2 + 2.128599134 * j - 0.343930367


def jump_height_to_strength(h: float) -> float:
    lo, hi = 0.4, 1.0
    for _ in range(16):
        mid = (lo + hi) / 2
        if jump_strength_to_height(mid) < h: lo = mid
        else: hi = mid
    return (lo + hi) / 2


stable = Stable()
help_text()
while True:
    cmd = input("> ").strip().split()
    if not cmd: continue

    match cmd:
        case ["add", hp, jump, speed]:
            success, msg = stable.add_horse(hp, jump, speed)
            if success: print("add success\n")
            else: print(f"add failed: {msg}\n")

        case ["sort", attr] if attr in ("hp", "jump", "speed"):
            stable.sort_by(attr)

        case ["show"]:
            stable.table()

        case ["modify", hid, attr, value]:
            try:
                hid = int(hid)
                success, msg = stable.modify_horse(hid, attr, value)
                if success: print("modify success\n")
                else: print(f"modify failed: {msg}\n")
            except Exception as e:
                print(f"modify failed: {e}\n")

        case ["weight", w1, w2, w3]:
            try:
                w1, w2, w3 = float(w1), float(w2), float(w3)
                stable.sort_by_weight(w1, w2, w3)
            except Exception as e:
                print(f"weight failed: {e}\n")

        case ["factor", w1, w2, w3]:
            try:
                w1, w2, w3 = float(w1), float(w2), float(w3)
                stable.factor = (w1, w2, w3)
            except Exception as e:
                print(f"factor failed: {e}\n")

        case ["weight"]:
            stable.sort_by_weight(*stable.factor)

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
                if stable.delete_by_id(hid): print(f"Horse {hid} deleted\n")
                else: print(f"Horse {hid} not found\n")
            except Exception as e:
                print(f"delete failed: {e}\n")

        case ["target", hp, jump, speed]:
            try:
                hp, jump, speed = int(hp), float(jump), float(speed)
                if stable.check(hp, jump, speed):
                    stable.target = Horse(hp, jump, speed)
                    print("Successfully set target\n")
                else:
                    print("Target parameters must be within valid ranges\n")
            except Exception as e:
                print(f"target failed: {e}\n")

        case ["breed", hid1, hid2]:
            try:
                hid1, hid2 = int(hid1), int(hid2)
                success, msg = stable.breed_predict(hid1, hid2)
                if not success:
                    print(f"breed predict failed: {msg}\n")
                elif stable.target:
                    stable.probability(*success)
                else:
                    print("Target not set so that probability cannot be calculated, use 'target' command to set it\n")
            except Exception as e:
                print(f"breed predict failed: {e}\n")

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
            except Exception as e:
                print(f"height failed: {e}\n")

        case ["strength", H]:
            try:
                H = float(H)
                if 1.086 <= H <= 5.293:
                    J = jump_height_to_strength(H)
                    print(f"Jump strength: {J:.3f}\n")
                else:
                    print("Jump height must be between 1.086 and 5.293\n")
            except Exception as e:
                print(f"strength failed: {e}\n")

        case _:
            print("invalid command\n")
