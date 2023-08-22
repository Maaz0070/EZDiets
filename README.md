# EZDiets

The **Dietary Choice Django Website** is a web application that allows users to search for and view menu items, groceries, restaurants, and recipes based on dietary restrictions or allergies. This application is built using the Django framework and integrates with the Spoonacular Recipe Food Nutrition API to retrieve relevant data.

## Features

- **Search and Filter:** Users can perform searches for menu items, groceries, restaurants, and recipes using specific keywords.
- **Dietary Restrictions:** The application supports filtering by dietary restrictions or allergies to ensure that users can find suitable options.
- **Results Page:** The results page displays the retrieved information, including detailed information about menu items, groceries, restaurants, and recipes.
- **User Registration:** Users can register for accounts to personalize their experience.
- **User Authentication:** Registered users can log in to access additional features and save preferences.

## Views (`views.py`)

The views defined in the `views.py` file of the Django application include:

- `index(request)`: Renders the initial search page.
- `results(request)`: Processes user searches, calls the Spoonacular API, and displays the search results.
- `register(request)`: Handles user registration, creating new user accounts.
- `login(request)`: Handles user login using authentication.

## Getting Started

To set up and run the Dietary Choice Django Website locally, follow these steps:

1. Clone the repository to your local machine:

   ```sh
   git clone <repository_url>

2. Install the necessary dependencies using pip:
```
pip install -r requirements.txt
```
3. Configure API Access: Obtain an API key from Spoonacular Recipe Food Nutrition API. Update the x-rapidapi-key and x-rapidapi-host headers in the views.py file with your API key.
4. Run the Django development server:
   ```
   python manage.py runserver
   ```
5. Access the application in your web browser at http://127.0.0.1:8000/.

   
