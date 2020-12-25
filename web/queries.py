current_sql = """ 
    select 
        cast("datetime" as varchar(100)) datetime,
        cast (Temperature as int) Temperature,
        cast (Feels_Like as int) Feels_Like,
        Pressure,
        Humidity,
        Dew_Point,
        UVI,
        Clouds,
        Visibility,
        Wind_Speed,
        Wind_Direction,
        Rain_mm,
        Snow_mm,
        Condition_Name,
        Condition_Description,
        Probability_of_Precipitation,
        Current_or_Forecast,
        l.Location_Key 
    from Weather_Hourly w 
        join "Location" l on w.Location_Key = l.Location_Key
    where City = ? 
        and Current_or_Forecast = 'Current' """

hourly_sql = """ 
    select 
        cast("datetime" as varchar(100)) datetime,
        Temperature,
        Feels_Like,
        Pressure,
        Humidity,
        Dew_Point,
        UVI,
        Clouds,
        Visibility,
        Wind_Speed,
        Wind_Direction,
        Rain_mm,
        Snow_mm,
        Condition_Name,
        Condition_Description,
        Probability_of_Precipitation,
        Current_or_Forecast,
        l.Location_Key
    from Weather_Hourly w 
        join "Location" l on w.Location_Key = l.Location_Key
    where City = ? 
        and Current_or_Forecast = 'Forecast' """

daily_sql = """
    select 
        cast("datetime" as varchar(100)) as datetime,
        cast(Sunrise as varchar(100)) sunrise,
        cast(Sunset as varchar(100)) sunset,
        Pressure,
        Humidity,
        Dew_Point,
        Wind_Speed,
        Wind_Direction,
        Clouds,
        Probability_of_Precipitation,
        UVI,
        Rain_mm,
        Snow_mm,
        Day_Temp,
        Min_Temp,
        Max_Temp,
        Night_Temp,
        Evening_Temp,
        Morning_Temp,
        Day_FL,
        Night_FL,
        Evening_FL,
        Morning_FL,
        Condition_Name,
        Condition_Description,
        l.Location_Key,
        Current_or_Forecast
    from Weather_Daily w 
        join "Location" l on w.location_key=l.location_key
    where City = ?"""

    