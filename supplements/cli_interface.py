def select_among_multiple_options(
        question: str,
        options: list,
        return_index=False
):
    if len(options) > 1:
        choices = list(map(str, range((0 if return_index else 1), len(options) + (0 if return_index else 1))))
        choices_print = f"\n\n{question}"
        for idx, option in enumerate(options, start=0 if return_index else 1):
            choices_print += f"\n\t{idx} = {option}"
        choices_print = choices_print.strip() + "\n\n"
        choice = str()
        while choice not in choices:
            choice = input(choices_print).strip()
        return choice if return_index else options[int(choice) - 1]
    elif len(options) == 1:
        return "0" if return_index else options[0]
    else:
        print("no options provided")
        raise RuntimeError


def ask_true_false_question(message):
    answer = ''
    while answer not in {"1", "2"}:
        answer = input(
            f'\n\n{message}\n'
            '\t1 = Yes\n'
            '\t2 = No\n').strip()
    return answer == "1"