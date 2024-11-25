import datetime

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = []
        self.last_interaction = None

    def add_interaction(self, interaction):
        self.interactions.append(interaction)
        self.last_interaction = datetime.date.now()
        print(f"Interaction '{interaction}' has been added for {self.name}")

    def calculate_days_since_last_interaction(self):
        if not self.last_interaction:
            return None
        
        todays_date = datetime.date.today()
        days_last_interaction = todays_date - self.last_interaction
        return days_last_interaction.days

class CustomerDataSystem():
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        new_customer = Customer(name, email, phone)
        self.customers.append(new_customer)
        print(f"Customer: {self.name} added!")   

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)
        else:
            print(f"Customer: {self.name} removed!")   

    def update_customer_info(self, customer, phone = None, email = None):
        if phone:
            customer.phone = phone
            print(f"Phone number for {customer.name}, changed to {phone} succesfully!")
        elif email:
            customer.email = email
            print(f"{customer.name}'s email changed to {email} succesfully!")
        
    def add_interaction(self):
        pass

    def get_list(self):
        return self.customers

customer_1 = CustomerDataSystem.add_customer("Boyd", "SheriffBoyd@gmail.com", 0700474811)
customer_2 = CustomerDataSystem.add_customer("Sara", "SaraPsycho@gmail.com", 0700123456)
    


    

    




    