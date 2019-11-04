import json


OD_CONFIG_COLUMN_NAME = "Configuration"
CLASSIFIER_COLUMN_NAME = "Classifier"
OD_JSONS_DIRECTORY = "OD_jsons"
CSV_NAME_INPUT = "accurracyTemp.csv"
CSV_NAME_OUTPUT = "accuracyTransformed.csv"

JSONFiles = dict()
with open(CSV_NAME_INPUT) as accFile, open(CSV_NAME_OUTPUT, "w") as accFileNew:
    line = accFile.readline()
    columnsArr = line.split(",")
    ODConfigurationColumnIndex = columnsArr.index(OD_CONFIG_COLUMN_NAME)
    for line in accFile:
        dataArr = line.split(",")
        if not len(dataArr) > 1:  # here we check for the final newline in the csv to skip it
            continue
        JSON_OD_hash = dataArr[ODConfigurationColumnIndex]
        classifier = dataArr[columnsArr.index(CLASSIFIER_COLUMN_NAME)].split(".")[-1]

        if JSON_OD_hash not in JSONFiles:
            JSONFiles[JSON_OD_hash] = open(OD_JSONS_DIRECTORY + ("" if OD_JSONS_DIRECTORY[-1] == "/" else "/") +
                                           classifier + "_" + JSON_OD_hash + ".json", "r", encoding="UTF-8")
        else:
            JSONFiles[JSON_OD_hash].seek(0)

        #print(line)

        od_config = json.load(JSONFiles[JSON_OD_hash])  # loads json configuration as a dict
        parametersStr = str.join(";", ['"{}":"{}"'.format(k, v) for k, v in od_config["ad_config"]["parameters"].items()])
        dataArr[ODConfigurationColumnIndex] = parametersStr


        #print(str.join(",", dataArr))
        accFileNew.write(str.join(",", dataArr))

