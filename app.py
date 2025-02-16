# from fasthtml.common import *
# from monsterui.all import *
# from faker import Faker

# fake = Faker()

# # Ensure MonsterUI theme is set
# hdrs = Theme.slate.headers(highlightjs=True)
# app, rt = fast_app(hdrs=hdrs, live=True)

# class RandomIdentity:
#     def __init__(self):
#         self.name = fake.name()
#         self.address = fake.address()
#         self.email = fake.email()
#         self.phonenumber = fake.phone_number()

#     def regenerate(self):
#         self.__init__()

#     def __repr__(self):
#         return f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\nPhone: {self.phonenumber}"
    
#     def __str__(self):
#         return f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\nPhone: {self.phonenumber}"
    
#     def __ft__(self):
#         return CardContainer(
#             Card(
#                 DivVStacked(
#                     H4(self.name, cls="text-black-700"),  # Dark blue
#                     P(self.address, cls="text-black-600"),  # Dark yellow
#                     P(self.email, cls="text-black-500"),  # Standard green
#                     P(self.phonenumber, cls="text-black-500"),  # Standard red
#                 ),
#                 cls=(CardT.primary, "w-full max-w-lg p-8")
#             ),
#             cls=ContainerT.lg  # Consistent width container
#         )

# g_rid: RandomIdentity = RandomIdentity()

# @rt("/")
# def get():
#     return Container(
#         DivCentered(
#             H1("Random Identity Generator", cls="text-xl font-bold mb-6"),  # Added bottom margin
#             Div(
#                 g_rid.__ft__(),
#                 id="name_display",
#                 cls="bg-gray-100 p-4 rounded-lg shadow mb-6"  # Added bottom margin
#             ),
#             Button(
#                 "Randomize",
#                 hx_post="/randomize",
#                 hx_target="#name_display",
#                 cls="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-6 rounded mt-4"  # Added top margin & padding
#             ),
#             cls="bg-blue-900 text-white p-8 min-h-screen flex items-center justify-center"
#         )
#     )


# @rt("/randomize")
# async def post(req: Request):
#     new_id = RandomIdentity()
#     return new_id.__ft__()

# serve()

from fasthtml.common import *
from monsterui.all import *
from faker import Faker

fake = Faker()

# Ensure MonsterUI theme is set
hdrs = Theme.slate.headers(highlightjs=True)
app, rt = fast_app(hdrs=hdrs, live=True)

class RandomIdentity:
    def __init__(self):
        self.name = fake.name()
        self.address = fake.address()
        self.email = fake.email()
        self.phonenumber = fake.phone_number()

    def regenerate(self):
        self.__init__()

    def __repr__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\nPhone: {self.phonenumber}"
    
    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\nPhone: {self.phonenumber}"
    
    def __ft__(self):
        return CardContainer(
            Card(
                DivVStacked(
                    H4(self.name, cls=TextT.primary),  # Better contrast
                    P(self.address, cls=TextT.muted),  # Muted secondary text
                    P(self.email, cls=TextT.info),  # Slightly highlighted email
                    P(self.phonenumber, cls=TextT.success),  # Green success style for phone
                ),
                cls=(CardT.secondary, "p-10 shadow-lg rounded-xl")
            ),
            cls=ContainerT.lg # Medium container for better layout balance
        )

g_rid: RandomIdentity = RandomIdentity()

@rt("/")
def get():
    return Container(
        DivCentered(
            H1("Random Identity Generator", cls="text-2xl font-extrabold mb-8"),  # Larger, bolder title
            Div(
                g_rid.__ft__(),
                id="name_display",
                cls="bg-gray-100 p-6 rounded-lg shadow-xl mb-8 w-1/2"  # Improved shadow & spacing
            ),
            Button(
                "Generate New Identity",
                hx_post="/randomize",
                hx_target="#name_display",
                cls=(ButtonT.primary, "px-8 py-3 rounded-lg shadow-md transition hover:scale-105")  # Enhanced button effect
            ),
            cls=(BackgroundT.primary, "text-white p-12 min-h-screen flex items-center justify-center")  # Darker primary bg
        )
    )

@rt("/randomize")
async def post(req: Request):
    new_id = RandomIdentity()
    return new_id.__ft__()

serve()

