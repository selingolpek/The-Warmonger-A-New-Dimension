	While implementing this project, some of the implementation details has been ignored/changed because of the nature of Python programming language. These are listed below:

Faction class and its subclasses has a Faction pointer representing first enemy and second enemy
Merchant class has a Faction pointer representing first and second faction in the battlefield

Pointers does not exist natively in Python. Type hinting was used for this to inform the developers.

It should be noted that if the related methods function when given variables of different type, no errors will be generated. Type hinting is only meant to hint the IDE and developers.


  

Merchant class has a fixed starting armor point (ap)and weapon point (wp). The constructor should optionally take the starting weapon point and starting armor point attributes.
	
	   In other programming language, this could be solved by 	keeping these variables as private, and make them 	accessible only with the getter function. But Python does 	not have private variables.
	

The ap and wp could be set as properties but when they're given as parameters, setter functions would be needed to be implemented. But since they could be reassigned with the setter functions whenever desired, ap and wp would be not be "fixed"


	The ap and wp could be implemented as methods, such as:

	def A_CONSTANT():
    			return "constant" 

	but value this could be changed by calling
	A_CONSTANT = lambda: 'not constant anymore :/'

And the optional parameter passing also makes this approach impossible.



