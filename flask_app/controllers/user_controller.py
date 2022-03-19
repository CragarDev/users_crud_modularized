from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User


# * ===========================================
# ? RENDER / Users
# * ===========================================


@app.route('/users')
def users():
    all_users = User.get_all_users()

    print("Where... HOME--READ")
    return render_template("users.html", all_users=all_users)


# * ===========================================
# ? RENDER / Create
# * ===========================================

@app.route('/create')
def create():

    print("Where...CREATE--READ")
    return render_template("create.html")


# t- ===========================================
# ? PROCESS FORM - / Create_new
# t- ===========================================

@app.route('/create/new', methods=["POST"])
def create_new():

    query_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }

    user_id = User.create_new_user(query_data)

    print(f"user id: {user_id}")
    print("What...CREATE-created")
    return redirect(f"/read_one/{user_id}")


# * ===========================================
# ? RENDER / Update
# * ===========================================

@app.route('/update_user/<int:user_id>')
def update_user(user_id):

    query_data = {
        "user_id": user_id
    }

    one_user = User.get_one_user(query_data)

    print(f"user id: {user_id}")
    print("Where...UPDATE--READ")
    return render_template("update.html", one_user=one_user)


# t- ===========================================
# ? PROCESS FORM - / Update
# t- ===========================================

@app.route('/update_user/update/<int:user_id>', methods=["POST"])
def update_user_update(user_id):

    query_data = {
        "id": user_id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }

    User.update_user(query_data)

    print(f"user id: {user_id}")
    print("What...UPDATE-Updated")
    return redirect(f"/read_one/{user_id}")


# * ===========================================
# ? RENDER / confirm Delete
# * ===========================================

@app.route('/confirm_delete/<int:user_id>')
def confirm_delete(user_id):

    query_data = {
        "user_id": user_id
    }

    one_user = User.get_one_user(query_data)
    print(f"user id: {user_id}")
    print("Where...CONFIRM DELETE--READ")
    return render_template("confirm_delete.html", one_user=one_user)


# t- ===========================================
# ? PROCESS / Delete
# t- ===========================================

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    print(f"user id: {user_id}")

    query_data = {
        "id": user_id
    }

    User.delete_user(query_data)

    print("Where...DELETE--PROCESS")
    return redirect("/users")


# * ===========================================
# ? RENDER / read_one
# * ===========================================

@app.route('/read_one/<int:user_id>')
def read_one(user_id):

    query_data = {
        "user_id": user_id
    }

    one_user = User.get_one_user(query_data)
    print(f"user id: {user_id}")
    print("Where...READ_ONE--READ")
    return render_template("read_one.html", one_user=one_user)
