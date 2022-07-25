from test_package import TestObject
obj_1 = TestObject("HelloWorld")
obj_1.print_name()

# (base) onyr@ly-vm-rd-es-ubuntu1:~/missing_import_custom_package$ conda activate elastic
# (elastic) onyr@ly-vm-rd-es-ubuntu1:~/missing_import_custom_package$ cd src/
# (elastic) onyr@ly-vm-rd-es-ubuntu1:~/missing_import_custom_package/src$ python main.py 
# TestObject(HelloWorld)
# TestObject(HelloWorld)