create table Death_byState_2021 (
	Year_2021 Int  NOT NULL,
	State varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric  NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric  NOT NULL,
	Influenza_Deaths numeric  NOT NULL,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric  NOT NULL,
	PRIMARY KEY (State)
);
select * from Death_byState_2023 

create table Death_byState_2022 (
	Year_2022 Int NOT NULL,
	State varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric NOT NULL,
	Influenza_Deaths numeric not null,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric NOT NULL,
	PRIMARY KEY (State)
);
	
create table Death_byState_2023 (
	Year_2023 Int NOT NULL,
	State varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric NOT NULL,
	Influenza_Deaths numeric NOT NULL,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric NOT NULL,
	PRIMARY KEY (State)
);
	
CREATE TABLE Death_bySex_2021 (
	Year_2021 Int NOT NULL,
	State varchar NOT NULL,
	Sex varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric NOT NULL,
	Influenza_Deaths numeric NOT NULL,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric NOT NULL
);

CREATE TABLE Death_bySex_2022 (
	Year_2022 int NOT NULL,
	State varchar NOT NULL,
	Sex varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric NOT NULL,
	Influenza_Deaths numeric NOT NULL,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric NOT NULL
);

CREATE TABLE Death_bySex_2023 (
	Year_2023 Int NOT NULL,
	State varchar NOT NULL,
	Sex varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric NOT NULL,
	Influenza_Deaths numeric NOT NULL,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric NOT NULL	
);


CREATE TABLE Death_byAge_2021 (
	Year_2021 Int NOT NULL,
	State varchar NOT NULL,
	Age_Group varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric NOT NULL,
	Influenza_Deaths numeric NOT NULL,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric NOT NULL	
);

CREATE TABLE Death_byAge_2022 (
	Year_2022 Int NOT NULL,
	State varchar NOT NULL,
	Age_Group varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric NOT NULL,
	Influenza_Deaths numeric NOT NULL,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric NOT NULL	
);


CREATE TABLE Death_byAge_2023 (
	Year_2023 Int NOT NULL,
	State varchar NOT NULL,
	Age_Group varchar NOT NULL,
	COVID_19_Deaths numeric NOT NULL,
	Total_Deaths numeric NOT NULL,
	Pneumonia_Deaths numeric NOT NULL,
	Pneumonia_and_COVID_19_Deaths numeric NOT NULL,
	Influenza_Deaths numeric NOT NULL,
	Pneumonia_Influenza_or_COVID_19_Deaths numeric NOT NULL	
);

CREATE TABLE Vaccination2021 (
	Year_2021 INT, 
	State VARCHAR, 
	Dose_1_Administered BIGINT,
	Series_Completed BIGINT
);
SELECT * FROM Vaccination2021;

CREATE TABLE Vaccination2022 (
	Year_2022 INT, 
	State VARCHAR, 
	Dose_1_Administered BIGINT,
	Series_Completed BIGINT
);
SELECT * FROM Vaccination2022;

CREATE TABLE Vaccination2023 (
	Year_2023 INT, 
	State VARCHAR, 
	Dose_1_Administered BIGINT,
	Series_Completed BIGINT
);
SELECT * FROM Vaccination2023;

drop table Vaccination2023;

CREATE TABLE State_Population (
    State varchar NOT NULL,
    Year_2020 int NOT NULL,
    Year_2021 int NOT NULL,
    Year_2022 int NOT NULL
);

SELECT Death_byState_2021.Total_Deaths, State_Population.Year_2021
INTO per_capita_byState_2021
FROM Death_byState_2021
JOIN State_Population ON Death_byState_2021.State = State_Population.State;

SELECT Death_byState_2022.Total_Deaths, State_Population.Year_2022
INTO per_capita_byState_2022
FROM Death_byState_2022
JOIN State_Population ON Death_byState_2022.State = State_Population.State;

ALTER TABLE per_capita_byState_2021
ADD COLUMN Deaths_Per_Capita_2021 FLOAT;

ALTER TABLE per_capita_byState_2022
ADD COLUMN Deaths_Per_Capita_2022 FLOAT;

UPDATE per_capita_byState_2021
SET Deaths_Per_Capita_2021 = (total_deaths / Year_2021)*100;

UPDATE per_capita_byState_2022
SET Deaths_Per_Capita_2022 = (total_deaths / Year_2022)*100;

SELECT * from per_capita_byState_2021;

SELECT * from per_capita_byState_2022;


select * from State_Population;
select * from Death_byAge_2021
select * from Death_bySex_2023;
select * from Death_byAge_2021
select * from Death_byAge_2021
