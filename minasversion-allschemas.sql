DROP TABLE Death_byState_2021;
DROP TABLE Death_byState_2022;
DROP TABLE Death_byState_2023;
DROP TABLE Death_bySex_2021;
DROP TABLE Death_bySex_2022;
DROP TABLE Death_bySex_2023;
DROP TABLE Death_byAge_2021;
DROP TABLE Death_byAge_2022;
DROP TABLE Death_byAge_2023;
DROP TABLE Vaccination2021;
DROP TABLE Vaccination2022;
DROP TABLE Vaccination2021and2022;
DROP TABLE State_Population;
DROP TABLE per_capita_byState_2021;
DROP TABLE per_capita_byState_2022;
DROP TABLE capital_coords;
DROP TABLE deaths_perstate_wCoords2021;
DROP TABLE deaths_perstate_wCoords2022;

CREATE TABLE Death_byState_2021 (
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
SELECT * FROM Death_byState_2021; 

CREATE TABLE Death_byState_2022 (
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
SELECT * FROM Death_byState_2022; 	

CREATE TABLE Death_byState_2023 (
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
SELECT * FROM Death_byState_2023; 

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
SELECT * FROM Death_bySex_2021; 

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
SELECT * FROM Death_bySex_2022; 

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

SELECT * FROM Death_bySex_2023; 

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
SELECT * FROM Death_byAge_2021; 

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

SELECT * FROM Death_byAge_2022; 

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
SELECT * FROM Death_byAge_2023; 

CREATE TABLE Vaccination2021 (
	Year_2021 INT, 
	State VARCHAR, 
	Dose_1_Administered NUMERIC ,
	Series_Completed NUMERIC 
);
SELECT * FROM Vaccination2021;

CREATE TABLE Vaccination2022 (
	Year_2022 INT, 
	State VARCHAR, 
	Dose_1_Administered NUMERIC,
	Series_Completed NUMERIC
);
SELECT * FROM Vaccination2022;

CREATE TABLE Vaccination2021and2022 (
	Years INT, 
	State VARCHAR, 
	Dose_1_Administered NUMERIC,
	Series_Completed NUMERIC
);
SELECT * FROM Vaccination2021and2022;

CREATE TABLE State_Population (
    State varchar NOT NULL,
    Year_2020 int NOT NULL,
    Year_2021 int NOT NULL,
    Year_2022 int NOT NULL
);
SELECT * FROM State_Population;

CREATE TABLE capital_coords(
	State VARCHAR, 
	Latitude DECIMAL, 
	Longitude DECIMAL
);

SELECT * FROM capital_coords;

SELECT Death_byState_2021.State, Death_byState_2021.Total_Deaths, State_Population.Year_2021
INTO per_capita_byState_2021
FROM Death_byState_2021
JOIN State_Population ON Death_byState_2021.State = State_Population.State;

ALTER TABLE per_capita_byState_2021
ADD COLUMN Deaths_Per_Capita_2021 FLOAT;
UPDATE per_capita_byState_2021
SET Deaths_Per_Capita_2021 = (total_deaths / Year_2021)*1000;

SELECT * from per_capita_byState_2021;

SELECT Death_byState_2022.State, Death_byState_2022.Total_Deaths, State_Population.Year_2022
INTO per_capita_byState_2022
FROM Death_byState_2022
JOIN State_Population ON Death_byState_2022.State = State_Population.State;

ALTER TABLE per_capita_byState_2022
ADD COLUMN Deaths_Per_Capita_2022 FLOAT;
UPDATE per_capita_byState_2022
SET Deaths_Per_Capita_2022 = (total_deaths / Year_2022)*1000;

SELECT * from per_capita_byState_2022;


SELECT per_capita_byState_2021.State, per_capita_byState_2021.Deaths_Per_Capita_2021, capital_coords.latitude, capital_coords.longitude 
INTO deaths_perstate_wCoords2021
FROM per_capita_byState_2021
JOIN capital_coords ON per_capita_byState_2021.State = capital_coords.State;

SELECT * from deaths_perstate_wCoords2021;


SELECT per_capita_byState_2022.State, per_capita_byState_2022.Deaths_Per_Capita_2022, capital_coords.latitude, capital_coords.longitude 
INTO deaths_perstate_wCoords2022
FROM per_capita_byState_2022
JOIN capital_coords ON per_capita_byState_2022.State = capital_coords.State;

SELECT * from deaths_perstate_wCoords2022;
