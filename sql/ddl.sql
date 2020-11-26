CREATE TABLE "Location" (
    Location_Key INT,
    City,
    Region,
    Country,
    Latitude,
    Longitude,
    Timezone
)

-- 
CREATE TABLE Weather_Daily (
    "datetime" BIGINT,
    Current_or_Forecast varchar(15),
    Temperature,
    Feels_Like,
    Pressure,
    Humidity,
    Dew_Point,
    Clouds,
    Visibility,
    Wind_Speed,
    Wind_Direction,
    Conditions,
    Sunrise,
    Sunset,
    Minimum_Temperature,
    Maximum_Temperature
)

-- there is no intention to keep this data, it will be overwritten 
CREATE TABLE Weather_Hourly (
    "datetime" BIGINT,
    Current_or_Forecast varchar(15),
    Temperature,
    Feels_Like,
    Pressure,
    Humidity,
    Dew_Point,
    Clouds,
    Visibility,
    Wind_Speed,
    Wind_Direction,
    Conditions
)
