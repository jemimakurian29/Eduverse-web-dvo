from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
import os

#os.chdir("C:\\KJC Work\\dvo eduverse (coursera)")


app = Flask(__name__)
app.secret_key = 'gracepwd'
# Function to authenticate user
def authenticate_user(username, password):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="admin",
            user="admin",
            password="Grace678",
            host="db",
            port="5432"
        )

        # Create a cursor object
        cur = conn.cursor()

        # Prepare the query to fetch user credentials
        query = "SELECT * FROM logcreds WHERE username ='"+username+"'AND password='"+password+"'"

        # Execute the query with username and password as parameters
        cur.execute(query)

        # Fetch the first row (if any)
        user = cur.fetchone()

        print(user)
        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return user data if authentication is successful, None otherwise
        return user

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

# Route for login page
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Authenticate the user (replace this with your authentication logic)
        authenticated_user = authenticate_user(username, password)
        
        if authenticated_user:
            # Assuming authenticate_user returns a tuple with user details
            user_details = {
                'name': authenticated_user[0],
                'email': authenticated_user[1],
                'username': username,
                'enrolled_courses': authenticated_user[2]
            }
            # Store user information in session
            session['user'] = user_details
            session['logged_in'] = True
            # Redirect to home page upon successful login
            return redirect(url_for('home_page'))
        else:
            return "Authentication failed. Invalid username or password."
    else:
        return render_template('login2.html')
    
# Route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_email = request.form['new-email']
        new_username = request.form['new-username']
        new_password = request.form['new-password']
        print("Hello0")
        try:
            # Connect to your PostgreSQL database
            conn = psycopg2.connect(
                dbname="admin",
                user="admin",
                password="Grace678",
                host="db",
                port="5432"
            )

            # Create a cursor object
            cur = conn.cursor()
            print("Hello1")
            # Check if the username or email already exists in the database
            cur.execute("SELECT * FROM logcreds WHERE username = %s OR email = %s", (new_username, new_email))
            existing_user = cur.fetchone()
            print("Hello2")
            if existing_user:
                return "Username or email already exists. Please choose a different one."

            # If username or email doesn't exist, insert the new user into the database
            cur.execute("INSERT INTO logcreds (username, email, password) VALUES (%s, %s, %s)", (new_username, new_email, new_password))
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()

            # Redirect to login page after successful registration
            return redirect(url_for('login'))

        except psycopg2.Error as e:
            print("Error connecting to the database:", e)
            return "An error occurred during registration. Please try again later."

    else:
        return render_template('login2.html')

    
@app.route('/profile')
def profile():
    # Check if the user is logged in
    if 'user' in session and session['logged_in']:
        # Retrieve user information from session
        user = session['user']
        return render_template('profile.html', user=user)
    else:
        return redirect(url_for('login'))

# Home page route
@app.route('/home')
def home_page():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="admin",
            user="admin",
            password="Grace678",
            host="db",
            port="5432"
        )
        
        cursor = conn.cursor()

        cursor.execute("SELECT course_id, title, description FROM course_details")
        courses_data = cursor.fetchall()

        cursor.close()
        conn.close()
        
        # Save courses_data in session
        session['courses_data'] = courses_data
        
        # Pass the fetched data to the template
        return render_template('homepg2.html')
    except Exception as e:
        # Handle exceptions, such as database connection errors
        return f"An error occurred: {e}"
    

@app.route('/courses')
def courses():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="admin",
            user="admin",
            password="Grace678",
            host="db",
            port="5432"
        )
        
        cursor = conn.cursor()

        cursor.execute("SELECT course_id, title, description FROM course_details")
        courses_data = cursor.fetchall()

        cursor.close()
        conn.close()
        
        # Save courses_data in session
        session['courses_data'] = courses_data
        
        # Pass the fetched data to the template
        return render_template('courses.html')
    except Exception as e:
        # Handle exceptions, such as database connection errors
        return f"An error occurred: {e}"


# Route for the course page
@app.route('/c1webdev')
def course_webdev():
    return render_template('c1webdev.html')

@app.route('/c2psychology')
def course_psych():
    return render_template('c2psychology.html')

@app.route('/c3perfin')
def course_perfin():
    return render_template('c3perfin.html')

@app.route('/c4graphicdes')
def course_graphicdes():
    return render_template('c4graphicdes.html')

@app.route('/c5python')
def course_python():
    return render_template('c5python.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)