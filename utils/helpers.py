import re

def validate_email(email:str)->bool:
        """
        Args: email: str \n
        validates email i.e checks weather email ends with "@university.com"
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@university\.com$'
        return re.match(pattern, email) is not None