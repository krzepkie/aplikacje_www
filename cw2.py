#zad1

def my_function(a_list, b_list):
    return_list = []
    for x in range(0, len(a_list)):
        if x % 2:
            return_list.append(a_list[x])
    for x in range(0, len(b_list)):
        if not x % 2:
            return_list.append(b_list[x])
    return return_list


a_list = [x for x in range(1, 16)]
b_list = [x for x in range(23, 39)]
print(my_function(a_list, b_list))

#zad2


def my_function(data_text):
    return {'length': len(data_text),
            'letters': list(set(list(data_text))),
            'big_letters': data_text.upper(),
            'small_letters': data_text.lower(),
            }


data_text = "Koteł"
print(my_function(data_text))



#zad3

def my_function(text, letter):
    return text.lower().replace(letter.lower(), "")


text = "Ala ma kota"
letter = "K"
print(my_function(text, letter))


#zad4


def my_function(temperature, temperature_type):
    temp = 0
    if temperature < -273:
        return Exception("Temperature does not exist")
    elif temperature_type not in ["kelvin", "fahrenheit", "rankine"]:
        return Exception("You need to choose one of (kelvin, fahrenheit, rankine)")
    if temperature_type.lower() == "fahrenheit":
        temp = (temperature * 1.8) + 32
    elif temperature_type.lower() == "kelvin":
        temp = temperature + 273.15
    elif temperature_type.lower() == "rankine":
        temp = (temperature + 273.15) * 1.8
    return temp


print(my_function(15, "fahrenheit"))
print(my_function(15, "kelvin"))
print(my_function(15, "rankine"))
print(my_function(15, "oooo"))
print(my_function(-500, "kelvin"))



#zad5


class Calculator:
    def add(self, x, y):
        return x + y

    def difference(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y



#zad6





class ScienceCalculator(Calculator):
    def power(self, x, y):
        return pow(x, y)


c = ScienceCalculator()
print(c.power(5, 10))




#zad7



def my_function(text):
    return text[::-1]


text = "koteł"
print(my_function(text))
