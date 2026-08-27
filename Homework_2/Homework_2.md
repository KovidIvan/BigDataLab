# Система высшего образования – ER-диаграмма

## 1. Описание сценария
Разрабатывается информационная система для управления расписанием, преподавателями, студентами и группами студентов в вузе. Система обеспечивает хранение данных о преподавателях, студентах, группах и расписании занятий, а также связей между этими сущностями.

## 2. Сущности и атрибуты

### 2.1. Преподаватели (Professors)
Хранит информацию о преподавателях.

| Атрибут | Тип | Ограничения |
|---------|-----|-------------|
| `ProfessorID` | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| `FirstName` | VARCHAR(100) | NOT NULL |
| `LastName` | VARCHAR(100) | NOT NULL |

**Дополнительные ограничения:**
- `UQ_ProfessorFullName` – уникальность комбинации (`FirstName`, `LastName`).

---

### 2.2. Группы студентов (Groups)
Хранит информацию о группах.

| Атрибут | Тип | Ограничения |
|---------|-----|-------------|
| `GroupName` | VARCHAR(100) | PRIMARY KEY, NOT NULL, UNIQUE |
| `Faculty` | VARCHAR(100) | NOT NULL |

---

### 2.3. Студенты (Students)
Хранит информацию о студентах.

| Атрибут | Тип | Ограничения |
|---------|-----|-------------|
| `StudentID` | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| `FirstName` | VARCHAR(100) | NOT NULL |
| `LastName` | VARCHAR(100) | NOT NULL |
| `Group` | VARCHAR(100) | NOT NULL, FOREIGN KEY |

**Дополнительные ограничения:**
- `UQ_StudentFullName` – уникальность комбинации (`FirstName`, `LastName`).
- `FK_Students_Groups` – внешний ключ на `Groups(GroupName)`.

---

### 2.4. Расписание (Schedule)
Хранит информацию о расписании занятий.

| Атрибут | Тип | Ограничения |
|---------|-----|-------------|
| `ScheduleID` | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| `ProfessorLastName` | VARCHAR(100) | NOT NULL, FOREIGN KEY |
| `GroupName` | VARCHAR(100) | NOT NULL, FOREIGN KEY |
| `Subject` | VARCHAR(200) | NOT NULL |
| `DayOfWeek` | VARCHAR(20) | NOT NULL |
| `Classroom` | VARCHAR(50) | NOT NULL |

**Дополнительные ограничения:**
- `FK_Schedule_Professors` – внешний ключ на `Professors(LastName)` (требует уникальности `LastName`).
- `FK_Schedule_Groups` – внешний ключ на `Groups(GroupName)`.

---

## 3. Взаимосвязи

| Связь | Тип | Описание |
|-------|-----|----------|
| **Groups → Students** | Один-ко-многим | Одна группа может содержать множество студентов. Связь реализована через поле `Students.Group`, которое ссылается на `Groups.GroupName`. |
| **Professors → Schedule** | Один-ко-многим | Один преподаватель может вести несколько записей в расписании. Связь реализована через поле `Schedule.ProfessorLastName`, ссылающееся на `Professors.LastName`. |
| **Groups → Schedule** | Один-ко-многим | Одна группа может быть указана в нескольких записях расписания. Связь реализована через поле `Schedule.GroupName`, ссылающееся на `Groups.GroupName`. |

> **Примечание:**  
> Чтобы внешний ключ `Schedule.ProfessorLastName` мог ссылаться на `Professors.LastName`, на столбец `LastName` в таблице `Professors` наложено ограничение уникальности (добавлено в SQL-коде, так как иначе ссылка невозможна). Это небольшое отклонение от исходного текста, но оно необходимо для корректной работы схемы.

---

## 4. SQL-код для PostgreSQL

```sql
-- Создание таблицы Groups
CREATE TABLE Groups (
    GroupName VARCHAR(100) PRIMARY KEY,
    Faculty VARCHAR(100) NOT NULL
);

-- Создание таблицы Professors
CREATE TABLE Professors (
    ProfessorID INTEGER PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    CONSTRAINT UQ_ProfessorFullName UNIQUE (FirstName, LastName),
    CONSTRAINT UQ_ProfessorLastName UNIQUE (LastName)   -- добавлено для внешнего ключа
);

-- Создание таблицы Students
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    "Group" VARCHAR(100) NOT NULL,
    CONSTRAINT UQ_StudentFullName UNIQUE (FirstName, LastName),
    CONSTRAINT FK_Students_Groups FOREIGN KEY ("Group") REFERENCES Groups(GroupName)
);

-- Создание таблицы Schedule
CREATE TABLE Schedule (
    ScheduleID INTEGER PRIMARY KEY,
    ProfessorLastName VARCHAR(100) NOT NULL,
    GroupName VARCHAR(100) NOT NULL,
    Subject VARCHAR(200) NOT NULL,
    DayOfWeek VARCHAR(20) NOT NULL,
    Classroom VARCHAR(50) NOT NULL,
    CONSTRAINT FK_Schedule_Professors FOREIGN KEY (ProfessorLastName) REFERENCES Professors(LastName),
    CONSTRAINT FK_Schedule_Groups FOREIGN KEY (GroupName) REFERENCES Groups(GroupName)
);