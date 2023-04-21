class ParenthesisNumber:
    def __init__(self, open_par: int, close_par: int):
        self.open_par = open_par
        self.close_par = close_par
        self.open_index = 0
        self.close_index = 0
        self.open_anchor = 0
        self.close_anchor = 0


def input_number() -> str:
    while True:
        user_input = input("Enter a list of numbers: ")
        for x in user_input:
            if x not in "0123456789-(), ":
                print("Invalid input")
        return user_input


def str_int(input_str: str, input_list: list):
    if input_str != "":
        for x in input_str.split(", "):
            if x != "(" or x != ")" or x != ",":
                input_list.append(int(x))


def num_to_data_list(input_set: str, number_list: list = None,
                     par_num: ParenthesisNumber = ParenthesisNumber(0, 0)) -> list:
    """Takes in a string of numbers and symbols and returns a list of numbers properly formatted."""
    if number_list is None:
        number_list = []

    for index, x in enumerate(input_set):
        if x == "(":
            par_num.open_par += 1
            par_num.open_index = index
        elif x == ")":
            par_num.close_par += 1
            par_num.close_index = index

        if (par_num.open_par - par_num.close_par) == 1 and par_num.open_par >= 1:
            if x == ")":
                number_list.append(input_set[par_num.open_anchor:par_num.close_index + 1])
                par_num.close_anchor = index

        elif (par_num.open_par - par_num.close_par) == 2 and x == "(":
            par_num.open_anchor = index

        elif par_num.open_par == par_num.close_par:
            if par_num.open_par == 1:
                str_int(input_set[par_num.open_index + 1:par_num.close_index], number_list)
            elif input_set[par_num.close_anchor + 3:index] != "":
                str_int(input_set[par_num.close_anchor + 3:index], number_list)

        if index + 3 <= len(input_set) and (par_num.open_par - par_num.close_par) <= 1:
            if x + input_set[index + 1] + input_set[index + 2] == ", (":
                if par_num.close_anchor == 0:
                    str_int(input_set[par_num.open_index + 1:index], number_list)
                elif par_num.close_anchor != 0:
                    str_int(input_set[par_num.close_anchor + 3:index], number_list)

    for index_2, w in enumerate(number_list):
        if type(w) == str:
            number_list[index_2] = []
            num_to_data_list(w, number_list[index_2], ParenthesisNumber(0, 0))
    return number_list


if __name__ == '__main__':
    print(num_to_data_list("(1, (2, 3, (4, 5, 6), 7), 8, (9, 10, 11), 12)"))
    number = input_number()
    print(number)
    print(num_to_data_list(number))
