class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        # MRO - Method resolution order
        super().greet()

c = C()
c.greet()  # Hello from A

# Якщо потрібно, щоб B.greet() 
# також викликалося, можна зробити наступне:
class C(A, B):
    def greet(self):
        B.greet(self)  # Виклик методу B
        super().greet()  # Виклик методу A
