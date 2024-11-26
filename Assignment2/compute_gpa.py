from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local", "GPA Computation")
spark = SparkSession.builder.appName("GPA Computation").getOrCreate()


grades = sc.textFile("/opt/spark/data/grades.txt")
credits = sc.textFile("/opt/spark/data/academic_credit.txt")


def score_to_gpa(score):
    score = int(score)
    if 90 <= score <= 100:
        return 4.5
    elif 85 <= score <= 89:
        return 4.0
    elif 80 <= score <= 84:
        return 3.7
    elif 77 <= score <= 79:
        return 3.3
    elif 73 <= score <= 76:
        return 3.0
    elif 70 <= score <= 72:
        return 2.7
    elif 67 <= score <= 69:
        return 2.5
    elif 63 <= score <= 66:
        return 2.3
    elif 60 <= score <= 62:
        return 2.0
    elif 50 <= score <= 59:
        return 1.0
    else:
        return 0.0

def parse_credits(line):
    try:
        parts = line.split(":")
        if len(parts) == 2:
            course_id, credit = parts[0], int(parts[1])
            return course_id, credit
        else:
            raise ValueError("Invalid format")
    except Exception as e:
        print(f"Error parsing line: {line}, Error: {e}")
        return None


course_credits = credits.map(parse_credits).filter(lambda x: x is not None).collectAsMap()


def compute_gpa(student_record):
    fields = student_record.split()
    student_id = fields[0]
    courses = fields[1:]
    total_points = 0
    total_credits = 0
    for i in range(0, len(courses), 2):
        course_id = courses[i]
        grade = courses[i + 1]
        if course_id in course_credits:
            gpa = score_to_gpa(grade)
            credit = course_credits[course_id]
            total_points += gpa * credit
            total_credits += credit
    gpa = total_points / total_credits if total_credits > 0 else 0
    return student_id, round(gpa, 3)


student_gpas = grades.map(compute_gpa)


course_stats = grades \
    .flatMap(lambda line: [(line.split()[i], int(line.split()[i + 1])) for i in range(1, len(line.split()), 2)]) \
    .map(lambda x: (x[0], (score_to_gpa(x[1]), 1))) \
    .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1])) \
    .mapValues(lambda x: (round(x[0] / x[1], 3), x[1]))


failure_rates = grades \
    .flatMap(lambda line: [(line.split()[i], int(line.split()[i + 1])) for i in range(1, len(line.split()), 2)]) \
    .map(lambda x: (x[0], 1 if x[1] < 60 else 0)) \
    .reduceByKey(lambda a, b: a + b) \
    .leftOuterJoin(course_stats) \
    .mapValues(lambda x: round(x[0] / x[1][1], 3) if x[1] is not None else 0)  


student_gpas.saveAsTextFile("/opt/spark/data/output_student_gpas")
course_stats.saveAsTextFile("/opt/spark/data/output_course_stats")
failure_rates.saveAsTextFile("/opt/spark/data/output_failure_rates")

print("Results saved to /opt/spark/data/output_student_gpas, output_course_stats, output_failure_rates")