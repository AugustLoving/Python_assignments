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
        self.last_interaction = datetime.datetime.now()
        print(f"Interaction '{interaction}' has been added for {self.name}")

    def calculate_days_since_last_interaction(self):
        if not self.last_interaction:
            return None
        
        todays_date = datetime.datetime.today()
        days_last_interaction = todays_date - self.last_interaction
        return days_last_interaction.days


class ExistingCustomerError(Exception):
    pass


class CustomerDataSystem():
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        if any(customer.email == email for customer in self.customers):
            raise ExistingCustomerError(f"{email} already linked with existing account!")

        new_customer = Customer(name, email, phone)
        self.customers.append(new_customer)
        print(f"Customer: {name} added!")   


    def remove_customer(self, customer_name):
        customer_to_remove = next((c for c in self.customers if c.name == customer_name), None)
        if customer_to_remove:
            self.customers.remove(customer_to_remove)
            print(f"Customer '{customer_name}' removed from the system!")
        else:
            print(f"Customer '{customer_name}' not found!")
            #raise keyerror här? då behövs try där nere. bra eller dåligt?

    def update_customer_info(self, name, phone = None, email = None):
        customer = next((c for c in self.customers if c.name == name), None)
        if customer:
            if phone:
                customer.phone = phone
                print(f"Phone number for {customer.name}, changed to {phone} succesfully!")
            elif email:
                customer.email = email
                print(f"{customer.name}'s email changed to {email} succesfully!")
        else:
            print(f"Customer {name} not found")
        
    def add_interaction(self):
        pass

    def get_list(self):
        for customer in self.customers:
            print(f"name: {customer.name}, email: {customer.email}, phone: {customer.phone}")


#Användning
crm = CustomerDataSystem("Riot Games")

crm.add_customer("Boyd", "SheriffBoyd@gmail.com", 700474811)
crm.add_customer("Sara", "SaraPsycho@gmail.com", 700123456)

crm.get_list()

crm.update_customer_info("Boyd", phone = 793856239)

customer_boyd = next(c for c in crm.customers if c.name == "Boyd")
customer_boyd.add_interaction("Called to discuss a new deal.")

days = customer_boyd.calculate_days_since_last_interaction()
print(f"days since last interc: {days}")

crm.remove_customer("Sara")
crm.get_list()

try:
    crm.add_customer("Boyd", "SheriffBoyd@gmail.com", 700474811)
except ExistingCustomerError as error:
    print(f"Something went wrong: {error}")

 

    




    