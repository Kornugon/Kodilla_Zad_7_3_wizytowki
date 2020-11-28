"""
Zadanie 7.3: wizytówki

Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: 
pierwsza (BaseContact) powinna przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. 
Za pomocą kolejnej klasy (BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.

Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. 
Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.

Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.

Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość. 
Wykorzystaj bibliotekę faker do generowania danych.
"""
from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, tel_priv, email):
       self.first_name = first_name
       self.last_name = last_name
       self.tel_priv = tel_priv
       self.email = email

    def __str__(self):
      return f'{self.first_name} {self.last_name} {self.email}'
    
    #to zostawiam tak dla siebie
    #def __repr__(self):
    #  return f'{self.first_name} {self.last_name} {self.email}'

    def contact(self):
        return f"Wybieram numer {self.tel_priv} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def get_name_len(self):
        return len(self.first_name) + len(self.last_name)
    
    #Blok BusinessContact ma tą funkcję i @property przez dziedziczenie więc nie trzeba tego powielać
    @get_name_len.setter
    def get_name_len(self, name):
        first_name, last_name = name.split(" ")
        self.first_name = first_name
        self.last_name = last_name



class BusinessContact(BaseContact):
    def __init__(self, position, company_name, tel_comp, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company_name = company_name
       self.tel_comp = tel_comp
    
    #z premedytacja nadpisuję metodę bazowej funkcji zmieniając jedynie wyświetlany telefon według instrukcji:
    #"Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”.
    # Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny."
    def contact(self):
        return f"Wybieram numer {self.tel_comp} i dzwonię do {self.first_name} {self.last_name}"



def create_contacts(contact_obj, amount):
    """
    Faker to generate false personal data.
    Instet "Priv" in first position for private data,
    Insert "Company" in first position for corporate data.
    Second position is for amount of data.
    """
    if contact_obj == "Priv":
        for i in range(amount):
            cont = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), tel_priv=fake.phone_number(), email=fake.email())
            print(f"Wizytówka {i+1} prywatna: {cont}")
    elif contact_obj == "Company":
        for i in range(amount):
            cont = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), tel_priv=fake.phone_number(), email=fake.email(), position=fake.job(), company_name=fake.company(), tel_comp=fake.phone_number())
            print(f"Wizytówka {i+1} firmowa: {cont}")



#wywołanie 10 fałszywych kontaktów
create_contacts("Priv", 10)
create_contacts("Company", 10)



# printy sprawdzajace dla Priv
con_1 = BaseContact(
    first_name="Jan", 
    last_name="Kowalski", 
    tel_priv="+48 555 666 999", 
    email="Jan.Kowal@Dgmail.com"
    )

print(con_1.contact())

print(con_1.get_name_len)
con_1.get_name_len="Kuba KKK"
print(con_1.get_name_len)


# printy sprawdzajace dla Company
con_2 = BusinessContact(
    first_name="Jan", 
    last_name="Kowal", 
    tel_priv="+48 555 666 999", 
    email="Jan.Kowal@Dgmail.com", 
    position="Self Employment", 
    company_name="Private Company", 
    tel_comp="+48 111 222 666"
    )

print(con_2.contact())

print(con_2.get_name_len)
con_2.get_name_len="Ludwik XXXVI"
print(con_2.get_name_len)
