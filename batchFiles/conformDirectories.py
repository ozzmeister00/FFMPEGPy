import os

baseDir = "G:\GoPro"

for dirPath, dirNames, files in os.walk(baseDir):
    for filename in files:
        basePath = os.path.join(dirPath, filename)
        if " " in basePath:
            renamed = basePath.replace(' ', '_')
            renamedDir, renamedFile = os.path.split(renamed)
            if not os.path.exists(renamedDir):
                print("making directory", renamedDir)
                os.makedirs(renamedDir)

            print(basePath, renamed)
            os.rename(basePath, renamed)

print("done")