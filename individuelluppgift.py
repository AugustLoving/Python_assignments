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

    def inactiv_customer(self, days_max = 30):
        if self.calculate_days_since_last_interaction() is not None and self.calculate_days_since_last_interaction() > days_max:
            return True
        return False
        

class ExistingCustomerError(Exception):
    pass
class CustomerNotFoundError(Exception):
    pass

class CustomerDataSystem():
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        try:
            if any(customer.email == email for customer in self.customers):
                raise ExistingCustomerError(f"{email} already linked with existing account!")
#raise fångar
            new_customer = Customer(name, email, phone)
            self.customers.append(new_customer)
            print(f"Customer '{name}' added!")
        
        except ExistingCustomerError as e:
            print(f"Error: {e}")
#except kastar            


    def remove_customer(self, customer_name):
        try:
            customer_to_remove = next((c for c in self.customers if c.name == customer_name), None)
            if not customer_to_remove:
                raise CustomerNotFoundError(f"No customer '{customer_name}' found!")
            
            self.customers.remove(customer_to_remove)
            print(f"Customer '{customer_name}' removed!")
        
        except CustomerNotFoundError as e:
            print(f"Error: {e}")

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
        
    def add_interaction(self, customer_name, interaction):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if customer:
            customer.add_interaction(interaction)
            customer.last_interaction = datetime.datetime.now()
        else:
            print(f"Customer '{customer_name}' not found!")

    def get_interaction_list_specifik(self, customer_name):
        try:
            customer = next((c for c in self.customers if c.name == customer_name), None)
            if not customer:
                raise CustomerNotFoundError(f"Customer '{customer_name}' not found")

            print(f"List of interactions for {customer.name}: ")
            for interaction in customer.interactions:
                print(f"- {interaction}")
            
            return customer.interactions

        except CustomerNotFoundError as e:
            print(f"Error: {e}")
            return []


    def calculate_days_since_last_interaction(self, customer_name):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if not customer:
            print(f"Customer: '{customer_name}' not found!")
            return None

        if not customer.last_interaction:
            print(f"Customer '{customer_name}' has no previous interactions")
            return None

        todays_date = datetime.datetime.today()
        days_since = (todays_date - customer.last_interaction).days
        print(f"Days since last interaction with {customer_name}: {days_since}")
        return days_since
            

    def get_list(self):
        for customer in self.customers:
            print(f"name: {customer.name}, email: {customer.email}, phone: {customer.phone}")


    def print_inactiv_customers(self, days_max = 30):
        print(f"Customers inactiv for more than {days_max} days: ")
        for customer in self.customers:
            if customer.inactiv_customer(days_max):
                days_since_last_interaction = customer.calculate_days_since_last_interaction()
                print(f"Customer name: {customer.name}, last interaction: {days_since_last_interaction} days ago")

#Användning
crm = CustomerDataSystem("Riot Games")

crm.add_customer("Boyd", "SheriffBoyd@gmail.com", 700474811)
crm.add_customer("Sara", "SaraPsycho@gmail.com", 700123456)


crm.get_list()

crm.update_customer_info("Boyd", phone = 793856239)


crm.add_interaction("Boyd", "Booked a meeting.")
crm.calculate_days_since_last_interaction("Boyd")


crm.remove_customer("Sara")
crm.get_list()

crm.add_customer("Boyd", "SheriffBoyd@gmail.com", 700474811)


crm.get_interaction_list_specifik("Boyd")
crm.add_customer("Jade", "Jade@gmail.com", 7023470287)
crm.get_list()

crm.update_customer_info("Jade", email= "Jadde@ajd.com")
