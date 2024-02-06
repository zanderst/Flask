from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your_very_secret_key'


@app.route('/')
def home():
   return render_template('home.html')


@app.route('/requirements')
def requirements():
   return render_template('requirements.html')


@app.route('/grades', methods=['GET', 'POST'])
def grades():
   validsubjects = {'biology', 'geography', 'computer science', 'maths', 'mathematics', 'physical education', 'history',
                    'advanced maths', 'advanced mathematics', 'chemistry', 'physics', 'psychology', 'it', 'english',
                    'english literature', 'economics'}
   if request.method == 'POST':
      sg_pairs = {}
      high_grades_count = 0
      valid = True

      subjects = request.form.getlist('subjects[]')
      grades = request.form.getlist('grades[]')

      for subject, grade in zip(subjects, grades):
         subject_lower = subject.lower()
         if subject_lower not in validsubjects:
            valid = False
            flash(f'{subject} not in list of valid subjects, try again', category='error')
            return render_template('Student_grades.html')

         print(sg_pairs)

         if subject_lower not in sg_pairs:
            sg_pairs[subject_lower] = grade.lower()
         else:
            valid = False
            flash(f'{subject} has been entered multiple times, please try again', category='error')
            return render_template('Student_grades.html')

         if grade.lower() in ['a', 'a*']:
            high_grades_count += 1

      print(high_grades_count)
      if valid is True and high_grades_count < 3:
         flash('You must receive at least 3 A or A* grades.', category='error')
         return render_template('Student_grades.html')

      # Process valid subject-grade pairs here, sg_pairs contains all valid pairs
      return 'You are eligible for a computer science degree at Birmingham University!'

   return render_template('Student_grades.html')


@app.route('/confirmation')
def confirmation():
   # Adjust confirmation handling as needed
   return 'Submission confirmed'


if __name__ == "__main__":
   app.run(debug=True)
