from website import create_app
#pulling from the folder website from the file init.py and we can import the name create app and it will run
if __name__== "__main__":
    app = create_app()
    app.run(debug=True)
#Makes sure that the app.py file runs rather that it been imported
#debug true means the flask server will automaticly re run when a change is made in the code rather than doing it myself every time