import re

def generate_tests(schema_class_path, output_path):

    # list of class names to be instantiated - first element should be the parent class
    class_names = []
    class_pattern = re.compile("(public class )([a-zA-Z0-9_]+)( {)")

    with open(schema_class_path, 'r') as f:
        for line in f.readlines():
            m = re.search(class_pattern, line)
            if m is not None:
                class_names.append(m.group(2))

    print(class_names)

    if len(class_names) > 1:
        with open(output_path, 'w') as f:
            f.write("@IsTest\npublic class {}Test {{\n".format(class_names[0]))
            f.write("\t@IsTest\n\tpublic static void testAllTypes() {\n")
            for i in range(1, len(class_names)):
                type_to_write = "{}.{}".format(class_names[0], class_names[i])
                f.write("\t\t{} type{} = new {}();\n".format(type_to_write, str(i), type_to_write))
            f.write("\t}\n}")
