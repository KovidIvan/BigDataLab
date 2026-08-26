--ЗАПРОС 1: Количество отличных оценок которые ставит препод
--Вопрос: Сколько высоких оценок (балл больше 90) поставил каждый преподаватель за всё время?

SELECT 
    p.full_name AS "Преподаватель",
    COUNT(f.student_id) AS "Количество отличных оценок"
FROM Fact_Exam_Results f
JOIN Dim_Professor p ON f.professor_id = p.professor_id
WHERE f.score > 90
GROUP BY p.full_name
ORDER BY "Количество отличных оценок" DESC;

--ЗАПРОС 2: Средний балл студентов по факультетам
--Вопрос: Какой средний балл получают студенты на каждом из факультетов? 
SELECT 
    s.faculty AS "Факультет",
    AVG(f.score) AS "Средний балл"
FROM Fact_Exam_Results f
JOIN Dim_Student s ON f.student_id = s.student_id
GROUP BY s.faculty
ORDER BY "Средний балл" DESC;


--ЗАПРОС 3: Количество пересдач по конкретным предметам в Осеннем семестре
--Вопрос: Сколько раз студентам приходилось идти на пересдачу по каждой дисциплине в осеннем семестре?

SELECT 
    c.course_name AS "Дисциплина",
    COUNT(f.student_id) AS "Количество пересдач"
FROM Fact_Exam_Results f
JOIN Dim_Course c ON f.course_id = c.course_id
JOIN Dim_Date d ON f.date_id = d.date_id
WHERE f.attempt_number > 1 AND d.semester = 'Осенний'
GROUP BY c.course_name
ORDER BY "Количество пересдач" DESC;


--ЗАПРОС 4: Максимальный и минимальный балл на коммерческом обучении
--Вопрос: Какой самый высокий и самый низкий балл получали студенты платной формы обучения по каждому курсу?

SELECT 
    c.course_name AS "Дисциплина",
    MAX(f.score) AS "Самый высокий балл",
    MIN(f.score) AS "Самый низкий балл"
FROM Fact_Exam_Results f
JOIN Dim_Course c ON f.course_id = c.course_id
JOIN Dim_Student s ON f.student_id = s.student_id
WHERE s.study_form = 'Платное'
GROUP BY c.course_name;

