create table UserAccount (
    login varchar(50) primary key,
    password varchar(50) not null,
    accountStatus boolean not null,
    datetimeAuthorized timestamp
);

create table Manager (
    login varchar(50) primary key references UserAccount on delete cascade on update cascade,
    lastname varchar(30) not null,
    firstname varchar(30) not null,
    patronymic varchar(30) not null
);

create table Performer (
    login varchar(50) primary key references UserAccount on delete cascade on update cascade,
    lastname varchar(30) not null,
    firstname varchar(30) not null,
    patronymic varchar(30) not null,
    grade varchar(20) not null,
    manager varchar(50) not null references Manager (login) on delete cascade on update cascade
);

create table Task (
    taskId serial primary key,
    taskName varchar(50) not null,
    aboutOfTask varchar(100) not null,
    periodOfExecution date not null,
    dateOfCompletion date,
    taskComplexity smallint not null,
    timeToCompleteTheTask smallint not null,
    taskStatus varchar(20) not null,
    natureOfTheTask varchar(50) not null,
    taskPerformer varchar(50) references Performer (login) on delete cascade on update cascade
);

create table ListOfCoefficient (
    manager varchar(50) primary key references Manager (login) on delete cascade on update cascade,
    minimumWageGm integer not null,
    timeToCompleteTheTaskTi smallint not null,
    coefficientOfCostTimeTc smallint not null,
    taskComplexityDi smallint not null,
    coefficientOfTaskComplexityDe smallint not null,
    coefficientOfNatureOfWorkCi real not null,
    forConvertedIntoCashTb smallint not null
);

insert into UserAccount values ('user1', 'pass', true, '2020-01-01');
insert into UserAccount values ('user2', 'pass', true, '2020-01-01');
insert into Manager values ('user2', 'Сидоров', 'Николай', 'Викторович');
insert into Performer values ('user1', 'Петров', 'Иван', 'Сергеевич', 'Middle', 'user2');
insert into Task values (1, 'Новая задача', 'Описание задачи', '2020-01-01', '2020-01-01', '30', '20', 'Исполняется', 'Установка оборудования', 'user1');