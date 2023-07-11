DROP TABLE Vaccination2021;
DROP TABLE Vaccination2022;
DROP TABLE Vaccination2023;

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