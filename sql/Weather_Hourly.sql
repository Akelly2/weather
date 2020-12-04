-- there is no intention to keep this data, it will be overwritten 
CREATE TABLE Weather_Hourly (
    "datetime" datetime,
    Current_or_Forecast varchar(15),
    Location_Key SMALLINT,
    Temperature REAL,
    Feels_Like REAL,
    Pressure SMALLINT,
    Humidity SMALLINT,
    Dew_Point REAL,
    Clouds SMALLINT,
    Visibility INT,
    Wind_Speed REAL,
    Wind_Direction SMALLINT,
    Probability_of_Precipitation REAL,
    Rain_mm VARCHAR(100),
    Snow_mm VARCHAR(100),
    Condition_Name VARCHAR(100),
    Condition_Description VARCHAR(100),

);
