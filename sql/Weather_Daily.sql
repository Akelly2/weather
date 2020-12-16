CREATE TABLE Weather_Daily (
    "datetime" TIMESTAMP,
    Current_or_Forecast VARCHAR(15),
    Location_Key INT, 
    Day_Temp REAL,
    Min_Temp REAL,
    Max_Temp REAL,
    Night_Temp REAL,
    Evening_Temp REAL,
    Morning_Temp REAL, 
    Day_FL REAL,
    Night_FL REAL,
    Evening_FL REAL,
    Morning_FL REAL,
    Pressure SMALLINT,
    Humidity SMALLINT,
    Dew_Point REAL,
    UVI REAL,
    Clouds SMALLINT,
    Visibility INT,
    Wind_Speed REAL,
    Wind_Direction SMALLINT,
    Probability_of_Precipitation REAL,
    Rain_mm VARCHAR(100),
    Snow_mm VARCHAR(100),
    Condition_Name VARCHAR(100),
    Condition_Description VARCHAR(100),
    Sunrise TIMESTAMP,
    Sunset TIMESTAMP
);
