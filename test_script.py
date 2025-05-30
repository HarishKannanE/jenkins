# test_script.py
def main():
    print("Running CI build simulation in Jenkins!")
    with open("output.txt", "w") as f:
        f.write("Build Success\n")

if __name__ == "__main__":
    main()

