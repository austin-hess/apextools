### Installation
```
git clone https://github.com/hessbag/apextools.git
cd ./apextools && pip install -r requirements.txt
```

### Usage
##### Fixing WSDL Inconsistencies
This will fix the inconsistencies in the WSDL-generated classes and save the changes to the same files
```
./apextools fix-classes -p path/to/class1,path/to/class2
```

##### Generating test class for schema classes
This will generate a test class that gets code coverage for a Schema class
```
./apextools gen-tests -c path/to/class -o path/to/newtestclass
```