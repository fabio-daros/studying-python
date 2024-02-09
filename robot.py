class Robot:
    def __init__(self, name, battery, skills=[]):
        self.__name = name
        self.__battery = battery
        self.__skills = skills

    @property
    def name(self):
        return self.__name

    @property
    def battery(self):
        return self.__battery

    @property
    def skills(self):
        return self.__skills

    def recharge(self):
        self.__battery = self.__battery = 100

    def say_name(self):
        if self.__battery > 0:
            self.__battery -= 1
            return f'BEEP... BEEP... I AM {self.__name.upper()}'
        return 'Low battery, please recharge and try again...'

    def learn_skills(self, new_skill, cost):
        if self.__battery >= cost:
            self.__battery -= cost
            self.__skills.append(new_skill)
            return f'Yeah! I learn a new skill... {new_skill.upper()}'
        return 'Low battery, please recharge and try again...'
