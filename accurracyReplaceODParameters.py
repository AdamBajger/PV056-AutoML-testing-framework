import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Script replaces configuration hashes in an accurracy CSV file \
                    with actual OD configuration information."
    )
    parser.add_argument(
        "--input-csv",
        "-i",
        required=True,
        help="Filename of CSV file with CLFs accurracies.",
    )
    parser.add_argument(
        "--output-csv",
        "-o",
        required=False,
        default="accurracyTransformed.csv",
        help="Filename of new, transformed CSV file with CLFs accurracies and OD configurations. Default name is "
             "accurracyTransformed.csv",
    )
    parser.add_argument(
        "--od-jsons-dir",
        "-od",
        required=True,
        help="Name of a directory containing JSON files for CLF outputs (usually same directory as CLF outputs are in)",
    )
    args = vars(parser.parse_args())
    print(args)
    colname_od_config = "Configuration"
    colname_classifier = "Classifier"
    filename_od_json_directory = args["od-jsons-dir"]
    filename_csv_input = args["input-csv"]
    filename_csv_output = args["output-csv"]

    dict_json_files = dict()
    try:
        with open(filename_csv_input) as accFile, open(filename_csv_output, "w") as accFileNew:
            line = accFile.readline()
            arr_column = line.split(",")
            index_column_od_configuration = arr_column.index(colname_od_config)
            for line in accFile:
                arr_data = line.split(",")
                if not len(arr_data) > 1:  # here we check for the final newline in the csv to skip it
                    continue
                json_od_hash = arr_data[index_column_od_configuration]
                classifier = arr_data[arr_column.index(colname_classifier)].split(".")[-1]

                if json_od_hash not in dict_json_files:
                    dict_json_files[json_od_hash] = open(
                        filename_od_json_directory + ("" if filename_od_json_directory[-1] == "/" else "/") +
                        classifier + "_" + json_od_hash + ".json", "r", encoding="UTF-8")
                else:
                    dict_json_files[json_od_hash].seek(0)

                # print(line)

                od_config = json.load(dict_json_files[json_od_hash])  # loads json configuration as a dict
                od_configuration_human_readable = str.join(";", ['"{}":"{}"'.format(k, v) for k, v in
                                                                 od_config["ad_config"]["parameters"].items()])
                arr_data[index_column_od_configuration] = od_configuration_human_readable

                # print(str.join(",", dataArr))
                accFileNew.write(str.join(",", arr_data))
    except KeyboardInterrupt:
        print("\nInterupted!", flush=True, file=sys.stderr)

    print("Done")


if __name__ == "__main__":
    main()
