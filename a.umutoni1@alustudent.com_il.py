# Creating Assignment class 
class Assignment:
    # Initializing Assignment objects with the required parameters.
    def __init__(self, name, assignment_type, score, weight):
        self.name = name
        self.assignment_type = assignment_type
        self.score = score
        self.weight = weight

    # Calculating the weighted score for the entered assignment based on its weight.
    def weighted_score(self):
        return (self.score * self.weight) / 100


# Creating Student class
class Student:
    # Initializing a Student object with the given name and an empty list of assignments.
    def __init__(self, name):
        self.name = name
        self.assignments = []

    # Adding the entered assignment to the list of assignments.
    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    # Calculating total assignments scores.
    def calculate_scores(self):
        formative_total = 0
        summative_total = 0
        formative_weight = 0
        summative_weight = 0

        for assignment in self.assignments:
            if assignment.assignment_type == 'Formative':
                formative_total += assignment.weighted_score()
                formative_weight += assignment.weight
            elif assignment.assignment_type == 'Summative':
                summative_total += assignment.weighted_score()
                summative_weight += assignment.weight

        # Making sure that entered weights are not exceeding 60 for formatives nor 40 for summatives
        if formative_weight > 60 or summative_weight > 40:
            raise ValueError("Total weights exceed the allowed limits.")

        return formative_total, summative_total

    # Checking if the student has passed or failed the course based on their scores.
    def check_progression(self):
        formative_total, summative_total = self.calculate_scores()
        passed_formative = formative_total >= 30
        passed_summative = summative_total >= 20

        if passed_formative and passed_summative:
            return "You have passed the course."
        else:
            return "You have failed the course and must retake it."

    # Identifying all Formative assignments eligible for resubmission.
    def check_resubmission(self):
        resubmission_assignments = []
        for assignment in self.assignments:
            if assignment.assignment_type == 'Formative' and assignment.score < 50:
                resubmission_assignments.append(assignment)
        return resubmission_assignments

    # Generating and displaying this student's transcript.
    def generate_transcript(self, order='ascending'):
        # Sorting assignments based on score, in the chosen order
        sorted_assignments = sorted(self.assignments, key=lambda x: x.score, reverse=(order == 'descending'))
        print("\nTranscript Breakdown ({} Order):".format(order.capitalize()))
        print("Assignment          Type            Score(%)    Weight (%)")
        print("-----------------------------------------------------------")
        for assignment in sorted_assignments:
            print(f"{assignment.name:<20} {assignment.assignment_type:<15} {assignment.score:<10} {assignment.weight:<10}")
        print("-----------------------------------------------------------")


# Main function to interact with the user for inputs.
def main():
    student_name = input("Hello, enter student name please: ")
    student = Student(student_name)

    while True:
        name = input("Enter assignment name (or type 'done' to proceed): ")
        if name.lower() == 'done':
            break
        assignment_type = input("Enter assignment type (Formative/Summative): ")
        while assignment_type not in ['Formative', 'Summative']:
            print ("Invalid input, try again!")
            assignment_type = input("Enter assignment type (Formative/Summative): ")
            
        score = float(input("Enter assignment score: "))
        weight = float(input("Enter assignment weight: "))

        assignment = Assignment(name, assignment_type, score, weight)
        student.add_assignment(assignment)

    # Calculate scores and check progression
    try:
        formative_total, summative_total = student.calculate_scores()
        print(f"\nFormative Total: {formative_total:.2f}%")
        print(f"Summative Total: {summative_total:.2f}%")
        print(student.check_progression())

        # Check for resubmission eligibility
        resubmissions = student.check_resubmission()
        if resubmissions:
            print("You are eligible for resubmission for the following assignments:")
            for resub in resubmissions:
                print(f"- {resub.name} (Score: {resub.score}%)")

        # Asking preferred order to display transcript
        order = input("Would you like the transcript displayed in ascending or descending order? ")
        student.generate_transcript(order)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

