DROP TABLE Weather_Hourly; 
CREATE TABLE Weather_Hourly (
    "datetime" TIMESTAMP,
    Current_or_Forecast VARCHAR(15),
    Location_Key SMALLINT,
    Temperature REAL,
    Feels_Like REAL,
    Pressure SMALLINT,
    Humidity SMALLINT,
    Dew_Point REAL,
    UVI REAL,
    Clouds SMALLINT,
    Visibility INT,
    Wind_Speed REAL,
    Wind_Direction SMALLINT,
    Probability_of_Precipitation REAL,
    Rain_mm REAL,
    Snow_mm REAL,
    Condition_Name VARCHAR(100),
    Condition_Description VARCHAR(100),
    Icon_Code CHAR(3)
);
