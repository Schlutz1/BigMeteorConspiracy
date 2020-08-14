# File to wrap getting perisher data

# imports
from selenium import webdriver
import pandas as pd
import time

# globals
DAY_RANGE = 16
ENTRY_RANGE = 7

perisher_endpoint = 'https://www.perisher.com.au/reports-cams/reports/weather-forecast'
perisher_xpath = '/html/body/div[2]/div[2]/section[1]/div/div[2]/div[7]/table/tbody/tr[{day}]/td[{entry}]'


class PerisherWrapper():

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def findPerisherForecast(self):
        ''' Extracts current Perisher 14 day Forecast '''

        headers_forecast = {1: "forecast_date"}
        df_forecast = []

        self.driver.get(perisher_endpoint)
        time.sleep(3)

        for day in range(1, DAY_RANGE):
            _ = {}
            for entry in range(1, ENTRY_RANGE):
                var = self.driver.find_element_by_xpath(perisher_xpath.format(
                    day=day,
                    entry=entry
                ))
                if day == 1 and entry != 1:  # param the headers, skip first empty column
                    headers_forecast[entry] = var.text.replace(" ","_").lower()
                else:
                    _[headers_forecast[entry]] = var.text

            if day > 1:
                df_forecast.append(_)

        # restructure, quit, and return
        df_forecast = pd.DataFrame(df_forecast)
        self.driver.quit()
        return df_forecast

    def parseSnowForecast(self, level):
        level = level.replace("cm", "")

        if level == 'Nil':
            return 0

        if "<" in level:
            return level.split("<")[1]

        if "-" in level:
            min = level.split("-")[0]
            max = level.split("-")[1]
            return (int(max) + int(min))/2
