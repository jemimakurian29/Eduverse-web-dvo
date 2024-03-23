from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Function to authenticate user
def authenticate_user(username, password):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="admin",
            user="admin",
            password="Grace678",
            host="localhost",
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
        
        user = authenticate_user(username, password)
        if user:
            # Redirect to home page upon successful login
            return redirect(url_for('home_page'))
        else:
            return "Authentication failed. Invalid username or password."
    else:
        return render_template('login2.html')

# Home page route
@app.route('/home')
def home_page():
    return render_template('homepg2.html')

# Courses page route
@app.route('/courses')
def courses():
    return render_template('courses.html')

if __name__ == '__main__':
    app.run(debug=True)
