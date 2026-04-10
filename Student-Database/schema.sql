CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    marks INT
);

INSERT INTO Students VALUES
(1, 'Asha', 'CSE', 85),
(2, 'Ravi', 'ECE', 78),
(3, 'Priya', 'IT', 92),
(4, 'Kiran', 'CSE', 88);

-- View all students
SELECT * FROM Students;

-- Students with marks > 80
SELECT * FROM Students WHERE marks > 80;

-- Average marks
SELECT AVG(marks) FROM Students;

-- Group by department
SELECT department, AVG(marks) FROM Students GROUP BY department;
