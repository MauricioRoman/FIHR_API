from FHIRstats import *
import sys

def main():

    cls = FIHR_stats()
    cls.load_stats("records_unique.json")

    cls.stats_to_df()
    cls.df.to_csv("records_unique.csv")

if __name__ == '__main__':
        sys.exit(main())