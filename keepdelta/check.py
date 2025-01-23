from keepdelta.config import keys


class CheckConflict:
    """
    To check conflicting values with internal commands (keys) which may create issues.
    """
    @staticmethod
    def check_str(input: str) -> None:
        """
        Check if str has conflicting values
        """
        if input in keys.values():
            raise ValueError(f'The following value has a conflict with keys: {input}')

    @staticmethod
    def check_dict(input: dict) -> None:
        """
        Check if dict has conflicting values
        """
        CheckConflict.check_list(input.values())

    @staticmethod
    def check_list(input: list) -> None:
        """
        Check if list has conflicting values
        """
        conflicting_values = [value for value in input if value in keys.values()]
        if conflicting_values:
            raise ValueError(f'The following values are conflicting with keys: {conflicting_values}')

    @staticmethod   
    def check_set(input: set) -> None:
        """
        Check if set has conflicting values
        """
        CheckConflict.check_list(list(input))

    @staticmethod
    def check_tuple(input: tuple) -> None:
        """
        Check if tuple has conflicting values
        """
        CheckConflict.check_list(list(input))


if __name__ == '__main__':
    variable = [keys['delete'], 'hello']
    try:
        CheckConflict.check_list(variable)
    except:
        print(f'{variable} has conflicting elements')
