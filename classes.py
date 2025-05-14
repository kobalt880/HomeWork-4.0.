class Spell:
    def __init__(self, name: str, dificult: int, type: str, discription: str):
        self.set_name(name)
        self.set_dificult(dificult)
        self.set_type(type)
        self.set_discription(discription)
    
    def get_name(self):
        return self.__name
    def get_dificult(self):
        return self.__dificult
    def get_type(self):
        return self.__type
    def get_discription(self):
        return self.__discription
    
    def set_name(self, new: str):
        if isinstance(new, str):
            self.__name = new
        else:
            raise ValueError
    def set_dificult(self, new: int):
        if isinstance(new, int) and new > 0 and new < 11:
            self.__dificult = new
        else:
            raise ValueError
    def set_type(self, new: str):
        if isinstance(new, str):
            self.__type = new
        else:
            raise ValueError
    def set_discription(self, new: str):
        if isinstance(new, str):
            self.__discription = new
        else:
            raise ValueError
    
    def __str__(self):
        return f'Название: {self.__name}, сложность: {self.__dificult}/10, '\
        f'тип: {self.__type}, описание: {self.__discription}'

class Wizard:
    def __init__(self, name: str, house: str, magic_level: int,
                 spells: list[Spell], status: str):
        self.set_name(name)
        self.set_house(house)
        self.set_magic_level(magic_level)
        self.set_spells(spells)
        self.set_status(status)
    
    def get_name(self):
        return self.__name
    def get_house(self):
        return self.__house
    def get_magic_level(self):
        return self.__magic_level
    def get_spells(self):
        return self.__spells
    def get_status(self) -> str:
        return self.__status
    
    def set_name(self, new: str):
        if isinstance(new, str):
            self.__name = new
        else:
            raise ValueError
    def set_house(self, new: str):
        if isinstance(new, str):
            self.__house
        else:
            raise ValueError
    def set_magic_level(self, new: int):
        if isinstance(new, int) and new > 0:
            self.__magic_level
        else:
            raise ValueError
    def set_spells(self, new: list[Spell]):
        if isinstance(new, list) and all([isinstance(e, Spell) for e in new]):
            self.__spells
        else:
            raise ValueError
    def set_status(self, new: str) -> str:
        if isinstance(new, str):
            self.__status = new
        else:
            raise ValueError

    def add_spell(self, spell: Spell):
        if spell not in self.__spells:
            self.__spells.append(spell)

    def remove_spell(self, spell: Spell):
        if spell in self.__spells:
            self.__spells.remove(spell)
    
    def increase_magic_level(self, amount: int):
        if isinstance(amount, int) and amount > 0:
            self.__magic_level += amount

    def __str__(self):
        return f'Имя: {self.__name}, факультет: {self.__house}, уровень магии: {self.__magic_level}, '\
                f'заклинаний выучено: {len(self.__spells)}, статус: {self.__status}.'
    
    def __repr__(self):
        return self.__str__()

class Employee:
    def __init__(self, name: str, position: str, department: str, 
                 salary: int, experience: int, completed_projects: list[str]):
        self.set_name(name)
        self.set_position(position)
        self.set_department(department)
        self.set_salary(salary)
        self.set_experience(experience)
        self.set_completed_projects(completed_projects)
    
    def set_name(self, new: str):
        if isinstance(new, str):
            self.__name = new
        else:
            raise ValueError
    def set_position(self, new: str):
        if isinstance(new, str):
            self.__position = new
        else:
            raise ValueError
    def set_department(self, new: str):
        if isinstance(new, str):
            self.__department = new
        else:
            raise ValueError
    def set_salary(self, new: int):
        if isinstance(new, int) and new > 0:
            self.__salary = new
        else:
            raise ValueError
    def set_experience(self, new: int):
        if isinstance(new, int) and new > 0:
            self.__experience = new
        else:
            raise ValueError
    def set_completed_projects(self, new: list[str]):
        if isinstance(new, list) and all([isinstance(e, str) for e in new]):
            self.__completed_projects = new
        else:
            raise ValueError
    
    def get_name(self):
        return self.__name
    def get_position(self):
        return self.__position
    def get_department(self):
        return self.__department
    def get_salary(self):
        return self.__salary
    def get_experience(self):
        return self.__experience
    def get_completed_projects(self):
        return self.__completed_projects
    
    def increase_salary(self, amount: int):
        if isinstance(amount, int) and amount > 0:
            self.__salary += amount
        else:
            raise ValueError
        
    def add_comp_project(self, project: str):
        if isinstance(project, str) and project not in self.__completed_projects:
            self.__completed_projects.append(project)
    
    def remove_comp_project(self, project: str):
        if isinstance(project, str) and project in self.__completed_projects:
            self.__completed_projects.remove(project)

    def __str__(self):
        return f'Имя: {self.__name}, должность: {self.__position}, отдел: {self.__department}, '\
        f'зарплата: {self.__salary} руб. в мес., стаж: {self.__experience} лет, '\
        f'кол-во завершенных проектов: {len(self.__completed_projects)}'

    def __repr__(self):
        return self.__str__()
    
class Robot:
    def __init__(self, serial_number: int, model: str, current_task: str,
                 charge_level: float, status: str):
        self.set_serial_number(serial_number)
        self.set_model(model)
        self.set_current_task(current_task)
        self.set_charge_level(charge_level)
        self.set_status(status)
    
    def set_serial_number(self, new: int):
        if isinstance(new, int) and new > 0:
            self.__serial_number = new
        else:
            raise ValueError
    def set_model(self, new: str):
        if isinstance(new, str):
            self.__model = new
        else:
            raise ValueError
    def set_current_task(self, new: str):
        if isinstance(new, str):
            self.__current_task = new
        else:
            raise ValueError
    def set_charge_level(self, new: float | int):
        if (isinstance(new, float) or isinstance(new, int)) and new > 0:
            self.__charge_level = new
        else:
            raise ValueError
    def set_status(self, new: str):
        if isinstance(new, str):
            self.__status = new
        else:
            raise ValueError
    
    def get_serial_number(self):
        return self.__serial_number
    def get_model(self):
        return self.__model
    def get_current_task(self):
        return self.__current_task
    def get_charge_level(self):
        return self.__charge_level
    def get_status(self):
        return self.__status
    
    def __str__(self):
        return f'Серийный номер: {self.__serial_number}, модель: {self.__model}, '\
        f'текущая задача: {self.__current_task}, заряд: {self.__charge_level}, '\
        f'статус: {self.__status}'

    def __repr__(self):
        return self.__str__()
    
class Achievement(Spell):
    pass

class Athlete:
    def __init__(self, name: str, age: int, sport_type: str, 
                 achievements: list[Achievement], status: str):
        self.set_name(name)
        self.set_age(age)
        self.set_sport_type(sport_type)
        self.set_achievements(achievements)
        self.set_status(status)

    def set_name(self, new: str):
        if isinstance(new, str):
            self.__name = new
        else:
            raise ValueError
    def set_age(self, new: int):
        if isinstance(new, int) and new > 0:
            self.__age = new
        else:
            raise ValueError
    def set_sport_type(self, new: str):
        if isinstance(new, str):
            self.__sport_type = new
        else:
            raise ValueError
    def set_achievements(self, new: list[Achievement]):
        if isinstance(new, list) and all([isinstance(e, str) for e in new]):
            self.__achievements = new
        else:
            raise ValueError
    def set_status(self, new: str):
        if isinstance(new, str):
            self.__status = new
        else:
            raise ValueError
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_sport_type(self):
        return self.__sport_type
    def get_achievements(self):
        return self.__achievements
    def get_status(self):
        return self.__status
    
    def add_achievement(self, achievement: Achievement):
        if isinstance(achievement, Achievement) and achievement not in self.__achievements:
            self.__achievements.append(achievement)
    
    def remove_achievement(self, achievement: Achievement):
        if isinstance(achievement, Achievement) and achievement in self.__achievements:
            self.__achievements.remove(achievement)
        
    def __str__(self):
        return f'Имя: {self.__name}, возраст: {self.__age}, '\
        f'вид стпорта: {self.__sport_type}, кол-во достижений: {len(self.__achievements)}'\
        f'статус: {self.__status}'

    def __repr__(self):
        return self.__str__()
