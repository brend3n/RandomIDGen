# Random Identity Generator

This project is a Python application that generates random identities. It can be used for testing purposes, creating dummy data, or any other scenario where random identity generation is needed.

# Link to live site:

<a href="https://random-id-gen.vercel.app/" target="_blank">Link to site</a>

# TODO:
1) Add options to enter City, State, Zip code etc
2) Integrate email bot

## Features

- Generates random names
- Generates random addresses
- Generates random phone numbers
- Generates random email addresses

## Requirements

- Python 3.x
- `faker` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/brend3n/random_identity_generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd random_identity_generator
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the `app.py` script to generate a random identity:
```bash
python app.py
```

# Vercel

Push vercel using 
```bash
    vercel --prod
```
from the root of the directory

Test vercel locally 
```bash
    vercel dev
```
from the root of the directory

# Vercel Notes
For some reason, pushing to the branch breaks the deployment. So, just push above or test locally.

## Example Output

```
Name: John Doe
Address: 1234 Elm Street, Springfield, IL 62704
Phone: (555) 123-4567
Email: johndoe@example.com
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any questions or inquiries, please contact [yourname@example.com](mailto:yourname@example.com).