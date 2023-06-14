def test(x):
    try:
        y = int(x)
        wynik = 6 / x
        assert x > 0
        raise
    except ValueError:
        print("Wpisz liczbe")
    except ZeroDivisionError:
        print("Nie wpisuj zera!")
    except AssertionError:
        print("Blad assertion")
    except RuntimeError:
        print("Wszystko dziala")


def main():
    test(5)

main()