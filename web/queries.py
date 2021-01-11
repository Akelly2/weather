current_sql = """ 
    select 
        cast("datetime" + interval '1 second' * timezone_offset as varchar(100)) datetime,
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
        initcap(Condition_Description) Condition_Description,
        Icon_Code,
        Probability_of_Precipitation,
        Current_or_Forecast,
        l.Location_Key, 
        City,
        Region
    from Weather_Hourly w 
        join "Location" l on w.Location_Key = l.Location_Key
    where City = ? 
        and Current_or_Forecast = 'Current' """

hourly_sql = """ 
    select 
        trim(leading '0' from cast(to_char("datetime" + interval '1 second' * timezone_offset, 'hh12 AM') as varchar(20))) datetime,  
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
        initcap(Condition_Description) Condition_Description,
        Icon_Code,
        Probability_of_Precipitation,
        Current_or_Forecast,
        l.Location_Key,
        City,
        Region
    from Weather_Hourly w 
        join "Location" l on w.Location_Key = l.Location_Key
    where City = ? 
        and Current_or_Forecast = 'Forecast' """

daily_sql = """
    select 
        cast("datetime" as varchar(100)) as datetime,
        initcap(to_char("datetime", 'day')) as day_of_week,
        trim(leading '0' from cast(to_char(Sunrise + interval '1 second' * timezone_offset, 'hh12:mi AM') as varchar(20))) sunrise,  
        trim(leading '0' from cast(to_char(Sunset + interval '1 second' * timezone_offset, 'hh12:mi AM') as varchar(20))) sunset,
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
        cast(Min_Temp as int) Min_Temp,
        cast(Max_Temp as int) Max_Temp,
        Night_Temp,
        Evening_Temp,
        Morning_Temp,
        Day_FL,
        Night_FL,
        Evening_FL,
        Morning_FL,
        Condition_Name,
        initcap(Condition_Description) Condition_Description,
        Icon_Code,
        l.Location_Key,
        City,
        Region,
        Current_or_Forecast
    from Weather_Daily w 
        join "Location" l on w.location_key=l.location_key
    where City = ?"""

location_search_sql = """
        select 
            City, 
            Region, 
            Country 
        from "Location"
        where 
            lower(City) like lower(?)
        order by City asc
        limit 20
    """    

