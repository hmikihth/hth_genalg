#!/usr/bin/env python3

import configparser, os

CONFIG_PATH = "genalg.cfg"

class Container():
    def __init__(self):
        pass

class Settings():
    def __init__(self):
        self.config = configparser.ConfigParser()
        if not os.path.exists(CONFIG_PATH):
            self.createConfig()
        self.readConfig()

    def createConfig(self):
        self.config.add_section("Common")
        self.config.set("Common", "chromosomes_n", "10")
        self.config.set("Common", "termination_function", "myTermination")
        self.config.set("Common", "valueset", "myValueset")

        self.config.add_section("Population0")
        self.config.set("Population0", "population_limit", "30")
        self.config.set("Population0", "sorting_greater", "no")
        self.config.set("Population0", "criterium_function", "myCriterium")
        self.config.set("Population0", "elit_rate", "5")
        self.config.set("Population0", "elit_children", "3")
        self.config.set("Population0", "normal_children", "2")
        self.config.set("Population0", "deterministic", "no")
        self.config.set("Population0", "bests_alive", "no")
        self.config.set("Population0", "bests_alive_limit", "2")
        self.config.set("Population0", "mutant_chromosomes", "1")
        self.config.set("Population0", "inbreeding", "no")
        self.config.set("Population0", "equal_crossover", "yes")
    
        with open(CONFIG_PATH, "w") as configfile:
            self.config.write(configfile)

    def getOwn(self, module_name):
        exec("import "+module_name)
        result = eval(module_name+".get()")
        return result

    def readSection(self, section_name, container):
        if section_name == "Common":
            self.chromosomes_n = self.config.getint(section_name, "chromosomes_n")
            self.termination_function = self.getOwn(self.config.get(section_name, "termination_function"))
            self.valueset = self.getOwn(self.config.get(section_name, "valueset"))
        else:
            for option in self.config.options(section_name):
                try:
                    container.__dict__[option] = self.config.getint(section_name, option)
                except:
                    try:
                        container.__dict__[option] = self.config.getboolean(section_name, option)
                    except:
                        if option != "criterium_function":
                            container.__dict__[option] = self.config.get(section_name, option)
                        else:
                            container.__dict__[option] = self.getOwn(self.config.get(section_name, option))

    def readConfig(self):
        self.config.read(CONFIG_PATH)
        sections = self.config.sections()
        self.populations_n = 0
        self.populations = []
        for section in sections:
            container = None
            if section != "Common":
                container = Container()
            self.readSection(section, container)
            if section != "Common":
                self.populations.append(container)
                self.populations_n += 1
