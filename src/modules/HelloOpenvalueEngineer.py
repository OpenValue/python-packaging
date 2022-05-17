class HelloOpenvalueEngineerClass:

    def __init__(self, i_name: str, i_age: int, i_seniority: str) -> None:
        self.name: str = i_name
        self.age: str = i_age
        self.seniority: str = i_seniority

    def hello(self):
        print(
            "Hello {} ! You are {} years old, and you already are a {} engineer !".format(
                self.name,
                self.age,
                self.seniority
            )
        )
