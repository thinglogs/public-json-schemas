import glob

schema_files = glob.glob("./schemas/*")
print(schema_files)

with open("README.md", "a") as myfile:
    for schema_file in schema_files:
        myfile.write("- "+schema_file+"\n")
