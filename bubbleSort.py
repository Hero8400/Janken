from faker.factory import Factory


def main():
    Faker = Factory.create
    fake = Faker("ja_JP")
    nameList = list(map(lambda i: fake.romanized_name(), range(10)))
    print(nameList)
    nameSort(nameList)
    print(nameList)


def nameSort(nameList):
    nameList.sort()


if __name__ == "__main__":
    main()
