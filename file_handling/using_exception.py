try:
   f=open("greeating.txt","r")
   data=f.read()
   print(data)
   
except (FileNotFoundError,FileExistsError) as e:
    print("error",e) 


#filenotfound
#fileexists
#permissioneroor
#isadirectoryerror
#notadirectoryerror
#oserror
