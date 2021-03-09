# we want to use the module
#import module
import module as external_module
import module2
#print(module.b)
print(f"b = {external_module.b}")
print(f"b - {module2.b}")

# I want to call the function in the module:
#module.function_in_module()
external_module.function_in_module()
