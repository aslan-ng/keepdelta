from keepdelta.config import keys


class CheckConflict:
    """
    To check conflicting keys with internal commands which may create issues.
    """

    message = 'The following key is conflicting with internal command: '

    @staticmethod
    def check_str(input: str) -> None:
        """
        Check if str has conflicting keys
        """
        if input in keys.values():
            raise ValueError(CheckConflict.message + str(input))

    @staticmethod
    def check_dict(input: dict) -> None:
        """
        Check if dict has conflicting keys
        """
        CheckConflict.check_list(input.values())

    @staticmethod
    def check_list(input: list) -> None:
        """
        Check if list has conflicting keys
        """
        conflicting_values = [value for value in input if value in keys.values()]
        if conflicting_values:
            raise ValueError(CheckConflict.message + str(conflicting_values))

    @staticmethod   
    def check_set(input: set) -> None:
        """
        Check if set has conflicting keys
        """
        CheckConflict.check_list(list(input))

    @staticmethod
    def check_tuple(input: tuple) -> None:
        """
        Check if tuple has conflicting keys
        """
        CheckConflict.check_list(list(input))


if __name__ == '__main__':
    variable = [keys['delete'], 'hello']
    CheckConflict.check_list(variable)  # This will raise an error
