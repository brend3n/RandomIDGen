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
    
#     def __ft__(self):
#         return CardContainer(
#             Card(
#                 DivVStacked(
#                     H4(self.name, cls=TextT.primary),  # Better contrast
#                     P(self.address, cls=TextT.muted),  # Muted secondary text
#                     P(self.email, cls=TextT.info),  # Slightly highlighted email
#                     P(self.phonenumber, cls=TextT.success),  # Green success style for phone
#                 ),
#                 cls=(CardT.secondary, "p-10 shadow-lg rounded-xl")
#             ),
#             cls=ContainerT.lg # Medium container for better layout balance
#         )

# g_rid: RandomIdentity = RandomIdentity()

# @rt("/")
# def get():
#     return (
#             Title("Random Identity Generator"),
#             Container(
#                 DivLAligned(
#                     H1("Built with FastHTML", cls="text-2xl font-bold mb-4 bg-gradient-to-r from-red-500 via-yellow-500 via-green-500 via-blue-500 to-purple-500 inline-block text-transparent bg-clip-text"),  # Larger title
#                 ),
#                 DivCentered(
#                     A(
#                         UkIcon("github", height=24, width=24),
#                         href="https://github.com/brend3n/RandomIDGen",
#                         target="_blank",
#                         cls="absolute top-4 right-4 hover:scale-110 transition"
#                     ),
#                     H1("Random Identity Generator", cls="text-4xl font-extrabold mb-8"),  # Larger, bolder title
#                     Div(
#                         g_rid.__ft__(),
#                         id="name_display",
#                         cls="bg-gray-100 p-6 rounded-lg shadow-xl mb-8 w-1/2"  # Improved shadow & spacing
#                     ),
#                     Button(
#                         "Generate New Identity",
#                         hx_post="/randomize",
#                         hx_target="#name_display",
#                         cls=(ButtonT.primary, "px-8 py-3 rounded-lg shadow-md transition hover:scale-105")  # Enhanced button effect
#                     ),
#                     cls=(BackgroundT.primary, "text-white p-12 min-h-screen flex items-center justify-center")  # Darker primary bg
#                 )
#             )
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
    
    def __ft__(self):
        return CardContainer(
            Card(
                DivVStacked(
                    H4(self.name, cls=TextT.primary),
                    P(self.address, cls=TextT.muted),
                    P(self.email, cls=TextT.info),
                    P(self.phonenumber, cls=TextT.success),
                ),
                cls=(CardT.secondary, "p-6 shadow-lg rounded-xl")
            ),
            cls=(ContainerT.expand, "p-6")
        )

g_rid: RandomIdentity = RandomIdentity()

@rt("/")
def get():
    return (
        Title("Random Identity Generator"),
        Container(
            DivLAligned(
                H1("Built with FastHTML", 
                    cls="text-2xl md:text-xl sm:text-lg font-bold mb-4 bg-gradient-to-r from-red-500 via-yellow-500 via-green-500 via-blue-500 to-purple-500 inline-block text-transparent bg-clip-text"
                ),
            ),
            DivCentered(
                A(
                    UkIcon("github", height=24, width=24),
                    href="https://github.com/brend3n/RandomIDGen",
                    target="_blank",
                    cls="absolute top-4 right-4 hover:scale-110 transition"
                ),
                H1("Random Identity Generator", cls="text-4xl font-extrabold mb-8"),
                Div(
                    g_rid.__ft__(),
                    id="name_display",
                    cls="bg-gray-100 p-6 rounded-lg shadow-xl mb-8 flex flex-wrap justify-center"
                ),
                Button(
                    "Generate New Identity",
                    hx_post="/randomize",
                    hx_target="#name_display",
                    cls=(ButtonT.primary, "px-6 sm:px-4 py-3 rounded-lg shadow-md transition hover:scale-105")
                ),
                cls=(BackgroundT.primary, FlexT.column, FlexT.center, "text-white p-6 min-h-screen")
            )
        )
    )

@rt("/randomize")
async def post(req: Request):
    new_id = RandomIdentity()
    return new_id.__ft__()

serve()

