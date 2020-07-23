# EB2PY
My University Thesis: Plug-in in Rodin (Eclipse) that translates formal methods in Event-B to Python!

**Project Description**
Pending.

**How do I install it?**
Installing this Plug-in is incredibly easy.

Requirements:
  Rodin (v. 3.4 suggested)

1. You just need to download the .jar file (that you can find in the EB2PY_jar/ path of this repository) and copy it into the plugins/ path of your Rodin directory.
2. That's it :D!

**How do I make use of it?**

Requirements:
  Having the EB2PY Plug-in already installed.
  Python (v. 3.5+, but especially v. 3.7.2)
  Have a bit of knowledge about Event-B.
  Optional: Install Mypy if you want to check the typing of the generated .py files (by executing the -$mypy file.py- command).
  
Part I: Running the Translator.
1. Open Rodin. And create some amazing and correct Event-B models.
2. You will see a button named "EB2PY" in the upper menu of Rodin. After clicking that button, a drop-down list will pop. Click the only entry named "Sample Command".
3. That's it :D!

Part II: Understanding what happened after you ran the Translator.
- If Rodin showed no errors and the models contained operations that are supported by this translator, a message will pop telling you that the translation was a success. A directory named Output_EB2PY will be generated in the same directory of the current workspace being used by your Rodin instance.
- Inside that directory, you will find a directory for every (open) project that you had in your Rodin Instance. Inside every directory project, you will find a file for every context/machine that belonged to that project in Rodin.
- You will also find a directory for the Prelude (which is file that includes all the necessary dependencies that allow our generated work to be executed).
  
Part III: Executing a generated file.
There are two cases:
  - You want to run a Context File: Inside the Context file there will be a class that represents the Context that you had in Rodin. You can create an object of that class and call the checkedInit method to initialize the constants and 'Carrier Sets' of that context (you can specify their values, or you can allow the Prelude try to give values to those constants (if the context is extending another context, you can include your own object of the extended context class as a parameter, or you can let the Prelude try to do that job for you). Note: This translator has only one special case that require the user to edit the generated code. If you want to specify the size of a 'Carrier Set', you will need to change it directly in the code (something that you can do in the section just above the definition of the context's class).
  - You want to run a Machine File: Inside the Context file there will be a class that represents the Context that you had in Rodin. When creating an instance of a machine class, the constructor will automatically call the actions of the INITIALISATION event (from the corresponding machine that you had in the Event-B model) to initialize the variables. If that machine 'sees' a context, a context object of the corresponding context class will be a parameter of the constructor of the class (which you can specify, or again, you can let the Prelude try to do all the job). If that machine is refining another machine, the refined machine will be the parent class from the concrete machine.

Have some fun with the Plug-in!
