import json
file = '/Users/pmerkushkin/PycharmProjects/qa-auto-engineer-python-tw-project-50/files/file1.json'
def main():
    p = json.load(open(file))
    print(json.dumps(p, indent=4))

if __name__ == '__main__':
    main()