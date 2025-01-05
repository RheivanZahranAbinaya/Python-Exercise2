import calendar

def interactive_calendar(year, month):
    print(calendar.month(year, month))

year = int(input("Masukkan tahun: "))
month = int(input("Masukkan bulan (1-12): "))
interactive_calendar(year, month)