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
    Clouds ,
    Visibility,
    Wind_Speed,
    Wind_Direction,
    Conditions
);
