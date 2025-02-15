from fasthtml.common import *
from faker import Faker

fake = Faker()

# Ensure PicoCSS is included
picolink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css")
css = Style(':root { --pico-font-size: 90%; --pico-font-family: Arial; }')

# Create FastHTML app with correct headers
app, rt = fast_app(hdrs=(picolink, css), live=True)

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
        return Ul(
            Li(f"Name: {self.name}", cls="text-lg font-bold text-blue-600"),
            Li(f"Address: {self.address}", cls="text-sm text-gray-600"),
            Li(f"Email: {self.email}", cls="text-sm text-gray-600"),
            Li(f"Phone: {self.phonenumber}", cls="text-sm text-gray-600")
        )

g_rid: RandomIdentity = RandomIdentity()

@rt("/")
def get():
    return (
        Title("Random Identity Generator"),
        Main(
            H1("Random Identity Generator by brend3n", cls="text-2xl font-bold text-center text-gray-900"),
            Button(
                "Randomize",
                hx_post="/randomize",  # Uses the input value
                hx_target="#name_display",
                hx_swap="innerHTML",
                cls="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            ),
            Div(
                P(
                    g_rid.__ft__(), 
                    id="name_displayddd", 
                    cls="mt-4 p-4 border rounded bg-gray-100"
                ),  # Displays the updated name
                id="name_display"
            )
        )
    )

@rt("/randomize")
async def post(req: Request):
    new_id = RandomIdentity() # Reinitialize the object with a new random identity
    return new_id.__ft__()

serve()


