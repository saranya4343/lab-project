import pandas as pd
def load_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path,encoding="latin1")
        return dataset
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        exit()

def predict_gender(name, dataset):
    name = name.title()
    result = dataset[dataset['name'] == name]
    if not result.empty:
        return result.iloc[0]['gender']
    else:
        return "Unknown (Name not found in dataset)"
    if __name__ == "__main__":
        file_path = "D:\II MCA(SN LAB)\Indian-Names-genderwise.csv"
        dataset = load_dataset(file_path)
        name = input("Enter a name: ").strip()
        gender = predict_gender(name, dataset)
        print(f"The predicted gender for the name '{name}' is: {gender}")
