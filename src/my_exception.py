class InstantiateCSVError(Exception):
    """My custom exception from general script exception class"""

    def __init__(self, message="Файл item.csv поврежден"):
        super().__init__(message)

