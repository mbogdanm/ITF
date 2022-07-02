class Employee:
    # Initialize Employee object
    def __init__(self, ID, name, department, job):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__job = job

    # Set each object
    def set_name(self, name):
        self.__name = name

    def set_ID(self, ID):
        self.__ID = ID

    def set_dept(self, department):
        self.__department = department

    def set_job(self, job):
        self.__job = job

    # Get each object
    def get_name(self):
        return self.name

    def get_ID(self):
        return self.__ID

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job


    def print(self):
        print("Name: " + self.__name + \
               ", ID Number: " + self.__ID + \
               ", Department: " + self.__department + \
               ", Job Title: " + self.__job)