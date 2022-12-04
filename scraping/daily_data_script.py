from datetime import datetime

from utils.abbreviate_team_names import add_abbreviated_team_names
from scraping.scrape_advancedteamstats import scrape_alladvanced
from scraping.scrape_stats_cli import get_singleseason_stats
from scraping.scrape_stats_cli import get_typeKey
from scraping.scrape_stats_cli import years_areValid
from scraping.scrape_teamrecords import scrape_all_team_records
from utils.csv_functions import make_dir_if_nonexistent
from utils.csv_functions import reset_csv

shortDate = datetime.today().strftime('%Y-%m-%d')
shortDate_nodash = shortDate.replace('-', '')

directory = './baseData/dailystats'
mkdir = (f'{directory}/{shortDate}')
make_dir_if_nonexistent(mkdir)


def save_each_season_stats_daily(statType, yearStart, yearEnd):

    if years_areValid(statType, yearStart, yearEnd):
        yearList = list(range(int(yearStart), int(yearEnd) + 1))
        typeKey = get_typeKey(statType)

        for year in yearList:
            URL = (
                f'https://www.basketball-reference.com/leagues/NBA_{year}_{typeKey}.html'
            )
            # f-stringed
            fileName = (f'{mkdir}/{typeKey}_{shortDate_nodash}.csv')
            reset_csv(fileName)
            get_singleseason_stats(year, URL, fileName, True)
            # f-stringed
            print(
                (f'Finished populating season {year - 1}-{year}, {typeKey} data.'),
            )
    else:
        return False


def daily_data_script():
    save_each_season_stats_daily('-tot', '2022', '2022')
    save_each_season_stats_daily('-adv', '2022', '2022')
    scrape_all_team_records(
        (f'{mkdir}/teamStandings_{shortDate_nodash}.csv'), 2022, 2022,
    )
    add_abbreviated_team_names(
        (f'{mkdir}/teamStandings_{shortDate_nodash}.csv'),
    )
    scrape_alladvanced(f'{mkdir}', '1980', '2022')


def main():
    daily_data_script()


if __name__ == '__main__':
    main()