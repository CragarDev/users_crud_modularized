from flask_app import app
from flask_app.controllers import user_controller


#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
