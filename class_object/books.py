class Book:
    
    def __init__(self,title,auther,ref):
        self.title=title
        self.Auther=auther
        self.ref=ref
        self.is_check_out=False
    
    def check_in(self):
        if not self.is_check_out :
            self.is_check_out=True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."
    
    def check_out(self):
        if self.is_check_out :
            self.is_check_out=False
            return f"{self.title} is checked out."
        else:
            return f"{self.title} is not checked out."
    
   # print("Check whether this module running automatically in imported module or not")
   # check_in()
    
    