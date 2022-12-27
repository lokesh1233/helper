from src import create_app

# creating the app from __init__.py
app = create_app()

# starrting the application
if __name__ == '__main__':
    app.run(debug=True)