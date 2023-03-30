"""
Brian Smyth
ubit: briansmy

Sources: Kleinberg-Tardos textbook section 4.2
"""


class Solution:
    
    def __init__(self, listOfBattles):
        self.battles = listOfBattles
    
    def getSchedule(self):
        battle_dict = {}
        keys = []
        for i in range(0, len(self.battles)):
            # Map Deadlines to tuple(id, duration)
            battle = self.battles[i]
            battle_dict[battle[1]] = (i, battle[0])
            keys.append(battle[1])
        sorted_keys = keys.sort()
        schedule = []
        time = 0
        for deadline in sorted_keys:
            battle_id = battle_dict[deadline][0]
            duration = battle_dict[deadline][1]
            time = time + duration
            if time > deadline:
                schedule = []
                break
            else:
                schedule.append((battle_id, time))
        return schedule
