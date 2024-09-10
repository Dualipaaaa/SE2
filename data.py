from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data - this would come from your database in a real application
    guide_projects = [
        {'project_name': 'Project A', 'student_id': '123456', 'student_name': 'John Doe'},
        {'project_name': 'Project C', 'student_id': '789012', 'student_name': 'Alice Johnson'}
    ]
    
    examiner_projects = [
        {'project_name': 'Project B', 'student_id': '654321', 'student_name': 'Jane Smith'},
        {'project_name': 'Project D', 'student_id': '345678', 'student_name': 'Bob Brown'}
    ]
    
    return render_template('index.html', guide_projects=guide_projects, examiner_projects=examiner_projects)

@app.route('/view_project/<student_id>')
def view_project(student_id):
    # Logic to fetch and display the project
    return f"Displaying project for student ID: {student_id}"

@app.route('/view_submit_marks/<student_id>', methods=['GET', 'POST'])
def view_submit_marks(student_id):
    if request.method == 'POST':
        # Logic to submit marks
        marks = request.form['marks']
        return f"Marks submitted for student ID: {student_id} - Marks: {marks}"
    return f"Viewing/Editing marks for student ID: {student_id}"

if __name__ == '__main__':
    app.run(debug=True)
