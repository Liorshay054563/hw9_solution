# start
import statistics

num_list: list[int] = []

SENTINEL = -999

while True:
    number: int = int(input('Enter a number between 1 -10:'))
    if number == SENTINEL:
        print('Stop')
        break
    if not 0 < number <= 10:
        continue
    num_list.append(number)
    print(f"statistics : [{number}] :{num_list.count(number)},", end=" ")
    print()
    # ככה הבנתי את השאלה - אם אחרי כל קלט אני צריך להדפיס את כמה מספרים נקלטו (מן הסתם אני לא ידפיס מספר שלא נקלט לכן לא יהיה לי מספר שנקלט 0 פעמים)
    # ולכן לא צריך להתשמש ב"count" אם הוא גדול מה 0
