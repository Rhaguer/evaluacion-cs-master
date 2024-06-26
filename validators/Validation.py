class Validation:
    def __init__(self, validators):
        self.validators = validators


    def validate(self, prompt, default=None):
        while True:
            value = input(prompt)
            if not value.strip() and default is not None:
                return default

            try:
                for validator in self.validators:
                    value = validator.validate(value)
                return value
            except ValueError as e:
                print(f"Error: {e}")